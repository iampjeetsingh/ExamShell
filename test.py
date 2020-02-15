#!/usr/bin/python

import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)

import subprocess as sp
from datetime import datetime, timedelta
import threading

web = [19202 , 19134 , 19304]
mobile = [19307 , 19328 ,19320 ,19314 ,19206 ,19130 ,19213 ,19121 ,19127 , 19201 , 19331 , 19142 ]
ml = [19110, 19228, 19124, 19313, 19129, 19111, 19318, 19146, 19323, 19155, 19321, 19244, 19109, 19240, 19143, 19322, 19151, 19330, 19308]
game = [ 19120, 19128, 19141, 19237, 19101, 19214, 19126]

names = {"19202" : "Abhinav","19134" : "Pradyuman Yadav" ,"19304" : "Anoop Singh"
,"19307" : "Deekap Prajapati" , "19328" : "Shridhar Chouksey" ,"19320" : "Radhey Shyam" ,"19314" : "Kunal" , "19206" : "Aniket Kumar" , "19130" : "Nitish" , "19213" : "Ashok Yadav" , "19121" : "Kavisha Gupta",  "19127" : "Mohit Dhoundiyal" ,"19201" :"Aaradhya Kumar","19331" : "Umang Sharma" , "19142" : "Rishabh Mishra",
"19110" :"Chaitanya" , "19228" : "Mahavir Dabas" , "19124" : "Manav Babber" ,"19313" : "Kartikay Mann" , " 19129" : "Niket Agrawal" , "19111" : "Chandan Bansal" ,"19318" : "Piyush Agarwal" ,"19146" : "Shashank Mingwal " ,"19323" : "Riya Rana" , "19155" : "Vanshika Pandey" , "19321" : "Rahul Daksha" , "19244" : "Tejendra Saini" , "19109" : "Ayush Kumar Chauhan", "19240" : "Shubhi Dua" , "19143" : "Rishi Shukla " , "19322" : "Ravi Kumar Gupta", "19151" : "Siddharth Sharma" ,"19330" : "Tenzin Onge" , "19308" : "Devang Sharma ", "19329" : "Tapendra Kumar",
"19120" : "Kartik Singh", "19128" : "Naresh Kumar" , "19141" : "Rishabh Baid" ,
"19237" :"Rollin Yambem" , "19101" : "Aayushi Dangwal" , "19214" : "Siddhant Kaashikar", "19126" : "Mohd Uvaish Siddiqui"}

def current_time():
    return datetime.now()


def format_delta(delta):
    d = {}
    d["H"], rem = divmod(delta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)
    return str(d["H"]) + ":" + str(d["M"]) + ":" + str(d["S"])


def format_time(time):
    return time.strftime('%H:%M:%S')


def log(s):
    with open('log', 'a') as file:
        file.write(s + "\n")

class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = sp.Popen(self.cmd)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()      #use self.p.kill() if process needs a kill -9
            self.join()


# datetime(year, month, day, hour, minute, second, microsecond)

testStartTime = datetime(year=2020, month=2, day=8, hour=21, minute=00, second=0)
testEndTime = testStartTime + timedelta(hours=3)
print("Code Cops IIITU")
print("Welcome to Open Test 2")
inputs = ['ans', 'run', 'time', 'submit']
roll = None
name = None
coors = ['kohli','abhi', 'param','']
langs = ['java', 'cpp', 'python','c','js']
roll = int(input("Enter your roll > "))
if roll in names:
    name = names[roll]
else:
    name = input("Enter your name > ")
lang = None
if roll in web:
    lang='js'
elif roll in mobile:
    lang='java'
elif roll in game:
    lang='cpp'
elif roll in ml:
    lang='python'
else:
    lang = input("Enter your Language for test (c/cpp/java/js/python) > ")
    while lang not in langs:
        print(lang + " is not a valid language for OPT2.")
        lang = input("Enter your Language for test (c/cpp/java/python) > ")
extension = '.cpp'
if lang == 'java':
    extension = '.java'
elif lang=='python':
    extension = '.py'
elif lang=='c':
    extension = '.c'
elif lang=='js':
    extension = '.js'
start = input(name + " @ CodeCops > ")
while not (start == 'start' and current_time() > testStartTime):
    if start != 'start':
        print(start + ' is not a valid command.')
    elif current_time() < testStartTime:
        print('Test will start in ' + format_delta(testStartTime - current_time()))
    start = input(name + "@CodeCops > ")
startTime = current_time()
lateStartError = startTime - testStartTime
if start == 'start':
    sp.call('rm log', shell=True)
    sp.call('rm time', shell=True)
    log("\'" + format_time(current_time()) + "\':\'Started Test\'")
    print('Test Started, Start Coding.')
    with open('time', 'w') as tf:
        tf.write(str(startTime.hour) + "\n" + str(startTime.minute) + "\n" + str(startTime.second))
currentQuesNo = 1
while True:
    if testEndTime + lateStartError < current_time():
        print('Time Over.')
        log("\'" + format_time(current_time()) + "\':\'Forced Submit\'")
        break
    i = input(name + "@CodeCops > ")
    log("\'" + format_time(current_time()) + "\':\'" + i + "\'")
    i = i.split(' ')
    if i[0] == 'ans':
        currentQuesNo = i[1]
        sp.call('nano Test/Ques' + currentQuesNo + extension, shell=True)
    elif i[0] == 'time':
        print("Current Time : " + format_time(current_time()))
        print("Time Left : " + format_delta(testEndTime + lateStartError - current_time()))
    elif i[0] == 'battery':
        sp.call('acpi',shell=True)
    elif i[0] == 'run':
        if lang == 'java':
            sp.call('javac Test/Ques' + str(currentQuesNo) + extension, shell=True)
            RunCmd(["java", "Test.Ques"+str(currentQuesNo)], 60).Run()
        elif lang == 'cpp' or lang=='c':
            sp.call('g++ Test/Ques' + str(currentQuesNo) + extension, shell=True)
            RunCmd(["./a.out"], 60).Run()
        elif lang == 'python':
            RunCmd(["python3", "Test/Ques"+str(currentQuesNo)+extension], 60).Run()
        elif lang == 'js':
            RunCmd(["node", "Test/Ques"+str(currentQuesNo)+extension], 60).Run()
    elif i[0] == 'submit':
        with open('time', 'w') as tf:
            tf.write(format_time(startTime) + " to " + format_time(current_time()))
        break
    elif i[0] == 'clear':
        sp.call('clear', shell=True)
    else:
        print(i[0] + ' is not a valid command')
sp.call("cp log Test/", shell=True)
sp.call("cp time Test/", shell=True)
sp.call("tar -zcvf " + str(roll)+ ".tar.gz Test/", shell=True)
sp.call("mv "+str(roll)+".tar.gz ~/",shell=True)
sp.call(['sudo', 'systemctl', 'start', 'sddm.service'])
sp.call(['sudo', 'systemctl', 'start', 'kdm.service'])
sp.call(['sudo', 'systemctl', 'start', 'gdm.service'])
sp.call(['sudo', 'systemctl', 'start', 'mdm.service'])
sp.call(['sudo', 'systemctl', 'start', 'slim.service'])
sp.call(['sudo', 'systemctl', 'start', 'lxdm.service'])
sp.call(['sudo', 'systemctl', 'start', 'lightdm.service'])
sp.call("rm -rf Test log time",shell=True)
with open('test.py','w') as f:
    pass