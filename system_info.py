import os
import sys
import platform

def show_system_info():
    print("💻 Current Directory:")
    print(os.getcwd())
    print()

    print("🐍 Python Version:")
    print(sys.version)
    print()

    print("💾 Operating System:")
    print(platform.system())
    print()

    print("🖥️ Computer Name:")
    print(platform.node())
    print()