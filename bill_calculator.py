# Bill calculator-1 will add 5% tip.
# It can break anytime.
def bill_calculator_1(inPut):
  bill = inPut
  tip = bill * 5 / 100
  total_bill = bill + tip
  print(total_bill)


# Bill calculator-1 will add 5% tip.
# It won't break anytime.
def bill_calculator_2(inPut):
  try:
    bill = inPut
    tip = bill * 5 / 100
    total_bill = bill + tip
    print(total_bill)
  except Exception as e:
    print(e)


def bill_calculator_3(in_put):
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


def bill_calculator_4(in_put):
  try:
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
  except Exception as e:
    print(e)


bill_calculator_4("a")
