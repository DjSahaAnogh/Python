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
    print(num1*num1*num1)
  else:
    print("Error")
    

calculator(10, 5, "-")


def raise_power(based_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * based_num
    return result
    
raise_power(2, 2)
