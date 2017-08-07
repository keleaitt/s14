#! /usr/bin/env python
# -*- coding：utf-8 -*-
# Author : Yuan



# def bar():
#     print("in the bar")

# def foo():
#     print("in the foo")
#     bar()
# def bar():
#     print("in the bar")
# foo()
#
# def test1(func):
#     print(func)
#
# def bar():
#     print("in the bar")
#
#
# test1(bar)
# import time
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
#
# def test1(func):
#     kaishi_time = time.time()
#     func()
#     jieshu_time = time.time()
#
#     print("运行时间是：%s" %(jieshu_time-kaishi_time))
#
# test1(bar)

import  time

def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):
    kashi_time=time.time()
    print(func)
    print("我套了一层")
    jieshu_time = time.time()

    return func

bar = test1(bar)

bar()