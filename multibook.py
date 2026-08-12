class Book:
    def show(self):
        print("for discount on computer books visit AR store")
class old(Book):
    def type(self):
        print("It has good books")
class display(old):
        def head(self):
            print("display all books")
obj1=display()
obj1.head()
obj2=Book()
obj2.show()
obj3=old()
obj3.type()
