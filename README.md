# SIEM investigation demo

Scripts that load a few events into Elasticsearch, to simulate an investigation scenario.

*load.py* - reads a JSON file (in the format of an ES query response) and indexes it
while replacing the timestamp to current day.

*run.sh* - runs load.py multiple times with various parameters to create the scenario. It
is designed to be put in CRON and executed daily.
