class Person:
    #Properties/variables/attributes/characteristics
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Behaviour/Method/Function
    def study(self):
        print("Student is studying")


    #creating an object
student1 = Person(name='Hussein', age=23, gender='Male')
print(student1.name, student1.age, student1.gender)
student1.study()
student2 = Person(name="Charles", age=45, gender='Male')
print(student2.name, student2.age, student2.gender)
student3 = Person(name="Beatrice", age=34, gender='Female')
print(student3.name, student3.age, student3.gender)
