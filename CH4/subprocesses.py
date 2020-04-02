#!/usr/local/bin/python

import subprocess
import datetime as dt
import sys
import chardet

class SP():
    def execute(self, command, args = ""):
        try:
            p = subprocess.Popen(command +" "+ args, shell = True, stderr = subprocess.PIPE, stdout = subprocess.PIPE)       # shell = True should never be used in the real world since it makes the application vulnerable to shell injection
            # p = subprocess.Popen(command + " " + args, shell=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE). If we make shell False, we must pass the commands separately as a list - line 27
            print(f"The ID of the spawned process is: {p.pid}" + "\n")
            out, err = p.communicate()
            result = chardet.detect(out)
            out = str(out).encode('ascii')
            out = out.decode('utf-8')
            splitted = str(out).split("\\n")
            for o in splitted:
                print(o)
        except Exception as ex:
            print(f"Exception caught: {ex}")

obj = SP()
obj.execute("ls")

#obj.execute(["ls", "-l"])