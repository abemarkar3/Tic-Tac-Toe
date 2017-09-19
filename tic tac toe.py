import sys
import random
import time

markerT = 0
markerCheck = [1,2,3,4,5,6,7,8,9]
marker = [1,2,3,4,5,6,7,8,9]

# Show is a function to make it easier to print to console
def Show(x,y,z):
	print("{} | {} | {}".format(x,y,z))
	print("-----------")

#Use the Show function to print
Show(marker[0],marker[1],marker[2])
Show(marker[3],marker[4],marker[5])
Show(marker[6],marker[7],marker[8])

checker = 0
gameOver = False
def Turn():
	turn = random.randrange(0,100)
	if turn > 50:
		print('player 1 goes first')
		pT = 'x'
	if turn < 50:
		print('player 2 goes first')
		pT = 'o'
	if turn == 50:
		turn = random.randrange(0,100)	

def winCheckx(coor1,coor2,coor3):
	global marker
	if marker[coor1] == 'x' and marker[coor2] == 'x' and marker[coor3] == 'x':
		marker = [1,2,3,4,5,6,7,8,9]
		gameOver = True
		print('player 1 wins!')

def winChecky(coor1,coor2,coor3):
	global marker
	if marker[coor1] == 'o' and marker[coor2] == 'o' and marker[coor3] == 'o':
		marker = [1,2,3,4,5,6,7,8,9]
		gameOver = True
		print('player 2 wins!')

def DrawCheck():
	global markerCheck
	global marker
	global markerT
	markerCheck = list(markerCheck)
	marker = list(marker)
	for b in range(0,8):
		if marker[b] != markerCheck[b]:
			markerT += 1
		if markerT == 9:
			return 1



def Main():
	global marker
	global markerCheck

	turn = random.randrange(0,1)
	if turn == 1 :
		print("player 1's turn")
		pT = 'x'
	if turn == 0:
		print("player 2's turn")
		pT = 'o'
	while not gameOver:
		print(pT)
		markerSelect = input("In what number do you want to put: ")
		real = markerSelect-1
		marker[real] = pT

		Show(marker[0],marker[1],marker[2])
		Show(marker[3],marker[4],marker[5])
		Show(marker[6],marker[7],marker[8])


#       check if player 1 won 		
		winCheckx(0,1,2)
		winCheckx(0,4,8)
		winCheckx(0,3,6)
		winCheckx(1,4,7)
		winCheckx(2,5,8)
		winCheckx(2,4,6)
		winCheckx(6,7,8)
#       check if player 2 won 	
		winChecky(0,1,2)
		winChecky(0,4,8)
		winChecky(0,3,6)
		winChecky(1,4,7)
		winChecky(2,5,8)
		winChecky(2,4,6)
		winChecky(6,7,8)

#		drawCheck(coor)
		DrawCheck()
		if DrawCheck == 1:
			print('Its a Draw')
			marker = [1,2,3,4,5,6,7,8,9]


		Show(marker[0],marker[1],marker[2])
		Show(marker[3],marker[4],marker[5])
		Show(marker[6],marker[7],marker[8])

		if pT == 'x':
			pT = 'o'
		else:
			pT = 'x'

	print(gameOver)
	print("your game is over")

Main()
	