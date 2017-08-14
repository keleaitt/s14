

def chibaozi(name):

    print("%s 准备吃包子了！" %name)
    while True:
        baozi = yield

        print("包子[%s]来了，被[%s]吃了"%(baozi,name))

def  zuobaozi(name):
    c = chibaozi("YHZ")

    c2 = chibaozi("ZQ")

    c.__next__()

    c2.__next__()

    print("%s开始做包子了!"%name)

    for i   in  range(10):

        print("做了两个包子开吃吧！")
        c.send(i)
        c2.send(i)

zuobaozi("YS")