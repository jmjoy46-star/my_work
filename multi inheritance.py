class Father:
    def about_father(self):
        print("Father is the head of the family")
class Mother():
    def about_mother(self):
        print("Mother is the housewife")
class child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
obj2=child()
obj2.about_father()
obj2.about_mother()






