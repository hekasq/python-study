import json
import random
import uuid
from datetime import datetime, timedelta

from elasticsearch import Elasticsearch
from elasticsearch import helpers as es_helper


# cluster name. Cluster must already exist and be configured
cluster_name = 'demo-telem-cluster'

index_name = 'logs'
tier = 'data_hot'
index_primary_shards = 20
index_replicas = 1

docs_to_generate = 1

regions = ["US", "EU", "KR"]
host_prefixes = ["web-server", "db-server", "api-server"]
programs = ["bgs", "fen", "test", "gry", "d4", "d4_dev"]
os_names = ["Ubuntu 20.04", "CentOS 8", "Red Hat Enterprise Linux 8", "Windows Server 2019"]
platform = ["Openstack", "GCP", "AWS", "Azure"]
entries = []


def populate_elasticsearch():
    es_client = Elasticsearch(hosts=[f'http://localhost:9200'])

    if not es_client.indices.exists(index=index_name):
        index_settings = {
            "settings": {
                "number_of_shards": index_primary_shards,
                "number_of_replicas": index_replicas,
                "index.routing.allocation.include._tier_preference": tier
            }
        }
        es_client.indices.create(index=index_name, body=index_settings)

    with open('sample_data.json', 'r') as file:
        data = json.load(file)

    actions = [
        {
            "_op_type": "index",
            "_index": index_name,
            "_source": item
        }
        for item in data
    ]
    es_helper.bulk(es_client, actions)


def generate_sample_file():
    start_time = datetime.strptime("2023-09-29T12:02:00Z", "%Y-%m-%dT%H:%M:%SZ")
    for _ in range(docs_to_generate):
        region = random.choice(regions)
        host_name = f"{random.choice(host_prefixes)}-{region.lower()}{random.randint(1, 100)}.example.com"
     #   timestamp = (start_time + timedelta(seconds=_ * 5)).strftime("%Y-%m-%dT%H:%M:%SZ")
       # timestamp = (start_time - timedelta(minutes=_ * 5)).strftime("%Y-%m-%dT%H:%M:%SZ")
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        entry = {
            "timestamp": timestamp,
            "region": region,
            "process_id": str(uuid.uuid4()),
            "host_name": host_name,
            "platform": random.choice(platform),
            "program_id": random.choice(programs),
            "OS_name": random.choice(os_names)
        }
        entries.append(entry)

    with open("sample_data.json", "w") as file:
        json.dump(entries, file, indent=4)


if __name__ == "__main__":
    generate_sample_file()
    populate_elasticsearch()