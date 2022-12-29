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
