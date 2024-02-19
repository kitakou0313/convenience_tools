import os
import subprocess
import argparse
from tqdm import tqdm
import sys

def rsync_copy(source, destination):
    command = ["rsync", "-lptD", source, destination]
    subprocess.run(command, check=True)

def copy_files(source, destinations:list, min_iter_num):
    all_items = []
    for root, dirs, files in os.walk(source):
        for item in dirs + files:
            item_path = os.path.join(root, item)
            relative_path = os.path.relpath(item_path, source)
            all_items.append((item_path, relative_path))

    
    print("{} files in {} is copied to {}".format(len(all_items), source, destinations))

    # Use tqdm to display a progress bar for each file and each destination
    for source_path, relative_path in tqdm(all_items, desc="Copying files", unit="item", miniters=min_iter_num):
        for destination in destinations:
            dest_path = os.path.join(destination, relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            rsync_copy(source_path, dest_path)

def main():
    parser = argparse.ArgumentParser(description="Copy files and directories with progress bar using rsync to multiple destinations")
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("min_iter_num", type=int, help="min iter num")
    parser.add_argument("log_file", type=str, help="log file")
    parser.add_argument("destinations", nargs="+", help="List of destination directory paths")
    args = parser.parse_args()

    log_file = open(args.log_file, 'w')

    sys.stdout = log_file 
    sys.stderr = log_file

    print(args)

    copy_files(args.source, args.destinations, args.min_iter_num)

if __name__ == "__main__":
    main()
