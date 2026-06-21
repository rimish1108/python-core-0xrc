class Student:
    def __init__(self, name, gender, course, year, CGPA):
        self.name = name
        self.gender = gender
        self.course = course
        self.year = year
        self.CGPA = CGPA

    def showDetails(self):
        print("\n--- Student Details ---")
        print("Your name:", self.name)
        print("Your gender:", self.gender)
        print("Your course:", self.course)
        print("Your year:", self.year)
        print("Your CGPA:", self.CGPA)

# Taking input from the user
name = input("Enter your name: ")
gender = input("Enter your gender: ")
course = input("Enter your course: ")
year = int(input("Enter your year: "))
CGPA = float(input("Enter your marks: "))

# Creating object
stu1 = Student(name, gender, course, year, CGPA)

# Displaying details
stu1.showDetails()