import os
import json
import argparse

def get_files_in_directory(directory, skip=None):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:

			# Skip files with the specified prefix
            if skip and file.startswith(skip):
                continue

            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def main():
    parser = argparse.ArgumentParser(description='List files in a directory.')
    parser.add_argument('directory', help='Directory path to scan')
    parser.add_argument('--skip', help='Skip files with the specified prefix')

    args = parser.parse_args()

    directory_to_scan = args.directory
    if not os.path.isdir(directory_to_scan):
        print(f"Error: {directory_to_scan} is not a valid directory.")
        sys.exit(1)

    files = get_files_in_directory(directory_to_scan, args.skip)

    # Convert the list of files to a JSON array
    json_array = json.dumps(files, indent=2)

    # Save the JSON array to a file
    output_file_path = "files_list.json"
    with open(output_file_path, "w") as json_file:
        json_file.write(json_array)

    print(f"File list saved to {output_file_path}")

if __name__ == "__main__":
    main()
