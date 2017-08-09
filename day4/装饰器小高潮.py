#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

# import time
#
# def test1():
#     time.sleep(3)
#
#     print("in the test1")
#
#
# def test2():
#     time.sleep(3)
#
#     print("in the test2")
#
#
# def deco(func):
#     start_time =time.time()
#     func()
#     stop_time = time.time()
#
#     print("程序运行时间：%s" %(stop_time-start_time))
#     return  func
# test1 = deco(test1)
#
# test1()

import  time



def zhuangshiqi(func):
    def test_new(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("程序运行时间：%s"%(stop_time-start_time))
    return  test_new


@zhuangshiqi
def test1(name,age):

    time.sleep(1)
    print('in the test1')
    print(name , age)

test1("yuan",23)