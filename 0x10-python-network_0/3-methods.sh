#!/bin/bash
#This script takes in a URL and displays HTTP methods the server accepts
curl -i -L -X OPTIONS $1
