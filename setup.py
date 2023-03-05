import os
import sys

if __name__ == "__main__":
    with open("regular-git.bat", "w") as batch_file:
        batch_file.write(f"python {os.getcwd()}\\regular-git.py %1")
    print("Created regular-git batch script")
    os.environ['PATH'] += os.pathsep + os.getcwd()
    print("Added script to path", "Restarting Terminal", sep="\n")
    print("Usage:\n- regular-git <path-to-repo>")
    os.system("pause")
    os.system("start")
    os.system("exit")
    sys.exit(1)
