def calculator():
  num1 = int(input("Enter the first number: "))
  symbol = input("Enter a math operator: ")
  num2 = int(input("Enter the second number: "))

  if symbol in ["+", "-", "*", "/"]:
    pass
  else:
    print("Invalid operator!")
    return

  if not symbol in ["-", "*", "/"]:
    sum_result = num1 + num2
    print("The sum is: ", sum_result)
    return

  if not symbol in ["+", "*", "/"]:
    sum_result_1 = num1 - num2
    print("The result is: ", sum_result_1)
    return
  if not symbol in ["+", "-", "/"]:
    sum_result_2 = num1 * num2
    print("The result is: ", sum_result_2)
    return
  if not symbol in ["+", "-", "*"]:
    sum_result_3 = num1 / num2
    print("The result is: ", sum_result_3)
    return


calculator()


def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  print(result)


def cube(num):
  ans = num * num * num
  print(ans)
