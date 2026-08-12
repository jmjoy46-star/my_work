import pickle
data=["ASHJAN",20,3000]
f=open("data.txt","wb")
pickle.dump(data,f)
f.close()
print("Data stored successfuly")