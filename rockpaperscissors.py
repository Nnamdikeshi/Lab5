from random import randint
import sys

# Rock Paper Scissors created by Nnamdi Keshi
# Resources used to help create this game:
# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://docs.python.org/3/tutorial/

# Set our Global score variables
wins = 0
loss = 0
ties = 0
outcome = ''

# Main
def main():
	

	# Open the file back and read the contents
	rcp_rules = open('rcp_rules.txt', 'r')
	if rcp_rules.mode == 'r': #check to ensure that the file was open
		contents = rcp_rules.read()
		print (contents) #Print rules :)
	# Call in our global variables

	global wins, loss, ties
	
	# Loop control with play variable
	play = 'yes'
	
	# Essentially the game start
	while play == 'yes':
	
		# Assign the player and computers choices to variables
		player = get_player_pick()
		computer = get_computer_pick()
		# Function to determine who wins
		winner_pick(player, computer)
		# Player continuation choice
		play = str(input("**Do you wants to play again? type yes or no **\n"))
	
	# Print our score board
	print('You have', wins, 'wins! ^_^')
	print('You have', loss, 'losses -___-')
	print('You have', ties, 'ties -_-')
	
# Player choice definition 
def get_player_pick():
	# Gather the users input
	player = input('\nRock (r), Paper (p) or Scissors (s)?\n')
	# Assign choice with its corresponding option
	if player == "r":
		player = "Rock"
		
	elif player == 'p':
		player = 'Paper'
		
	elif player == 's':
		player = 'Scissors'
	else:
		print ("Your input was wrong.. Try again")
		get_player_pick()
	# Return players choice
	return player
			
# Computer choice definition
def get_computer_pick():
	# Random function to determine a generated choice  in the range of 1-3
	chosen = randint(1,3)
	# Determine the computers choice based on random generated #
	if chosen == 1:
		computer = "Rock"

	elif chosen == 2:
		computer = 'Paper'

	else:
		computer = 'Scissors'
	# Return Computers choice
	return computer
	
# Winner definition	
def winner_pick(player, computer):
	# Call our global variables
	global wins, loss, ties, outcome 
	# Determine who won and record the outcome
	# After winner determined print who won 
	if player == computer:
		outcome = 'tie'
		print('Draw')
		
	elif player == "Rock" and computer == 'Scissors':
		outcome = 'win'
		print('\nRock beats Scissors!\nPlayer wins!')
		
	elif player == 'Paper' and computer == 'Rock':
		outcome = 'win'
		print('\nPaper covers Rock!\nPlayer wins!')
		
	elif player == 'Scissors' and computer == 'Rock':
		outcome = 'loss'
		print('\nRock beats Scissors!\nComputer wins!')
	
	else:
		outcome = 'loss'
		print("You lost... -__-")
		
	# This if function records our wins,losses, and ties to our global variables
	if outcome == 'win':
		wins += 1
	elif outcome == 'lose':
		loss += 1
	else:
		ties += 1
	# Return the outcome
	return outcome
	
main()