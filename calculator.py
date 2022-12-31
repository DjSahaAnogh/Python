def calculator(num1, num2, operator):
  if "+" == operator:
    print(num1 + num2)
  elif "-" == operator:
    print(num1 - num2)
  elif "*" == operator:
    print(num1 * num2)
  elif "/" == operator:
    print(num1 / num2)
  elif "^2" == operator:
    print(num1 * num1)
  elif "^3" == operator:
    print(num1 * num1 * num1)
  else:
    print("Error")


def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  print(result)


raise_to_power(10, 10)
