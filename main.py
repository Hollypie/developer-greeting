from datetime import datetime
import os

print("Welcome Holly!")
print()

today = datetime.now()

print("Today is:")
print(today.strftime("%A, %B %d, %Y"))
print()

print("Current directory:")
print(os.getcwd())