#!/bin/bash

if [ $# -ne 2 ]; then
    echo 'usage : start <version> <env file>'
else
    docker run -d --restart always --env-file $2 --name jira-tempo-helper -p 5001:80 commencis/jira-tempo-helper:$1
fi



