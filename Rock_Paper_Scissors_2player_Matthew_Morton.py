
p1 = input("Player 1 - Enter your name: ")
p1 = p1.title()
p2 = input("Player 2 - Enter your name: ")
p2 = p2.title()

p1_score = 0
p2_score = 0
game_on = True
print(f"Welcome, {p1.title()} and {p2.title()}! Let's get ready to play Rock, Paper, Scissors!")

while True:
	p1_action = input(f"{p1.title()} - Enter a choice: (rock, paper, or scissors): ")
	p2_action = input(f"{p2.title()} - Enter a choice: (rock, paper, or scissors): ")

	possible_actions = ["rock", "paper", "scissors"]


	print(f"\n{p1.title()} chose {p1_action}, {p2.title()} chose {p2_action}.\n")

	if p1_action == p2_action:
		print(f"Both players drew {p1_action}. It's a tie! Shoot again!")

	elif p1_action == "rock":
		if p2_action == "scissors":
			print(f"Rock crushes scissors! You win, {p1.title()}!")
			p1_score += 1
		else:
			print(f"Paper covers rock. You win, {p2.title()}!")
			p2_score += 1

	elif p1_action == "paper":
		if p2_action == "rock":
			print(f"Paper covers rock! You win {p1.title()}!")
			p1_score += 1
		else:
			print(f"Scissors cuts paper! You win, {p2.title()}!")
			p2_score += 1

	elif p1_action == "scissors":
		if p2_action == "paper":
			print(f"Scissors cuts paper! You win, {p1.title()}!")
			p1_score += 1
		else:
			print(f"Rock smashes scissors! You win, {p2.title()}!")
			p2_score += 1



	print("\n\t-----Score Board-----")
	print(f"\t{p1.title()}: {p1_score} <- | -> {p2.title()}: {p2_score}")	

	play_again = input("\nPlay again? (yes/no): ")
	if play_again.lower() != "yes":
		break
	
if p1_score > p2_score:
	print(f"\t\nYou won, {p1.title()}!! Let's play again sometime!")
elif p1_score == p2_score:
	print("It's a tie! Don't quit now... Settle the Score!")
	play_again = input("\nPlay again? (yes/no): ")
	if play_again.lower() != "yes":
		print("\t\nFine, quitters! It's a draw!")
else:
	print(f"\t\nYou won, {p2.title()}! Let's play again sometime!")


