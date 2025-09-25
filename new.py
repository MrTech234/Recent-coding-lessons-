while True:
	print("\n Simple Calculator")
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	operator = input("Choose an operator(+,-,*,**,/,%): ")
	if operator == "+":
		result = num1 + num2
	elif operator == "-":
		result = num1 - num2
	elif operator == "*":
		result = num1 * num2
	elif operator == "**":
		result = num1 ** num2
	elif operator == "/":
		if num2 != 0:
			result = num1 / num2
		else:
			print("Invalid, division by zero")

			continue
	elif operator == "%":
                result = num1 % num2
	else:
		print("Invalid operator! try again")
		
		continue
	print("Result:", result)
	choice = input("Do you want to continue (yes/no) ")
	if choice.lower() == "no":
		print("Good fucking bye!")
		break
