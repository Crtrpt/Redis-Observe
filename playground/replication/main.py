#!/usr/bin/env
import os
from multiprocessing import  Process
import redis

def startMaster():
    os.system("redis-server redis_master/default.conf")
def startSlave():
    os.system("redis-server redis_slave/default.conf")

m=Process(target=startMaster)
m.start()
s=Process(target=startSlave)
s.start()
m.join()
s.join()
