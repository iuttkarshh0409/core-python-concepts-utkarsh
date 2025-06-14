marks= int(input("Enter your marks: "))

if marks >= 90:
    print("Marks: "+ str(marks)+" Your grade is A")

elif 80<=marks<=89:
    print("Marks: "+ str(marks)+" Your grade is B")

elif 70<=marks<=79:
    print("Marks: "+ str(marks)+" Your grade is C")

elif 60<=marks<=69:
    print("Marks: "+ str(marks)+" Your grade is D")

else :
    print("Marks: "+ str(marks)+" Your grade is F")
