from os import getcwd
import os
import sys

curpath=getcwd()
sys.path.append(curpath)

print(sys.path)
