import sys
import random
def main():
	restart = 1
	while restart == 1:

		print("Prince of Persia game is starting")
		print("Game Rules: To choose room 1 press 1, room 2 press 2, for room 3 press 3")
		print("To proceed please make your choice: ")

		start()

		restart = int(input("Would you like to play again? Please enter '1' for YES or '2' for NO: "))
	print ("Thanks for playing!")

def room1():
	print("You are in room 1, you have to pass this test to proceed")
	print("You have to guess item order number from the list")
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
	print("room2")

def room3():
	print("room3")

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
