#!/bin/bash

echo "This will run the application in development mode."

# Settings
export FLASK_APP=mainp.py
export FLASK_DEBUG=1

# Runtime
flask run
