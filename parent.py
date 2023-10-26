#!/usr/bin/python3

import sys
import os
import random


def start_child():
    child_pid = os.fork()

    if child_pid == 0:
        s = random.randint(5, 10)
        os.execl("./child.py", "./child.py", str(s))
    elif child_pid < 0:
        print("Error when starting child process")
        os._exit(3)
    else:
        print(f"Parent[{pid}]: I ran children process with PID {child_pid}.")


if len(sys.argv) != 2:
    print("Need one argument: N (amount of child processes)")
    os._exit(1)

if not sys.argv[1].isdigit():
    print("Argument N (amount of child processes) must be a positive integer")
    os._exit(2)

N = int(sys.argv[1])
pid = os.getpid()

for i in range(N):
    start_child()

count = 0
while count < N:
    child_pid, status = os.wait()
    status = os.waitstatus_to_exitcode(status)
    print(f"Parent[{pid}]: Child with PID {child_pid} terminated. Exit Status {status}.")

    if status == 0:
        count += 1
    else:
        start_child()
