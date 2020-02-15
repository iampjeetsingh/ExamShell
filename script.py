#!/usr/bin/python

import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)
import subprocess as sp
print("Welcome Code Cops Shell")
langs = ['java', 'cpp', 'python','c','js']
lang = input("Enter your Language for test (c/cpp/java/js/python) > ")
while lang not in langs:
    print(lang + " is not a valid language for OPT2.")
    lang = input("Enter your Language for test (c/cpp/java/js/python) > ")
sp.call('cd ~', shell=True)
sp.call('wget http://codecopsiiitu.c1.biz/'+lang+'.txt', shell=True)
sp.call('mv test.txt OPT2/test.py', shell=True)
sp.call('mv '+lang+'.txt ques.zip', shell=True)
sp.call('unzip ques.zip -d OPT2/Test/', shell=True)
sp.call('rm ques.zip',shell=True)
sp.call(['sudo', 'apt', 'update'])
sp.call(['sudo', 'apt', 'install', 'nano'])
sp.call(['sudo', 'apt', 'install', 'curl'])
sp.call(['sudo', 'apt', 'install', 'acpi'])
if lang == 'cpp' or lang=='c':
    sp.call(['sudo', 'apt', 'install', 'build-essential'])
elif lang == 'java':
    sp.call(['sudo', 'apt', 'install', 'default-jdk'])
    sp.call(['sudo', 'apt', 'install', 'openjdk-11-jdk'])
elif lang == 'js':
    sp.call('sudo apt install npm')
    sp.call('npm install readline-sync', shell=True)
sp.call(['sudo', 'systemctl', 'stop', 'sddm.service'])
sp.call(['sudo', 'systemctl', 'stop', 'kdm.service'])
sp.call(['sudo', 'systemctl', 'stop', 'gdm.service'])
sp.call(['sudo', 'systemctl', 'stop', 'mdm.service'])
sp.call(['sudo', 'systemctl', 'stop', 'slim.service'])
sp.call(['sudo', 'systemctl', 'stop', 'lxdm.service'])
sp.call(['sudo', 'systemctl', 'stop', 'lightdm.service'])