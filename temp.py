# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import os
import time

jian=random.randint(1,10)
pu=random.randint(1,100)
nan=random.randint(1,1000)

print ("选择难度\n1-简单,2-普通,3-困难")
x=int(input("x\n"))

if x==1:
    print (jian)
    print("输入你猜的数(1-10)\n输入“0”结束")
    while True:
        b=int(input())
        if b==0:
            print("结束")
            break
        if b<jian:
            print("小了")
        if b>jian:
            print("大了")
        if b==jian:
            print("yep\n5秒后结束")
            time.sleep(5)
            break
            
if x==2:
    print (pu)
    print("输入你猜的数(1-100)\n输入“0”结束")
    while True:
        b=int(input())
        if b==0:
            print("结束")
            break
        if b<pu:
            print("小了")
        if b>pu:
            print("大了")
        if b==pu:
            print("yep\n5秒后结束")
            time.sleep(5)
            break

if x==3:
    print ("nan\n")
    print("输入你猜的数(1-100)\n输入“0”结束")
    while True:
        b=int(input())
        if b==0:
            print("结束")
            break
        if b<nan:
            print("小了")
        if b>nan:
            print("大了")
        if b==nan:
            print("yep\n5秒后结束")
            time.sleep(5)
            break




