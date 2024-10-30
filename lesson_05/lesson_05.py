from operator import ifloordiv

age = 25
numbers = int(input("please enter number: "))

print("before if statement: ")
if numbers > 0:
    print(f"Number {numbers} is greater than 0. ")
print("After if statement: ")

# Loop
fruit = ["apple", "banana", "cherry"]
for i in range(1, 2, 10):
    print(i)

# condition
if 'banana' in fruit:
    print('banana is in the fruit list. ')
else:
    print("banana isn't n the fruit list. ")

if age >= 11 and numbers == 2:
    print("Age is 11+ and numbers are 2 ")
elif age == 11 or numbers >= 3:
    print("Age is 11 and numbers is 3 ")
else:
    print("out of condition!!")

# ternary operator
is_adult = "Adult" if age >= 20 else "Teenager"
print(is_adult)

# Loops, range function
range_list = list(range(4, 11, 2))
print(range_list)  # output: [4, 6, 8, 10 ]

# Loops , continue and break
for number in range_list:
    if number == 5:
        break  # if number ==5 - out of all loop
    if number == 3:
        continue  # if number ==3 - jump to next condition and do nothing
    if number % 2 == 0:
        print(f"Even number: {number}")


# Function
def name_of_function(name):
    print(f"The function is: {name}")


# function-return
def name_of_function_return(a, b):
    return a + b


result12 = name_of_function_return(8, 9)
print(result12)  # output= 17


# function - with default value
def test_function(value="Guest"):
    print(f"Output of function {value}! ")


test_function()
test_function("update_guest")


# Function- args
def my_function(*args):
    for arg in args:
        print(arg)


my_function(2, 3, 4, 5, 6)

# Function- lambda
square = lambda x: x ** 2
print(square(6))  # output 36

# Function - lambda with map(), it returns the iteration with action
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # lambda= the function, numbers= iterable= list
print(squared_numbers)  # output [1, 4, 9, 16, 25]

# Function- lambda with filter(), it returns what's True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # output [2, 4]
