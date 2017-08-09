#! /usr/bin/env python
# -*- coding：utf-8 -*-
# Author : Yuan
import time

# user,pwd = 'yuan','5771500'
#
#
# def yanzhengdengluzhuangshi(denglufangshi):
#     print("现在的登录方式是：",denglufangshi)
#     def yanzhengzhuangshi(func):
#         def yanzheng(*args,**kwargs):
#             username = input("请输入用户名：").strip()
#             password = input("请输入密码：").strip()
#
#             if username == user and password ==pwd:
#                 print("欢迎您登录！！")
#                 res =func(*args,**kwargs)
#                 print("有返回值！")
#                 return  res
#             else:
#                 exit("输入错误，再见！")
#         return  yanzheng
#     return yanzhengzhuangshi
#
# @yanzhengdengluzhuangshi(denglufangshi = "远程")
# def index():
#     print("welcome to index page")
#
# @yanzhengdengluzhuangshi(denglufangshi = "本地")
# def  home():
#     print("welcome to home page")
#
#     return "欢迎登录主页面"
#
#
# @yanzhengdengluzhuangshi(denglufangshi = "本地")
# def  bbs():
#     print("welcome to bbs page")
#
# # index()
# print(home())


# 示例7: 在示例4的基础上，让装饰器带参数，
# 和上一示例相比在外层多了一层包装。
# 装饰函数名实际上应更有意义些


def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print(" myfunc() called.")

@deco("module2")
def myfunc2():
    print(" myfunc2() called.")

myfunc()
myfunc2()