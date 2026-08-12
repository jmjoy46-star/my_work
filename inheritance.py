class Father:


    def input(self):

        name=input("Enter father name:")
        job=input("enter father's job")
        print(f"Father name is:{name}")
        print(f"job is {job}")

class mother():
    def getdata1(self):
        name1=input("enter mother name")
        job1=input("enter mother job")
        print(f"job is {job1}")
        print(f"mother name:{name1}")
class Child(Father,mother):
    def getdata(self):
        name2=input("enter name of child")
        print(f"child name is:{name2}")
obj=Father()
obj2=mother()
obj.input()
obj2.getdata1()
















