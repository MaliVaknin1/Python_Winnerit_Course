# str1= "Hello"
# str2 ='Hello'
# multi_lines= """Hello 1
# Hello 2
# Hello 3 """
#
# print(f"{str1} {str2} \n{multi_lines}")
#
# #output text.text
# print('text'+ ".text")
#
# #output text text text
# print('text '*3)
#
# #lenght of text -output 5
# text='Hello'
# print(len(text))
#
# #index
# string_12 = 'python'
# print(string_12[0])  #output 'p'
# print(string_12[-1])  #output 'n'
#
# #string slicing
# print(string_12[1:4]) #output 'yth'
#
my_name = "Mali_Vaknin"
print(my_name[0:8:2])  #output 'Ml_a'
print(my_name[::-1])  #output 'ninkaV_ilaM'


#Methods of strings
print(my_name.lower()) #output "mali_vaknin"
print(my_name.upper())  #output "MALI_VAKNIN"
print(my_name.replace("Vaknin", "Update")) #output "Mali_Update"
print(my_name.split(",")) #output "Mali_Vaknin"
print(my_name.startswith("Mali")) #output "True"
print('al' in my_name) #output "True"

#F- string
age= 28
message= f"My name is: {my_name} and my age is: {age} ."
print(message)


x=120
y=1
result_string= f"The sum of {x} + {y} is: {x+y}"
print(result_string)

message= f"{my_name= }, and {age= }"
print(message)

#List
list_mix= [1, True, "Hello", 3.99]
print(list_mix[1])
#index position
last_index= list_mix[-1]
print(last_index)
#update value to index position
list_mix[0]= "update"
print(list_mix)

list_mix.append("Add_element")
print(list_mix)

x=list_mix.count(True)
print(x)

list_mix.insert(1,"Adding object to index 1")
print(list_mix)

list_mix.remove(True)
print(list_mix)

list_mix.pop(-1)
print(list_mix)

numbers=[9,6,8,7,4]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)





