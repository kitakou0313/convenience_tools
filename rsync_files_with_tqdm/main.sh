#!/bin/bash

docker compose run -d --rm rsync bash -c "python main.py test test_dist test_dist2 &> log.txt"