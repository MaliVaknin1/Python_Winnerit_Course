# Class work 1
text = input("Please enter word: ")
text_2 = input("Please enter another word: ")

if text == text_2[::-1]:
    print('Yes')
else:
    print('No')

# work class 2
salary = float(input("Please enter your salary: "))
if salary >= 20000:
    salary -= salary * 0.13
    print(salary)
else:
    print(salary)

# work class 3
number_a = int(input("Please enter a number: "))
result = "Even" if number_a % 2 == 0 else "Odd"
print(result)

# work class 4
day = input("Please enter a day: ")

match day.lower():
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")

# Work Class 5
loops = [20, 3, 15, 7, 12, 5]

for loop in loops:
    if loop > 10:
        print(loop)
