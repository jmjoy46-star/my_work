class Market:
    def __init__(self):
        print("All types of shops are available")
class Stationary(Market):
    def __init__(self):
        print("All types of books are available in some shops ")
        print("computer accessories are also available")
class Marginfree(Market):
    def __init__(self):
        print("All types of shampoos are available")
        print("wed and thurs are holiday")
        print("A good day to spend money")
class dutyfree(Marginfree,Stationary):
    def __init__(self):
        pass

obj2=dutyfree()
obj1=Marginfree()
obj3=Stationary()
obj4=Market()

