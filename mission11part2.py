import random
secret_number = random.randint(1,20)
attempts_left = 5
while attempts_left > 0:
	guess = int(input("Guess a number between 1 and 20: "))
	if guess < secret_number:
		print("Too low! ")
	elif guess > secret_number:
		print("Too high! ")
	else:
		print("Correct! You guessed it. ")
		break
	attempts_left -= 1
	print(f" you have {attempts_left} ")
if attempts_left == 0:
	print(f" Game over! The secret number was {secret_number} you are a failure, you are a failure, you can not make it. ")
