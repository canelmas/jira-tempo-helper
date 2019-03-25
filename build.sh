#!/bin/bash

if [ $# -ne 1 ]; then
    echo 'usage : build <version e.g. 3.0.0, 1.0.0-a1>'
else
    docker build -t commencis/jira-tempo-helper:$1 .
fi