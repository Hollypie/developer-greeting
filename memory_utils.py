import psutil

def check_ram():
    
    print("🧠 Memory Usage")
    # Gather virtual memory statistics
    ram = psutil.virtual_memory()
    
    # Convert bytes to Megabytes (GB)
    total_mb = ram.total / (1024 ** 3)
    available_mb = ram.available / (1024 ** 3)
    used_mb = ram.used / (1024 ** 3)
    
    print(f"Total RAM:     {total_mb:.0f} GB")
    print(f"Available RAM: {available_mb:.0f} GB")
    print(f"Used RAM:      {used_mb:.0f} GB ({ram.percent}%)")
    print()