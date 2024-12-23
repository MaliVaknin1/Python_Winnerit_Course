# lambda function
greet = lambda: print("Test function")

greet()

# structure of lambda -- name = lambda , something to send, function to do.
square_1 = lambda num: num ** 2
print(square_1(10))

# map function + lambda, מה שבעצם הפונקציה הזו עושה לוקחת את כל המספרים שהם כמערך,
# ואז הלמבדה מריצה את הפונקציה על כל המספרים שבמערך- היא לקחה את המספר הראשון
# והכניסה אותו לערך X ואז המפ שומר את הכל בערך אחד, ואז הליסט ממיר את זה למערך חדש
numbers4 = [1, 2, 3, 4, 5, 6, 7]
squared_num = list(map(lambda x: x ** 2, numbers4))
print("lambda function ", squared_num)

# Filter function +lambda-the same as map function, but it returns
# just the elements that the condition-function is True.
numbers4 = [1, 2, 3, 4, 5, 6, 7]
squared_num = list(filter(lambda x: x % 2 ==0, numbers4))
print(f"filter function {squared_num}")

# get list of numbers, make function on it, and returns as list
nums= map(int,input("Enter your scores , separate with space").split())
whole_nums_cast= list(map(int, nums))
print(whole_nums_cast)

#list comprehension- זה קיצור של יותר מלמבדה ופילטר והכל
#structure- [expression for item in iterable if condition]
squared_num= [x ** 2 for x in numbers4]
print(f"list Comprehension: {squared_num}")


#oop
class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age


    def bark(self):
        print("woof!")

dog1= Dog("Coco", 1)
dog2= Dog("Bar", 5)\

print(dog1.name)
dog2.bark()

class Animal(Dog):
    def __init__(self):
        super().__init__("Bart", 0)
    def __str__(self):
        return f"The name of animal is :{self.name} and the age is: {self.age}"
animal= Animal()
print(animal)