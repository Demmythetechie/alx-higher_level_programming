#!/bin/bash
#This script sends a post request to the url
curl -s -X POST -d "email=test@gmail.com" $1
