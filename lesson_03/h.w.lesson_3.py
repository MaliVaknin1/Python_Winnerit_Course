# H.W. no.1
num_1 = float(input("Please enter no.1: "))
num_2 = float(input("Please enter no.2: "))
print(f"The length between numbers is: {(abs(num_1 - num_2))}")

# H.W. no.2
grams = int(input("Please enter grams: "))
print(f"The kg in this grams are: {(round(grams / 1000))}")

# H.W. no. 3
number_a, number_b = map(int, input("Please enter 2 numbers: ").split())
print(f"The numbers divide with 7: {(number_a % 7 == 0) and (number_b / 7 == 0)}")

# H.W. no.4
print(int(input("Please enter number: ")) % 10)
