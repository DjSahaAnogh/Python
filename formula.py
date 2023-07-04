def a_plus_b(num1, num2):
	sum1 = num1 * num1
	sum2 = 2 * num1 * num2
	sum3 = num2 * num2
	print(sum1, sum2, sum3, sep=" + ")


a_plus_b(2, -5)

def asqr_bsqr(num1, num2):
	sum1: int = (num1 + num2)*(num1 + num2)
	sum2: int = -2*num1*num2
	print(sum1, sum2, sep=" - ")


asqr_bsqr(4, 5)
