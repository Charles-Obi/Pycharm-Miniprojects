courses = ["MIT", "Cyber security","Datascience"]
print(courses)
#Accessing an element in array
print(courses[0])

#looping through an array
for y in courses:
    print("Course is", y)

#adding a new element
courses.append("Web Development")
print(courses)

#deleting an element
courses.remove("MIT")
print(courses)