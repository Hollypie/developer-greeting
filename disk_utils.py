import shutil
import os

def show_disk_info(folder=None):
    print("💾 Performance for this directory:")
    
    if folder is None:
        folder = os.getcwd()
    
    stats = shutil.disk_usage(folder)
    
    print(f"Total space: {stats.total / (1024**3):.2f} GB")
    print(f"Used space:  {stats.used / (1024**3):.2f} GB")
    print(f"Free space:  {stats.free / (1024**3):.2f} GB")

    print()