#!/usr/bin/env python3

import argparse

from dashboard import print_header
from system_info import show_system_info
from file_utils import list_files
from git_utils import show_git_status

parser = argparse.ArgumentParser(description="Developer Dashboard")

parser.add_argument("command", choices=["systeminfo", "listfiles", "git", "all"])
parser.add_argument("--name")

args = parser.parse_args()

print_header(args.name)

if args.name:
    print(f"👋 Welcome {args.name}!")
else:
    print("👋 Welcome Developer!")

if args.command == "systeminfo":
    show_system_info()

elif args.command == "listfiles":
    list_files()
    
elif args.command == "git":
    show_git_status()

elif args.command == "all":
    show_system_info()
    list_files()
    show_git_status()
    
print("Have a great day coding!")