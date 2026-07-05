import os

def list_files():
    print("📂 Files in this folder:")

    for file in os.listdir():
        print(f"   {file}")

    print()