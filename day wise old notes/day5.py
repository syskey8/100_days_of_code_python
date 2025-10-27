# loop

fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)

fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_score = sum(student_scores) # gives the total of the values from the list
max_exam_score = max(student_scores) # gives the max value from the list

# using for loop using range function
for number in range(1, 10):
    print(number) # prints 1 to 9

for number in range(1, 11, 2):
    print(number) #prints 1 3 5 7 9

# The gauss challenge - print the sum of number from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)



