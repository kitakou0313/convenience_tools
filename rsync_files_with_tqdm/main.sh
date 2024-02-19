#!/bin/bash

source_path="$1"
shift
min_iter_num="$1"
shift
log_file_name="$1"
shift
format_file="$1"
shift
dest_paths="$@"

docker compose -f "${format_file}" run -d --rm rsync bash -c "python -u main.py ${source_path} ${min_iter_num} log_${log_file_name}.txt ${dest_paths[@]}"