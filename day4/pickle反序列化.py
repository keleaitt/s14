import pickle

f =  open("pickle.txt",'rb')

# data = pickle.loads(f.read())

data  = pickle.load(f) # 等同于  data = pickle.loads(f.read())


print(data["age"])
