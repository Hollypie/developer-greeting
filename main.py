import argparse

from dashboard import print_header
from system_info import show_system_info
from file_utils import list_files

parser = argparse.ArgumentParser(description="Developer Dashboard")

parser.add_argument("--name")
parser.add_argument("--systeminfo", action="store_true")
parser.add_argument("--listfiles", action="store_true")

args = parser.parse_args()

print_header(args.name)

if args.systeminfo:
    show_system_info()

if args.listfiles:
    list_files()

print("Have a great day coding!")