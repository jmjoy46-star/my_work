class Book:
    def bookname(self):
        print("All types of books are recieved at AR Store")
class old(Book):
    def oldbook(self):
        print("All the book recieve 10% discount")
class display(old):
    def show(self):
        print("All types of books are displayed in shelf")
obj1=display()
obj1.oldbook()
obj1.show()
obj1.bookname()