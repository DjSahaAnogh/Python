# This function will add 5% tip with the bill
def bill_calculator(in_put):
  def sum(bill):
    total = 0
    for amount in range(0, len(bill)):
      total = total + bill[amount]
    return total
  total = sum(in_put)
  tip = total * 5 / 100
  total_amount = total + tip
  print("Tip: ", tip)
  print("Payable amount: ", total_amount)


# Testing!
bill_calculator([100, 50])
