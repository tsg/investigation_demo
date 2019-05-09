#!/usr/bin/env python

import json
import sys
import os
from datetime import datetime
from elasticsearch import Elasticsearch
import ssl
from elasticsearch.connection import create_ssl_context
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_file(es, input_file):
    now = datetime.utcnow()
    js = json.load(input_file)
    for hit in js["hits"]["hits"]:
        source = hit["_source"]
        ts = datetime.strptime(source["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        add_hour = 0
        if os.environ.has_key("HOUR_ADJUST"):
            add_hour = int(os.environ["HOUR_ADJUST"])
        ts = ts.replace(year=now.year, month=now.month, day=now.day, hour=now.hour+add_hour)
        source["@timestamp"] = ts.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        print source["@timestamp"]

        try:
            agent_type = source["agent"]["type"]
        except:
            agent_type = "filebeat"

        try:
            agent_version = source["agent"]["version"]
        except:
            agent_version = "8.0.0"

        # the following relies on the ILM alias existing
        index_name = "{}-{}".format(agent_type, agent_version)

        es.index(index=index_name, body=source)



ssl_context = create_ssl_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
es = Elasticsearch([os.environ["ELASTICSEARCH_URL"]], ssl_context=ssl_context, ssl_show_warn=False)

for arg in sys.argv[1:]:
    with open(arg, "r") as f:
        load_file(es, f)
