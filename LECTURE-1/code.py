class Student:
    def __init__(self, name, gender, course, year, CGPA):
        self.name = name
        self.gender = gender
        self.course =course
        self.year = year
        self.CGPA = CGPA
    
    def showDetails(self):
        print("Your name: ", self.name)
        print("Your gender: ", self.gender)
        print("Your course ", self.course)
        print("Your year: ", self.year)
        print("Your CGPA: ", self.CGPA)
    
stu1 = Student("Rimish Chandra Srivastava", "Male", "BTech", 4, 8.8)
stu1.showDetails()