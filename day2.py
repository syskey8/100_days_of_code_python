print("Hello"[4]) # prints the 4th charater in the string
print("Hello"[-1]) # prints the last character and so on

print("123" + "456") # concatenates the string, output: 123456

print(123 + 456) # does addition, output: 579
print(123_456_789) # will print 123456, it ignores _ this is just for easy readability for the human

print(3.14159) # float data type because of the decimal

#BooleanE
print(True)
print(False)

type("Hello") # gives the data type, output: <class 'str'>

#Type conversion
print(int("123") + int("456")) # coverts into int then adds, output:579


#Mathematical operators
print(123 + 456) # addtion, output 579
print(7 - 3) # subtraction, output 4
print(3 * 2) # multiplication, output: 6
print(6 / 3) # division but the answer is in float, output: 2.0
print(2 ** 3) # exponet 2 raise to 3, output: 8

# PENDAS rule is followed for operations, Parentheses, Exponents, Multiplication, Division, Addtion, Subtraction
# ()
# **
# * OR /
# + OR -

# This rule always follows LEFT TO RIGHT rule

print(3 * 3 + 3 / 3 - 3) # output: 7

print(round(30.85123)) # round function, output: 31
print(round(30.85123, 2)) # round to 2 digits, output: 30.85

# handy operators
score = 0
print(score) # output: 0
score += 1
print (score)# 0 + 1, output: 1, +=, -=, *=, /=

# imp automatic data conversion
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. Yor are winning is {is_winning}") # add all the requied data types automatically
