#!/bin/bash

# ensure right directory and virtualenv
base=$(dirname "$0")
source $base/env/bin/activate
cd $base

# three times failures to get enough of them
HOUR_ADJUST=-3 ./load.py bob_failures.json
HOUR_ADJUST=-3 ./load.py bob_failures.json
HOUR_ADJUST=-3 ./load.py bob_failures.json
HOUR_ADJUST=-3 ./load.py bob_failures.json
HOUR_ADJUST=-3 ./load.py bob_failures.json
HOUR_ADJUST=-3 ./load.py bob_failures.json

# one time success
HOUR_ADJUST=-2 ./load.py bob_success.json

# one time workflow, after everything else but still in the past
HOUR_ADJUST=-1 ./load.py saved_events_auditbeat.json saved_events_packetbeat.json

