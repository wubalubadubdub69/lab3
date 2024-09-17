# -*- coding: utf-8 -*-
"""
Created 6 days after September 11th

@author: SaltyBedouin
"""

import time
import math
l = (time.ctime(time.time() + 86400))
print(" ".join(l.split()[:3]))
print("hellow")
StillInputting = True
tasks = []
taskno = 1
print("Hi, this is the schedueler: enter the tasks you want to scheduel; if you finished inputting tasks, input -1 \n")
path1 = int(input("Do you want to distribute tasks on given number of days? (input 1) OR Do you want to know how many days required to finish tasks based on workload intensity? (input 0) \nInput Here:"))

while(StillInputting):
    inputT = input(f"Enter Task {taskno}:")
    try:
        
        if(int(inputT) == -1):
            StillInputting = False
            break
    except:
            print("")
        
    tasks.append((inputT.split())[0])
    taskno +=1
print("Tasks Saved Successfully!")
print(tasks)

if(path1):
    daysno = int(input("How many days do you plan to finish these tasks within?\nEnter Number:"))
    workload = len(tasks)/daysno
    dayi = 0
    dayslist = []
    if(True):
        daysneeded = workload**(-1)
        for i in range(len(tasks)):
            date = (time.ctime(time.time() + 86400*dayi))
            dayslist.append((" ".join(date.split()[:3])))
            dayi = dayi + daysneeded
        print(f"Every {int(daysneeded)} start in a new project starting with")
        for i in range(len(tasks)):
            
            print(f"on day {dayslist[i]} start working on task {tasks[i]}")
else:
    workload = int(input("How many tasks do you plan to do per day?\n Enter Number:"))
   
    date = (time.ctime(time.time() + 86400*(len(tasks)/workload)))
    datei = (" ".join(date.split()[:3]))
    print(f" You will finish after {math.ceil(len(tasks)/workload)} days on {datei}")
    
            
            
        
    
    