import sys
import random
def main():
	restart = 1
	while restart == 1:

		print("Prince of Persia game is starting")
		print("""Game Rules: You have to pass 3 rooms to finish the game.
		\nTo start from room 1 press 1, room 2 press 2, for room 3 press 3""")
		print("To proceed please make your choice: ")

		start()

		restart = int(input("Would you like to play again? Please enter '1' for YES or '2' for NO: "))
	print ("Thanks for playing!")

def room1():
	print("\n\nYou are in room 1")
	print("Here's your challenge: You have to guess item order number from the list")
	colorList = ["Red", "Blue", "Green", "White", "Black"]
	print(colorList)
	randomChoise = (random.choice(colorList))
	print (f"""what is the index number of '{randomChoise}' in the list above""")
	room1Answer = int(input(">"))
	room1Index = 1 + int(colorList.index(randomChoise))
	print(room1Index)
	if room1Answer == room1Index:
		room2()
	else:
		dead()

def room2():
	rangeStep = random.randint(1,10)
	print ("\n\nYou are in room 2")
	print ("Here's your challenge: You have too gues step of arithmetic progression")
	for i in range(1,30,rangeStep):
		print(i, end = ' ')
	room2Answer = int(input("\nEnter your answer here: "))
	if room2Answer == rangeStep:
		room3()
	else:
		dead()

def room3():
	print("\n\nYou are in room 3")
	print("""Here's your challenge: You have to pass labyrinth.
	\nEach time when prompted you have to choose how many steps to go forward, left or right.
	\nMax steps count that you can choose for one move is 6""" )
	temp1Steps=[]
	f1Steps = 3
	while sum(temp1Steps) < f1Steps:
		tempSteps=int(input("How many steps to go forward?\n>"))
		temp1Steps.append(int(tempSteps))
	if sum(temp1Steps) == f1Steps:
		pass
	else:
		print ("Game Over! Your have been burned")
		exit(0)

	temp2Steps=[]
	f2Steps = 4
	while sum(temp2Steps) < f2Steps:
		tempSteps=int(input("You turned left, how many steps to go?\n>"))
		temp2Steps.append(tempSteps)
	if sum(temp2Steps) == f2Steps:
		pass
	else:
		print ("Game Over! You fell of from Clif")
		exit(0)

	temp3Steps=[]
	f3Steps = 6
	while sum(temp3Steps) < f3Steps:
		tempSteps=int(input("You turned right, how many steps to go?\n>"))
		temp3Steps.append(tempSteps)
	if sum(temp3Steps) == f3Steps:
		pass
	else:
		print ("Game Over! Your foot sliped and you fell on deadly snake")
		exit(0)

	temp4Steps=[]
	f4Steps = 4
	while sum(temp4Steps) < f4Steps:
		tempSteps=int(input("You turned right, how many steps to go?\n>"))
		temp4Steps.append(tempSteps)
	if sum(temp4Steps) == f4Steps:
		print("Congradulations you won the game!\n\n\n")
		main()
	else:
		print ("Game Over! Your foot sliped and you fell on deadly snake")
		exit(0)

def dead():
	print("You'r dead! Wrong Choice")

def start():
	startChoice = int(input())

	if startChoice == 1:
		room1()
	elif startChoice == 2:
		room2()
	elif startChoice == 3:
		room3()
	else:
		dead()

main()
