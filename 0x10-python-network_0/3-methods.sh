#!/bin/bash
#This script takes in a URL and displays HTTP methods the server accepts
curl -s -I -X OPTIONS $1
