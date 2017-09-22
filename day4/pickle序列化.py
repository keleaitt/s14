import  pickle



info= {'name':'yuan','age':22}

f = open("pickle.txt","wb")

# f.write(pickle.dumps(info))

pickle.dump(info,f) # 等同于 f.write(pickle.dumps(info))

f.close()