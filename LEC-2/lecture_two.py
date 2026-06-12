# Valid ways of creating a string 
str1 = "This is a string"
str2 = 'Rimish Chandra Srivastava'
str3 = """This is a String"""
print(str1)
print(str2)
print(str3)

# CONCATENATION
str4 = "Rimish"
str5 = "Srivastava"
print(str4 +" "+ str5)

# Finding Length of a string by using length function
str6 = "I love my india"
print(len(str6))

# INDEXING
str7 = "Rimish Chandra Srivastava"
ch = str7[22]
print(ch)

# SLICING
str8 = "Rimish Chandra Srivastava"
print(str8[0:4])
print(str8[0: ])
print(str8[1:8 ])
print(str8[ :8])
print(str8[3:7])
print(str8[4: ])
print(str8[5:19])

# NEGATIVE INDEXING IN SLICING
str9 = "APPLE"
print(str9[-3:-1])