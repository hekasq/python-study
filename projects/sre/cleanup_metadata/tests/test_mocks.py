import pytest
from elasticsearch import Elasticsearch, RequestsHttpConnection
import responses
import yaml
import os

from projects.sre.cleanup_metadata.src.main import healthcheck_pass, index_exists

# Read config
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
config_path = os.path.abspath(config_path)
with open(f"{config_path}", 'r') as stream:
    config = yaml.safe_load(stream)

cluster_info = config['local'][0]
ttl = cluster_info['ttl']
cluster_url = f'http://{cluster_info['name']}:9200'


@pytest.fixture
def mock_es_client():
    es_client = Elasticsearch([f'{cluster_url}'], connection_class=RequestsHttpConnection)
    return es_client


@responses.activate
def test_healthcheck(mock_es_client):
    responses.add(responses.GET, f'{cluster_url}/_cluster/health', json={"status": "green"}, status=200)
    health = healthcheck_pass(mock_es_client)
    assert health


@responses.activate
def test_index_exists(mock_es_client):
    index = cluster_info['index']
    url = f"{cluster_url}/{index}"
    responses.add(responses.HEAD, url, json={f"{index}": {"aliases": {}, "mappings": {
        "properties": {"OS_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                       "host_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                       "platform": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                       "process_id": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                       "program_id": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                       "region": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                       "timestamp": {"type": "date"}}}, "settings": {
        "index": {"routing": {"allocation": {"include": {"_tier_preference": "data_hot"}}}, "number_of_shards": "20",
                  "provided_name": "logs", "creation_date": "1716754633220", "number_of_replicas": "1",
                  "uuid": "_oBZvDQxRYGrbBE-Juo4UQ", "version": {"created": "8503000"}}}}}, status=200)
    exists = index_exists(mock_es_client, cluster_info['index'])
    assert exists

@responses.activate
def test_index_not_exists(mock_es_client):
    responses.add(responses.HEAD, f'{cluster_url}/wrong_index_name', json={"error": {"root_cause": [
        {"type": "index_not_found_exception", "reason": "no such index [logz]", "resource.type": "index_or_alias",
         "resource.id": "logz", "index_uuid": "_na_", "index": "logz"}], "type": "index_not_found_exception",
        "reason": "no such index [logz]",
        "resource.type": "index_or_alias",
        "resource.id": "logz",
        "index_uuid": "_na_",
        "index": "logz"}}, status=404)

    result = index_exists(mock_es_client, "wrong_index_name")
    assert result == False


@responses.activate
def test_ttl(mock_es_client):
    responses.add(responses.POST, f'{cluster_url}/_count',
                  json={"count": 200, "_shards": {"total": 20, "successful": 20, "skipped": 0, "failed": 0}},
                  status=200)

    count_response = mock_es_client.count()
    assert count_response['count'] == 200
