#!/bin/bash

echo "This will run the application in development mode."

# Settings
export FLASK_APP=main.py
export FLASK_DEBUG=1

# Runtime
flask run
