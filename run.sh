#!/bin/bash

# three times failures to get enough of them
HOUR_ADJUST=-2 ./load.py bob_failures.json
HOUR_ADJUST=-2 ./load.py bob_failures.json
HOUR_ADJUST=-2 ./load.py bob_failures.json

# one time success
HOUR_ADJUST=-2 ./load.py bob_success.json

# one time workflow, after everything else but still in the past
HOUR_ADJUST=-1 ./load.py saved_*.json

