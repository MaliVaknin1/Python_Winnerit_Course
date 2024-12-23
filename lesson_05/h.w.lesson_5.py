# H.w. ex.1.
age = int(input("Please enter your age: "))
has_ticket = input("Do you have a ticket? (Yes/ No) ").strip().lower() == "yes"
has_permission = input("Do you have a special permission? (Yes/ No) ").strip().lower() == "yes"

if age >= 18 and has_ticket:
    print("You can enter to the club! ")
elif age >= 18 and not has_ticket:
    print("You can't enter to the club! ")
elif age < 18 and has_permission:
    print("You can enter to the club! ")
else:
    print("You can't enter to the club! ")

# H.w. ex.2.
number_1 = float(input("Please enter number: "))
number_2 = float(input("Please enter another number: "))

larger_num = number_1 if number_1 >= number_2 else number_2
print("The larger number is: ", larger_num)

# H.w. ex. 3
month = input("Please enter the current month: ")

match month.lower():
    case "january" | "february" | "december":
        print("The season is: Winter")
    case "march" | "april" | "may":
        print("The season is: spring")
    case "june" | "july" | "august":
        print("The season is: Summer ")
    case "september" | "october" | "november":
        print("The season is: Fall ")
    case _:
        print("Invalid month")

# H.w. ex. 4
total = 0
count = 5
for i in range(count):
    number = float(input(f"Please enter number {i + 1}: "))
    total += number

avg = total / count
print(f"The average of all numbers is: {avg}")


# H.w. ex. 5
def find_max(*args):
    if not args:
        return "No numbers were given "
    max_num = args[0]
    for num in args:
        if num > max_num:
            max_num = num
    return max_num


numbers = find_max(3, 45, 12, 44, 21, 54, 34656, 546452, 564)
print(numbers)


# H.w. ex.6
def calculate_average(nums_list: list[int]):
    if not nums_list:
        return 0
    total_list = 0
    for num in nums_list:
        total_list += num
    return total_list / len(nums_list)


numbers_list = [4, 5, 3, 235, 35]
average = calculate_average(numbers_list)
print(average)
