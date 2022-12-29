def calculator(num1, num2, operator):
  if "+" == operator:
    add = num1 + num2
    print(add)
  elif "-" == operator:
    sub = num1 - num2
    print(sub)
  elif "*" == operator:
    multi = num1 * num2
    print(multi)
  elif "/" == operator:
    div = num1 / num2
    print(div)
  elif "^2" == operator:
    sq = num1 * num1
    print(sq)
  elif "^3" == operator:
    cube = num1 * num1 * num1
    print(cube)
  else:
    print("Error")


calculator(4, 0, "^")
