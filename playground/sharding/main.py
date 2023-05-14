#!/usr/bin/env
import os
from multiprocessing import  Process

def startMaster1():
    os.system("redis-server redis_master_1/default.conf")
def startMaster2():
    os.system("redis-server redis_master_2/default.conf")
def startMaster3():
    os.system("redis-server redis_master_3/default.conf")

m1=Process(target=startMaster1)
m1.start()
m2=Process(target=startMaster2)
m2.start()
m3=Process(target=startMaster3)
m3.start()

m1.join()
m2.join()
m3.join()
