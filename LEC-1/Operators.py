# OPERATORS IN PYTHON
# An operator is a symbol that performs a certain operation between operands. In Python, there are severals types of operators, including arithmetic, assignment, comparison, logical, bitwise, and more.
# TYPES OF OPERATORS IN PYTHON
# 1. ARITHMETIC OPERATORS
# These operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc

a = 5
b = 2
print("Addition:", a + b)        # Output: 7
print("Subtraction:", a - b)     # Output: 3
print("Multiplication:", a * b)  # Output: 10
print("Division:", a / b)        # Output: 2.5
print("Floor Division:", a // b) # Output: 2
print("Modulus:", a % b)        # Output: 1
print("Exponentiation:", a ** b) # Output: 25

# 2. RELATIONAL OPERATORS
# These operators are used to compare two values and return a boolean result (True or False).

x = 50
y = 20
print("Equal to:", x == y)       # Output: False
print("Not equal to:", x != y)   # Output: True
print("Greater than:", x > y)     # Output: True    
print("Less than:", x < y)        # Output: False
print("Greater than or equal to:", x >= y) # Output: True
print("Less than or equal to:", x <= y)    # Output: False

# 3. ASSIGNMENT OPERATORS
# These operators are used to assign values to variables. The most common assignment operator is the equal sign (=), but there are also compound assignment operators that combine an arithmetic operation with assignment. 

num = 10
print("Initial value:", num)  # Output: 10
num += 5  # Equivalent to num = num + 5
print("After addition:", num)  # Output: 15
num -= 3  # Equivalent to num = num - 3
print("After subtraction:", num)  # Output: 12
num *= 2  # Equivalent to num = num * 2
print("After multiplication:", num)  # Output: 24
num /= 4  # Equivalent to num = num / 4
print("After division:", num)  # Output: 6.0
num //= 2  # Equivalent to num = num // 2
print("After floor division:", num)  # Output: 3.0
num %= 2  # Equivalent to num = num % 2
print("After modulus:", num)  # Output: 1.0
num **= 3  # Equivalent to num = num ** 3
print("After exponentiation:", num)  # Output: 1.0

# 4. LOGICAL OPERATORS
# These operators are used to combine conditional statements. The three main logical operators are and, or, and not.
# NOT OPERATOR
# The not operator is a unary operator that negates the truth value of a condition. If the condition is true, it returns false, and if the condition is false, it returns true.
# RETURNS opposite values if true then output will show false and if false then output will show true

print("NOT True:", not True)   # Output: False
print("NOT False:", not False) # Output: True

# AND OPERATOR
# The and operator is a binary operator that returns true if both conditions are true, and false otherwise.
# This operator works on two values and returns true if both values are true, otherwise it returns false.
"""
0 0 => 0
0 1 => 0
1 0 => 0
1 1 => 1
"""
# In and operator, if both conditions are true, the result is true; otherwise, the result is false.
val1 = True
val2 = True
print(val1 and val2)  # Output: True

val1 = True
val2 = False
print(val1 and val2)  # Output: False

# OR OPERATOR
# The or operator is a binary operator that returns true if at least one of the conditions is true, and false if both conditions are false.
# This operator works on two values and returns true if at least one of the values is true, otherwise it returns false.
"""
0 0 => 0
0 1 => 1
1 0 => 1
1 1 => 1
"""
# In or operator, if at least one condition is true, the result is true; otherwise, the result is false.
V1 = True
V2 = False 
print(V1 or V2)  # Output: True

V1 = False
V2 = False
print(V1 or V2)  # Output: False

