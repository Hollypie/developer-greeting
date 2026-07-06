#!/usr/bin/env python3

import argparse

from dashboard import print_header
from system_info import show_system_info
from file_utils import list_files
from git_utils import show_git_status
from disk_utils import show_disk_info
from memory_utils import check_ram

parser = argparse.ArgumentParser(description="Developer Dashboard")

parser.add_argument("command", choices=["systeminfo", "listfiles", "git", "memory", "disk", "all"])
parser.add_argument("--name")
parser.add_argument("--folder")

args = parser.parse_args()

print_header(args.name)

if args.command == "systeminfo":
    show_system_info()

elif args.command == "listfiles":
    list_files()
    
elif args.command == "git":
    show_git_status()
    
elif args.command == "memory":
    check_ram()
    
elif args.command == "disk":
    show_disk_info(args.folder)

elif args.command == "all":
    show_system_info()
    list_files()
    show_git_status()
    check_ram()
    show_disk_info(args.folder)
    
print("Have a great day coding!")