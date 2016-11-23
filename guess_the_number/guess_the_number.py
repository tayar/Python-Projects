import sys
import random


number = random.randint(1,100)
guess_count = 1

def guessing_game():
		guess = int(raw_input("> "))
		if guess > number:
			print "Too high. Try a lower number."
			global guess_count 
			guess_count +=1
			guessing_game()
		elif guess < number:
			print "Too low. Guess a higher number."
			global guess_count
			guess_count +=1
			guessing_game()
		elif guess == number:
			global guess_count
			print "You got it!"
			print "It only took you %d guesses" %(guess_count)
			exit()
		elif guess == "QUIT":
			print "Closing game..."
			exit()
		else:
			print "That's not a number. Do you have to go back to pre-school?"
			guessing_game()


def guess_the_number():
	print "Welcome to Guess the Number!"
	print "Alright, pick a number from 1 to 100"
	print "To quit, type 'QUIT'"
	guessing_game()
				
guess_the_number()
	
	
		