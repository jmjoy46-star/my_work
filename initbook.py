class Book:
    def __init__(self):
        print("for discount on computer books visit AR store")
class old(Book):
    def __init__(self):
        Book.__init__(self)
        print("computer books from 2000 to 2010 has 5% discount,from 2010 to 2030 is 10 %,from 2030 to 2050 is 15%")

class display(old):
        def __init__(self):
            old.__init__(self)
            print("damage books on table")
            print("others are on shelf")
obj1=display()
obj2=old()
