#!/bin/bash
set -e
docker-compose -f  /opt/dr-analytics-superset/docker-compose-custom.yml down
sleep 20
docker-compose -f  /opt/dr-analytics-superset/docker-compose-custom.yml up -d
set +e
