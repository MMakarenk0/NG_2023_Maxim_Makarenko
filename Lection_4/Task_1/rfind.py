import os
import argparse

# Function for seaching folders and subfolders using os.walk method to recursively walk through all subfolders of a specified folder
def getFile(folder, file):
    for root, dirs, files in os.walk(args.folder):
        for file in files:
            if args.file in file: 
                print(f"File found: {os.path.join(root, file)}")

parser = argparse.ArgumentParser()

parser.add_argument('--folder', required=True, help='The folder to search in')
parser.add_argument('--file', required=True, help='The string to search in the file names')

args = parser.parse_args()

getFile(args.folder, args.file)