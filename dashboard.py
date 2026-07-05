from datetime import datetime

def print_header(name):
    print("=" * 50)
    print("      Holly's Raspberry Pi Developer Dashboard")
    print("=" * 50)
    print()

    if name:
        print(f"👋 Welcome {name}!")
    else:
        print("👋 Welcome Developer!")

    print()

    today = datetime.now()
    print(f"📅 Date: {today.strftime('%A, %B %d, %Y')}")
    print(f"🕒 Time: {today.strftime('%I:%M %p')}")
    print()