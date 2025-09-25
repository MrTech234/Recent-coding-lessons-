while True:
	correct_username = "Ebuka"
	correct_password = "123"
	attempts = 0
	max_attempts = 3
	while attempts < max_attempts:
		username = input("Enter your username: ")
		password = input("Enter your password: ")
		if username == correct_username and password == correct_password:
			print("Login successful")
			break
		else:
			print("incorrect, try again")
		attempts += 1
		if attempts == max_attempts:
			print("Incorrect, Access Denied! ")
			break
