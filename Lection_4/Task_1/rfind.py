import os
import argparse
from colorama import *

init(autoreset=True)
# Function for seaching folders and subfolders using os.walk method to recursively walk through all subfolders of a specified folder

def getFile(path: str, searchFile: str):
    for fileName in os.listdir(path):
        if os.path.isdir(os.path.join(path, fileName)):
            try:
                getFile(os.path.join(path, fileName), searchFile)
            except PermissionError:
                print(f"{Fore.RED}ACCESS DENIED! {os.path.join(path, fileName)}")
        elif searchFile in fileName:
            print(f"{Fore.GREEN}{Style.BRIGHT}FILE FOUND: {os.path.join(path, fileName)}")

parser = argparse.ArgumentParser()

parser.add_argument('--folder', required=True, help='The folder to search in')
parser.add_argument('--file', required=True, help='The string to search in the file names')

args = parser.parse_args()

getFile(args.folder, args.file)