#! /usr/bin/env python
# -*- coding：utf-8 -*-
# Author : Yuan

shangpin_list = [['Iphone' ,5800],['Bike' ,1300],['BOOK',80],['Car' , 20000],['Mouse' , 100],['Tplink',300]]


while True:
    shouru = input("请输入您的收入：")
    if shouru.isdigit():
        shouru = int(shouru)
        gouwuche = []
        while True:
            for index , item  in  enumerate(shangpin_list):
                print(index,item)
            xuanze = input("请您输入你要购买的商品序号:")
            if xuanze.isdigit() and int(xuanze)<len(shangpin_list) and int(xuanze)>=0:
                if shangpin_list[int(xuanze)][1]<=shouru:
                    gouwuche.append(shangpin_list[int(xuanze)])
                    shouru =  shouru -  shangpin_list[int(xuanze)][1]
                    print("您购买了  %s   商品 ， 您现在的余额是 %s"%(shangpin_list[int(xuanze)][0],shouru))
                else:
                    print("您的余额不足购买该商品，请重新选择！")
            elif  xuanze == "q" or xuanze =="Q":
                for index,item in enumerate(gouwuche):
                    print(index,item)
                print("您消费后的余额是 %s " %shouru )
                exit()
            else:
                print("您输入的有误，请重新输入！")





    else:
        print("您的输入有误请重新输入！")
