num1 = float(input("First number= "))
operator = input("Enter operator= ")
num2 = float(input("Second number= "))

if "+" == operator:
  Add = num1 + num2
  print(Add)
elif "-" == operator:
  Sub = num1 - num2
  print(Sub)
elif "*" == operator:
  Multi = num1 * num2
  print(Multi)
elif "/" == operator:
  Div = num1 / num2
  print(Div)
elif "^" == operator:
  Sq = num1 * num1
  print(Sq)
else:
  print("E")
