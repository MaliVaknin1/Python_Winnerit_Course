#H.W. ex. 1
from typing import List


class Person1:
    def __init__(self, name):
        self.name= name
    def get_name(self):
        return f"The name of person is: {self.name}"

class Employee(Person1):
    def __init__(self, name, salary, role):
        super().__init__(name)
        self.__salary=salary
        self.__role= role

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
           raise ValueError("The salary can't be negative number")
        self.__salary =new_salary

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, new_role_value):
        if not new_role_value :
            raise ValueError("The role can't be empty value")
        self.__role=new_role_value

employee1=Employee("Rami", 20000, "DevOps")
print(employee1.get_name())
print(employee1.role)
print(employee1.salary)

employee1.role= "QA"
print(f"The new role is: {employee1.role}")

employee1.salary= 10000
print(f"The new salary is: {employee1.salary}")
#
# employee1.role= ""
# print(employee1.role)
#
# employee1.salary=0
# print(employee1.salary)

#H.W. ex. 2
def list_words(words: List[str], length_num: int) -> List[str]:
    return [word for word in words if length_num >= len(word)]
words=["cucumber", "grapes", "banana"]
filter_words= list_words(words, 10)
print(filter_words)