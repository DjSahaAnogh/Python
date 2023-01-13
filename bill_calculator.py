# This function will add 5% tip with the bill
def bill_calculator():
  amount = int(input("Enter the total amount: "))
  tip = amount * 5 / 100
  total_amount = amount + tip
  print("Tip: ", tip)
  print("Payable amount: ", total_amount)


# Testing!
bill_calculator()
