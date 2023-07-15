def resistance():
	x = input("Enter type: ")
	if x in ["R", "I", "V"]:
		pass
	else:
		print("Invalid parameter!")
		return
	if not x in ["V", "R"]:
		V = int(input("Value of Volt: "))
		R = int(input("Value of Resistance: "))

		I = V / R
		print(I)
		return
	if not x in ["R", "I"]:
		I = int(input("Value of electricity: "))
		R = int(input("Value of Resistance: "))

		V = R * I
		print(V)
		return
	if not x in ["I", "V"]:
		I = int(input("Value of electricity: "))
		V = int(input("Value of Volt: "))

		R = V / I
		print(R)
		return
	else:
		print("Sorry!")


resistance()
