try:
    f=open("data.txt","r")
except FileNotFoundError:
    print("error")