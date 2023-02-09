def calculator():
  operation = input("Enter an operation (+, -, *, /): ")
  if operation not in ['+', '-', '*', '/']:
    print("Invalid operation. Please enter a valid operation.")
  
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  
  if operation == '+':
    print(num1 + num2)
  elif operation == '-':
    print(num1 - num2)
  elif operation == '*':
    print(num1 * num2)
  elif operation == '/':
    if num2 == 0:
      print("Cannot divide by 0.")
    else:
      print(num1 / num2)


def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  print(result)


def cube(num):
  ans = num * num * num
  print(ans)


cube(3)
