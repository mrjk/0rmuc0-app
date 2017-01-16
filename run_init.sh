#!/bin/bash

echo "This will initialise the application sqllite3 db."

# Settings
export FLASK_APP=main.py
export FLASK_DEBUG=1

# Runtime
flask initdb
