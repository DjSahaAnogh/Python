import re

# r = float(input("Enter the radius of the circle: "))
# ans = pi * r**2
# print("Answer: "+str("%d" % ans))

# first_name = input("First name: ")
# last_name = input("Last name: ")
# print(last_name + " " + first_name)

# values = input("Input some comma separated numbers : ")
# list_1 = values.split(",")
# tuple_1 = tuple(list)
# print("List : ", list)
# print("Tuple : ", tuple)

string_1 = input("Enter numbers: ")
numbers = re.findall(r'\d+', string_1)
list_1 = list(numbers)
print(list_1)
tuple_1 = tuple(list_1)
print(tuple_1)
