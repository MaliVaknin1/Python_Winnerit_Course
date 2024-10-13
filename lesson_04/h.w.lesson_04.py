#h.w. ex. 1
from os import remove

user_string= input(f"Please enter characters: ")
middle_char= user_string[len(user_string)//2]
print(f" The first character is: {user_string[0]}, The last character is: {user_string[-1]},"
      f" The middle character is: {middle_char}, The even characters are: {user_string[0::2]}, "
      f"The odd characters are: {user_string[1::2]}, The reversed characters are: {user_string[::-1]}" )

#h.w. ex. 2
user_message= input(f" Please enter a message: ")
print(f" Upper_message is: {user_message.upper()} , Lower_message is: {user_message.lower()},"
      f" Capitalize_message is: {user_message.capitalize()} The title is: {user_message.title()}, "
      f" Split_message is: {user_message.split()} ")

#h.w. ex. 3
width_resolution= int(input("Please enter width of screen: "))
height_resolution=int(input("Please enter height of screen: "))
print(f"{width_resolution= } x {height_resolution} \n"
      f"Total pixels are: {width_resolution * height_resolution}")

#h.w. ex. 4
numbers_list=list(range(1,17))
removed_numbers = [numbers_list.pop(-1), numbers_list.pop(0),
                   numbers_list.pop(12), numbers_list.pop(7)]
print(f"The numbers list without removed numbers: {numbers_list}")
print(f"The removed numbers: {removed_numbers}")
print(f"The sum of all removed numbers: {sum(removed_numbers)}")







