# marks1 = 94.4
# marks2 = 67.4
# marks3 = 42.3
# marks4 = 54.4
# marks5 = 95.8
# marks6 = 34.9

# to store these values , a python built in data type comes called lists
#representation of list in square [] brackets

marks = [94.4,  67.4, 42.3, 54.4, 95.8, 34.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["rimish", 99.9, "Delhi"]
print(student)

# LIST SLICING
marks = [85, 94, 76, 63, 98]
print(marks[1:4])
print(marks[ : 4])
print(marks[0 : ])
print(marks[-3 : -1])

#List Methods
list = [2,1,3]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(2, 22)
print(list)
list.insert(5, 1)
print(list)
list.remove(1)
print(list)
list.pop(3)
print(list)