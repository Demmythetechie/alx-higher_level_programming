#!/usr/bin/env bash
# This gets a website
curl -sI $1 | grep "^Content-Length" | cut -f 2 -d ' '
