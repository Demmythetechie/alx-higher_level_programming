#!/bin/bash
# This script send a request and displays the status code
curl -s -w "%{http_code}" -o /dev/null $1
