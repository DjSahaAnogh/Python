def bill_calculator():
	bill = input("Enter the bills: ")
	bill_list = list(map(int, bill.split(", ")))
	print(sum(bill_list))


bill_calculator()
