#!/usr/bin/env python3
import subprocess, sys

fname = "words.txt"
with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
    for i,line in enumerate(f,1):
        pwd = line.rstrip('\n')
        if pwd == "": 
            continue
        res = subprocess.run(['./crackme2', pwd], capture_output=True, text=True)
        out = (res.stdout or "") + (res.stderr or "")
        if i % 100 == 0:
            print(f"Tried {i} candidates... last: {pwd}")
        if "Access denied." not in out:
            print("\nFOUND:", pwd)
            print("PROGRAM OUTPUT:\n", out)
            sys.exit(0)
print("Done — no candidate succeeded.")

