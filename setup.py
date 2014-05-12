#!virtualenv/bin/python
import os
import subprocess as sub
import sys


#sub.call(['python', 'virtualenv.py', 'virtualenv'])
if sys.platform == 'win32':
    bin = 'Scripts'
else:
    bin = 'bin'

pip = os.path.join('virtualenv', bin, 'pip')

sub.call([pip, 'install', 'flask==0.10.1'])