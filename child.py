import sys
import os
import random
import time

if len(sys.argv) != 2:
    print("Need one argument: S (time to sleep, seconds)")
    os._exit(1)

if not sys.argv[1].isdigit():
    print("Argument S (time to sleep, seconds) must be a positive integer")
    os._exit(2)

pid = os.getpid()
ppid = os.getppid()

print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.")

time.sleep(float(sys.argv[1]))

print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.")
os._exit(random.randint(0, 1))
