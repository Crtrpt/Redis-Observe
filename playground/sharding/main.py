#!/usr/bin/env
import os
from multiprocessing import  Process

def startMaster1():
    os.system("redis-server redis_master_1/default.conf")
def startMaster2():
    os.system("redis-server redis_master_2/default.conf")
def startMaster3():
    os.system("redis-server redis_master_3/default.conf")

def startSlave1():
    os.system("redis-server redis_slave_1/default.conf")
def startSlave2():
    os.system("redis-server redis_slave_2/default.conf")
def startSlave3():
    os.system("redis-server redis_slave_3/default.conf")    

def main():
    m1=Process(target=startMaster1)
    m2=Process(target=startMaster2)
    m3=Process(target=startMaster3)
    s1=Process(target=startSlave1)
    s2=Process(target=startSlave2)
    s3=Process(target=startSlave3)
   
    m1.start()
    m2.start()
    m3.start()
    s1.start()
    s2.start()
    s3.start()
    m1.join()
    m2.join()
    m3.join()
    s1.join()
    s2.join()
    s3.join()


if __name__ == '__main__':
        main()

