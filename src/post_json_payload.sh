#!/bin/bash

curl -X POST http://127.0.0.1:8000/v1/customers/ \
    -H "Content-Type: application/json" \
    -d @data/payload.json
