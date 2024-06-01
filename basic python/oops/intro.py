# What is object oriented programming?

# is a programming paradigm where the software design revolves around objects/data

# helps to mimic real world entities and their interactions

# code can be reused 
# helps in organisation and mainatainablity of code


# classes
# user defined datatypes or a blueprint for an object



class student:


    def set_name(self,name):
        self.name=name

    def get_name(self): #self is a by default paprameter which is being passed
        return self.name #class attribute
    
student1= student()
student1.set_name("priya")
print(student1.get_name())
student1.eng_marks= 45 #instance attribute
print(student1.eng_marks)

student2= student()
student2.set_name("reena")
print(student2.get_name())


