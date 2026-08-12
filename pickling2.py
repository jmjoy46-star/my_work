import pickle
f=open("data.txt","rb")
data=pickle.load(f)
print(data)
f.close()