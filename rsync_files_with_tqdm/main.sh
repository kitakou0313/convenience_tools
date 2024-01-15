#!/bin/bash

source_path="$1"
shift
dest_paths="$@"

docker compose run -d --rm rsync bash -c "python main.py $source_path ${dest_paths[@]} &> log.txt"