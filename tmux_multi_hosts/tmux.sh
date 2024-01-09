#!/bin/bash
set -e

source ./hosts/hosts

# 全hostへのSSH
tmux new-session -s "monitor-hosts" -d ssh -p ${ALL_HOSTS_SSH_PORT[0]} -i ${ALL_HOSTS_SSH_PRIVATE_KEY[0]} ${ALL_HOSTS_SSH_USER[0]}@${ALL_HOSTS[0]} &&\
for ((host_idx=1; host_idx<${ALL_HOSTS_NUMS}; host_idx++));
do
  tmux split-window
  tmux send-keys "ssh -p ${ALL_HOSTS_SSH_PORT[host_idx]} -i ${ALL_HOSTS_SSH_PRIVATE_KEY[host_idx]} ${ALL_HOSTS_SSH_USER[host_idx]}@${ALL_HOSTS[host_idx]}" C-m
done
tmux select-layout even-vertical

tmux ls