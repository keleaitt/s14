#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import time

def test1():
    time.sleep(3)

    print("in the test1")


def test2():
    time.sleep(3)

    print("in the test2")


def deco(func):
    start_time =time.time()
    func()
    stop_time = time.time()

    print("程序运行时间：%s" %(stop_time-start_time))
    return  func
test1 = deco(test1)

test1()