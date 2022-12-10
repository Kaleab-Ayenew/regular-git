import os
import time
import sys

sleep_time = 60 * 1




def git_all(comment, repo_path):
    
    cmd_add = "git add ."
    cmd_commit = f"git commit -m \"{comment}\""
    print("This is the git cmd", cmd_commit)
    cmd_push = "git push -u origin main"
    final_cmd = f"cd {repo_path} && {cmd_add} && {cmd_push} && {cmd_commit}"
    os.system(final_cmd)

def write_log(text):
    try:
        with open(f"{PATH}/regular-git-log", "r") as log_file:
            n = log_file.readline().strip('\n')
            n = int(n)
            log_file.close()
    except FileNotFoundError:
        with open(f"{PATH}/regular-git-log", "w") as log_file:
            log_file.write("1\n")
            n = 1
            log_file.close()

    with open(f"{PATH}/regular-git-log", "a+") as log_file:
        content = "\n"+text+str(n)
        print("this is content", content)
        log_file.write(content)
        log_file.close()

    with open(f"{PATH}/regular-git-log", "r+") as log_file:
        n = n + 1
        print(n)
        log_file.write(str(n)+"\n")
        log_file.close()
    print(content)
    return content

def git_deamon(sleep_time):

    while True:

        comment = write_log("regular commit")
        comment = comment.strip("\n")
        git_all(comment, PATH)
        time.sleep(sleep_time)

def git_n(m):

    for i in range(m):
        comment = write_log("regular commit")
        comment = comment.strip("\n")
        git_all(comment, PATH)

def git_one():
    comment = write_log("regular commit")
    comment = comment.strip("\n")
    git_all(comment, PATH)

try:
    PATH = sys.argv[1] #You should enter the path to the repo here
    git_deamon(sleep_time)
except IndexError:
    print("Please provide the path to your repo")
    time.sleep(5)
    exit()    

