# many forms

# allows objects of different classes to behave as oj=bjects of same super class

class animal:
    def speaks():
        pass

class dog(animal):
    def speaks(self):
     print("barks")

class cat(animal):
    def speaks(self):
     print("meow")


Dog=dog()
Cat=cat()

Dog.speaks()
Cat.speaks()

# types
# run time polymorphism
# compile time polymorphism

