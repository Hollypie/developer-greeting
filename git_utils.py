import subprocess

def show_git_status():

    print("📂 Git Repository")
    print()

    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print()