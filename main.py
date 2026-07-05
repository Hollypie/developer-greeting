from datetime import datetime
import os
import sys
import platform


print("=" * 50)
print("      Holly's Raspberry Pi Developer Dashboard")
print("=" * 50)
print()

print("👋 Welcome Holly!")
print()

today = datetime.now()

print(f"📅 Date: {today.strftime('%A, %B %d, %Y')}")
print(f"🕒 Time: {today.strftime('%I:%M %p')}")
print()

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

print("📂 Files in this folder:")

for file in os.listdir():
    print(f"   {file}")

print()

print("Have a great day coding!")