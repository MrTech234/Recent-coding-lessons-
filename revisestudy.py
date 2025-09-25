while True:
	print("\n my fine simple Calculator")
	num1 = float(input("Enter first number"))
	num2 = float(input("Enter second number"))
	operation = input ("+,-,*,/,**")
	if operation == "+":
		result = sum1 + sum2
	elif operation == "-":
		result = sum1 - sum2
	elif operation == "*":
		result = sum1 * sum2
	elif operation == "/":
		if sum2 != 0:
			result = sum1 / sum2
	elif operation == "**":
		result = sum1 ** sum2
	else:
		result = "invalid! division by zero"
	else:
		result = "invalid operation"
	print("Result:", result)
	choice = input("Do you wish to continue (yes/no)")
	if choice.lower() == "no":
		print( "Fuck you, bye bye motherfucker")
		break
