import random
secret_number = random.randint(1,20)
attempts = 0
while True:
	guess = int(input("Guess a number between 1 and 20: "))
	attempts += 1
	if guess < secret_number:
		print("Too low! ")
	elif guess > secret_number:
		print("Too high! ")
	else:
		print(f" correct! you guessed it in {attempts} tries .")
		break
