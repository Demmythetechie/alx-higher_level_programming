#!/bin/bash
# This script post to the url
curl -s -X POST -d "@$2" -H "Content-Type: application/json" $1
