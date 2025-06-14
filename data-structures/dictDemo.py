student={
    "name": "Utkarsh",
    "age": 21,
    "course": "MCA"
}
print(student) #printing the full dictionary
print("Name: " + student["name"]) #printing the student's name
print("Age: "+ str(student["age"])) #printing the student's age
print("Course: " + student["course"]) #printing the student's course

student["age"]=19 #updating the student's age
print("Updated age: "+ str(student["age"]))

student["city"]= "Indore" #adding city element in the dictionary
print("City: "+ student["city"])

student.pop("course") #dropping the course element and value

print(student) #printing key value pairs