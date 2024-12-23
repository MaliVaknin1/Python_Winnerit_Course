#Class_Work_ex. 1
from symtable import Class


#regular function
def even_numbers (numbers_list_1):
    return [num for num in numbers_list_1 if num % 2 == 0]

numbers_list= [2,4,7,8,10]
even_numbers= (even_numbers(numbers_list))
print(f"using regular function: " ,even_numbers)

#lambda function
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers_list))
print(f"using lambda function: ", even_numbers_lambda)


class Person:
    def __init__(self, name):
        self._name= name

    def get_name(self):
        return f"Name of person is:{self._name}"

class Student(Person):
     def __init__(self, name, student_id ):
         super().__init__(name)
         self.__student_id=student_id

     def display_student_id(self):
         return f"Student ID: {self.__student_id}"

     @property
     def name(self):
         return self._name
     @name.setter
     def name(self, new_name):
         self._name=new_name

person1=Person("Omer")
print(person1.get_name())

student1=Student("Eitan",45678654)
print(student1.name)

student1.name="New_name- Rafi"
print(student1.name)


