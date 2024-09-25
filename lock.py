import os
import sys
import subprocess

locks = [
    dict(
        location="Lecture 1",
        files=[
            "Exercises.pdf",
            "Exercises.pptx"
        ],
        password=os.environ.get("LECTURE1_PASSWORD")
    ),
    dict(
        location="Lecture 2",
        files=[
            "ex1.ipynb",
            "ex2.ipynb"
        ],
        password=os.environ.get("LECTURE2_PASSWORD")
    ),
    dict(
        location="Lecture 3",
        files=[
            "ex0.ipynb",
            "ex1.ipynb",
            "ex2.ipynb",
        ],
        password=os.environ.get("LECTURE3_PASSWORD")
    ),
    dict(
        location="Lecture 4",
        files=[
            "ex1.ipynb",
            "ex2.ipynb"
        ],
        password=os.environ.get("LECTURE4_PASSWORD")
    ),
    dict(
        location="Lecture 5",
        files=[
            "ex1.ipynb",
            "ex2_logvar.ipynb",
            "ex2.ipynb",
        ],
        password=os.environ.get("LECTURE5_PASSWORD")
    ),
    dict(
        location="Lecture 6",
        files=[
            "ex1.ipynb",
            "ex2.ipynb"
        ],
        password=os.environ.get("LECTURE6_PASSWORD")
    ),
    dict(
        location="Lecture 7",
        files=[
            "ex1.ipynb",
            "ex2-trad.ipynb",
            "ex2-vae.ipynb",
        ],
        password=os.environ.get("LECTURE7_PASSWORD")
    ),
    dict(
        location="Lecture 8",
        files=[
            "ex1.ipynb",
            "ex2.ipynb",
            "ex3.ipynb",
        ],
        password=os.environ.get("LECTURE8_PASSWORD")
    ),
    dict(
        location="Recap 1",
        files=[
            "ex1.ipynb",
            "ex2.ipynb",
            "ex3.ipynb",
        ],
        password=os.environ.get("RECAP1_PASSWORD")
    )
]

def red(s):
    print(f"\033[91m{s}\033[0m")

def green(s):
    print(f"\033[92m{s}\033[0m")

def list_files():
    for lock in locks:
        location = lock['location']
        lock_zip = os.path.join(location, 'lock.zip')
        if os.path.exists(lock_zip):
            red(f"🔒 {location}")
        else:
            green(f"🔓 {location}")

def check_files():
    all_exist = True
    for lock in locks:
        location = lock['location']
        files = lock['files']
        for file in files:
            file_path = os.path.join(location, file)
            if not os.path.exists(file_path):
                red(f"File missing: {file_path}")
                all_exist = False
    if all_exist:
        green("All files exist.")
    else:
        red("Some files are missing.")

def generate_gitignore():
    for lock in locks:
        location = lock['location']
        files = lock['files']
        for file in files:
            file_path = os.path.join(location, file)
            print(file_path)

def unlock_location(location):
    lock = None
    for l in locks:
        if l['location'] == location:
            lock = l
            break
    
    if not lock:
        red(f"Location '{location}' not found.")
        sys.exit(1)

    if not os.path.exists(location):
        red(f"Location '{location}' does not exist.")
        sys.exit(1)
    
    lock_zip = os.path.join(location, 'lock.zip')
    if not os.path.exists(lock_zip):
        red(f"Encrypted file '{lock_zip}' not found.")
        sys.exit(1)

    password = input("Password: ")
    try:
        subprocess.run(['unzip', '-P', password, 'lock.zip'], cwd=location, check=True)
        green(f"Unlocked {location}")
    except subprocess.CalledProcessError as e:
        red(f"Failed to unlock {location}: {e}")

def lock_files():
    for lock in locks:
        location = lock['location']
        files = lock['files']
        password = lock['password']
        if not password:
            raise ValueError(f"Password for location '{location}' is empty.")
        try:
            lock_zip = os.path.join(location, 'lock.zip')

            if os.path.exists(lock_zip):
                os.remove(lock_zip)
            cmd = ['zip', '-r', '--password', password, 'lock.zip'] + files
            subprocess.run(cmd, cwd=location, check=True)

            green(f"Locked {location}")
        except subprocess.CalledProcessError as e:
            red(f"Failed to lock {location}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <command> [arguments]")
        sys.exit(1)
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command == 'list':
        list_files()
    elif command == 'check':
        check_files()
    elif command == 'gitignore':
        generate_gitignore()
    elif command == 'unlock':
        if len(args) < 1:
            print("Usage: script.py unlock <location>")
            sys.exit(1)
        location = ' '.join(args)
        unlock_location(location)
    elif command == 'lock':
        lock_files()
    else:
        red(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
