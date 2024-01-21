class parent:
    def __init__(self):
        self.superAttribute = True
        print("this is a parent class")


class child(parent):
    def __init__(self):
        super().__init__()
        print("this is a child class")
        print(self.superAttribute)


child1=child()

# types of inheritance
# single inheritance
# multiple inheritance
# multilevel inheritance
# heirarchical inheritance
# hybrid inheritance