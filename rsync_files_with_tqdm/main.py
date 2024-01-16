import os
import subprocess
import argparse
from tqdm import tqdm

def rsync_copy(source, destination):
    command = ["rsync", "-a", source, destination]
    subprocess.run(command, check=True)

def copy_files(source, destinations:list):
    all_items = []
    for root, dirs, files in os.walk(source):
        for item in dirs + files:
            item_path = os.path.join(root, item)
            relative_path = os.path.relpath(item_path, source)
            all_items.append((item_path, relative_path))

    for source_path, relative_path in all_items:
        for destination in destinations:
            print("{} is copied to {}".format(source_path, os.path.join(destination, relative_path)))

    miniters = len(all_items) // 10000
    # Use tqdm to display a progress bar for each file and each destination
    for source_path, relative_path in tqdm(all_items, desc="Copying files", unit="item", miniters=miniters):
        for destination in destinations:
            dest_path = os.path.join(destination, relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            rsync_copy(source_path, dest_path)

def main():
    parser = argparse.ArgumentParser(description="Copy files and directories with progress bar using rsync to multiple destinations")
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("destinations", nargs="+", help="List of destination directory paths")
    args = parser.parse_args()

    print(args)

    copy_files(args.source, args.destinations)

if __name__ == "__main__":
    main()
