#!/usr/bin/env python3

print("Reading from a file")
with open("example.txt", "r") as f:
    txt = f.read()
    print(txt)
    if "dog" in txt:
        print("YEP!")


errors = []
with open("loggy.log", "r") as logfile:
    log_txt = logfile.readlines()
    for logline in log_txt:
        print(logline.strip())
        if "Error" in logline:
            errors.append(logline)



