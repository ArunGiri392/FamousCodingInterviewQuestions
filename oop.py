class students:
    def __init__(self,name, age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class course:
    def __init__(self,course_name,max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []
    
    def add_students(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def average(self):
        result = 0
        for student in self.students:
            result += student.get_grade()
        return result//len(self.students)
        
# s1 = students("arun",12,95)
# s2 = students("sandesh",14,75)
# s3 = students("subrat",18,65)

# computer = course("computer",2)
# computer.add_students(s1)
# computer.add_students(s2)
# print(computer.add_students(s3))
# print(computer.students[1].age)
# print(computer.average())

# inheritance in oop.
class pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("i am {} and i am {} years old".format(self.name, self.age))
    def speak(self):
        print("I HAVE A WOEK TO DO")
class cat(pet):

# super keyword helps us to call the method in the parent class. We want to add another attribute in this cat class so what we do is first of all c
# call the constructor in the parent method using super keyword and pass the name,and age and the line 40 gets executed and in line 41 and 42 self
# .name and self.age gets updated to the value we have provided and since this is a child class, it will inherit every attribute from the parent class.
    def __init__(self,name,age,color):
        super().__init__(name,age)  
        self.color = color

    def speak(self): # overriding - A child class is overriding the method from the parent class.
        print("Meow")
    def show(self):
        print(" i am {} and i am {} years old and i am {} color".format(self.name, self.age,self.color))
class dog(pet):
    def speak(self): # overriding - A child class is overriding the method from the parent class.
        print("bark")
# p = pet("tim",19)
# p.speak()

# c = cat("arun",12,"black")
# c.show()

# # d = dog("subrat",45)
# d.speak()

# class attributes - for class not more objects.

class person:
    total_person = 0
    def __init__(self,name):
        self.name = name
        #self.total_person += 1 will not increase it because as soon as we write self. it denotes object and for every object it will be new.
        person.total_person += 1 # as we said, it is a class attribute so we need to use class to increment the value. nothing to do with the object.
        print(person.total_person)

p1 = person("arun")
p2 = person("sandesh")
p3 = person("sandesh")
# print(p1.total_person)
# print(person.total_person) # because this is specific to class, we can acess it using the class too,. also can be accessed using object.
# person.total_person = 5
# print(p2.total_person)

    
# class methods.
