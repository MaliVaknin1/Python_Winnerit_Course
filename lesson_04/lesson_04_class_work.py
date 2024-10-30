# Class work 1
my_string = input("Enter your string: ")
print(my_string[:4])

# Class work 2
your_string = input("Enter your string: ")
print(your_string[-1] + your_string[:-1])

# Class work 3
mystring = input("Enter string: ")
print(mystring[1::2])

# Class work 4
name = input("Please enter your name: ")
print(name.upper())

# Class Work 5
string_min_6_char = input("Please enter minimum 6 characters: ")
output_string = string_min_6_char[:3].upper() + string_min_6_char[3:-3].lower() + string_min_6_char[-3:].upper()
print(output_string)
