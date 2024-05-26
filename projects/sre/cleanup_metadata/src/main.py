import os
import time
from datetime import datetime, timedelta

import yaml
from elasticsearch import Elasticsearch


#
# logging with levels
# config from the yaml
#


# def cleanup():
#     client = create_client()
#     healthcheck()
#     if not green:
#         wait  configuratble_minutes for configurable_time
#             if still not green -> exit
#
#     verify_index_exists
#     construct_query_for_ttl
#     do_search to determine amount of docs to deleve
#     if amount of docs to delete > configurable value -> log error and message slack
#     if all good -> run delete query
#     periodically query to see whether delete completed
#     log success->message slack
#
#
#

# Read config
def get_config(env):
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    config_path = os.path.abspath(config_path)
    with open(f"{config_path}", 'r') as stream:
        config = yaml.safe_load(stream)
    return config[env]


config = get_config('local')


def setup_client(cluster):
    return Elasticsearch([f'http://{cluster["name"]}:9200'])


def healthcheck_pass(es_client):
    return es_client.cluster.health()['status'] == 'green'


def index_exists(es_client, index):
    return es_client.indices.exists(index=index)


def get_total_docs_to_delete(es_client, cluster):
    response = es_client.count(index=cluster['index'], body={
        'query': {'range': {
            "timestamp": {"lte": f"now-{cluster['ttl']}"}}}})
    return response['count']


def delete_docs(es_client, cluster):
    response = es_client.delete_by_query(index=cluster['index'], body={
        'query': {'range': {
            "timestamp": {"lte": f"now-{cluster['ttl']}"}}}})
    return response


def abort_delete(docs_to_be_deleted, limit):
    return docs_to_be_deleted >= limit or docs_to_be_deleted == 0


def run():
    for cluster in config:
        es_client = setup_client(cluster)

        if not healthcheck_pass(es_client):
            raise RuntimeError("Cluster not in a healthy state")
            # attempt = 1
            # while (attempt < cluster['max_attempts'] ):
            #     time.sleep(5)
            #     health = healthcheck_pass(es_client)
            #     print('handle error when connecting to Elasticsearch. notify slack')
            #     attempt = +1
            #     if attempt == cluster['max_attempts']:
            #         raise RuntimeError('Max attempts reached')

        if not index_exists(es_client, cluster['index']):
            print('index does not exist. add to error list. notify slack')
            continue

        docs_to_be_deleted = get_total_docs_to_delete(es_client, cluster)

        if abort_delete(docs_to_be_deleted, cluster['circuit_breaker_docs']):
            print('too many docs to be deleted. notify slack')
            continue

        delete_docs(es_client, cluster)

        print(docs_to_be_deleted)


if __name__ == '__main__':
    run()
# for each entry in config:
#     do cleanup()
