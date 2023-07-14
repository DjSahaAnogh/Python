def resistance():
	x = input("Enter type: ")
	if x == ["R", "I", "V"]:
		return
	else:
		print("Invalid parameter!")
	if not x in ["V", "R"] or x == "I":
		V = int(input("Value of Volt: "))
		R = int(input("Value of Resistance: "))

		I = V / R
		print(I)
		return
	if not x in ["R", "I"] or x == "V":
		I = int(input("Value of electricity: "))
		R = int(input("Value of Resistance: "))

		V = R * I
		print(V)
		return
	if not x in ["I", "V"] or x == "R":
		I = int(input("Value of electricity: "))
		V = int(input("Value of Volt: "))

		R = V / I
		print(R)
		return
	else:
		print("Sorry!")


resistance()
