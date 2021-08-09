# Python does not require a key word to declare a value as a variable.
first_name = 'Clint'
print(first_name)

# Strings can be set with single or double quotes.
last_name = "Edwards"
print(last_name)

# Note, like JavaScript, Python variables can change type.
age = 'thirty-five'
age = 35
bank_account = 0.190548273
loves_code = True
print(age)
print(bank_account)
print(loves_code)
if age > 17:
      print("You're Old")
elif age == 17:
      print("You are exactly 17! Wow cool")
else:
      print("you are a whippersnapper")

# Use the type function to see the type of a given value.
print(type(first_name))
print(type(age))

# Comments are set with the octothorpe (pound, hashtag).

# If Statements
if age >= 18:
  print('I am an adult.')

# If-else Statements
if age >= 18:
  print('I am an adult.')
else:
  print('I am a child.')

#If-elif-else
if age >= 18:
  print('I am an adult.')
elif age < 13:
  print('I am a child.')
else:
  print('I am a teen.')

## Note: above code would break if you had two blank lines in between code.

# For-In-Loop (similar to JavaScript for-loop)
numbers = [1,2,3,4,5,6,7,8]
for x in numbers:
  print(x)

# Another example of for-in loop, also demonstrating creation of array and use of a built in method, just like you would do in JavaScript.
instructors_and_jeddy = ['cameron', 'riley', 'eric', 'nitin']
for cool_cat in instructors_and_jeddy:
  print(cool_cat.capitalize())

# Handling Data with Python
open_file = open('FinalGrades.csv')

for row in open_file:
  print(row)

open_file.close()

# A more complicated look at what we can do with the data.
open_file = open("FinalGrades.csv")
total_a = 0
total_b = 0
total_c = 0

for line in open_file:
  line = line.rstrip('\n').split(',')
  for value in line: 
    if value == "A": 
      total_a += 1
    elif value == "B":
      total_b += 1
    elif value == "C": 
      total_c += 1

print("A's:", total_a)
print("B's:", total_b)
print("C's:", total_c)

open_file.close()

