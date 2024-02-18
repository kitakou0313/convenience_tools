#!/bin/bash

source_path="$1"
shift
min_iter_num="$1"
shift
log_file_name="$1"
shift
dest_paths="$@"

docker compose run -d --rm rsync bash -c "python main.py ${source_path} ${min_iter_num} ${dest_paths[@]} &> log_${log_file_name}.txt"