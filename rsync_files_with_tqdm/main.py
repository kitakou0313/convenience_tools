import os
import subprocess
import argparse
from tqdm import tqdm

def rsync_copy(source, destination):
    command = ["rsync", "-a", source, destination]
    subprocess.run(command, check=True)

def copy_files_recursive(source_dir, destination_dir):
    # Ensure source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Walk through the source directory and copy files
    for root, _, files in os.walk(source_dir):
        for file in tqdm(files, desc="Copying files", unit="file"):
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_dir)
            destination_path = os.path.join(destination_dir, relative_path)

            # Ensure the destination directory exists
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            # Copy the file using rsync
            rsync_copy(source_path, destination_path)

def main():
    parser = argparse.ArgumentParser(description="Recursive rsync file copy with progress")
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("destination", help="Destination directory path")
    args = parser.parse_args()

    copy_files_recursive(args.source, args.destination)

if __name__ == "__main__":
    main()
