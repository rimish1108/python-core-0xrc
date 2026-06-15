# WAP TO DISPLAY THE GRADES OF A STUDENT ACHIEVE ACCORDING TO THEIR OBTAINED MARKS

marks = int(input("Enter you marks :"))
if(marks>=90):
    print("Student got 'A' grade")
elif(marks>= 80 and marks< 90):
    print("Student got 'B' grade")
elif(marks>= 70 and marks<80):
    print("Student got 'C' grade")
elif(marks<70):
    print("Student got 'D' grade")
else:
    print("Sorry, Better luck next time")