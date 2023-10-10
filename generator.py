import numpy as np
import sys

n = np.random.randint(5, 14)
limit = np.random.randint(n, min(80, 5*n))

file = open(sys.argv[1], "w")
file.write(str(n)+","+str(limit)+"\n")

randomly_generate = 0

board = np.zeros((n, n))

red_orient = 1

red_alley = np.random.randint(n)
red_start = np.random.randint(n-1)


file.write(str(red_alley)+","+str(red_start)+"\n")
board[red_alley][red_start] = 1
board[red_alley][red_start+1] = 1
	


	
for i in range(np.random.randint(2*n, 4*n)):
	orient = np.random.randint(2)
	alley = np.random.randint(n)
	start = np.random.randint(n-1)
	draw = np.random.randint(n)
	mine = 1 if draw == 0 else 0
	orient = orient + mine
	
	if orient == red_orient and alley == red_alley:
		continue
	
	if orient == 0:
		if randomly_generate == 0:
			if board[start][alley]+board[start + 1][alley] != 0:
				continue
		file.write(str(orient)+","+str(start)+","+str(alley)+"\n")
		board[start][alley] = 1
		board[start + 1][alley] = 1
	
	elif orient == 1:
		if randomly_generate == 0:
			if board[alley][start]+board[alley][start + 1] != 0:
				continue
		file.write(str(orient)+","+str(alley)+","+str(start)+"\n")
		board[alley][start] = 1
		board[alley][start+ 1] = 1
		
	else:
		row = np.random.randint(n)
		col = np.random.randint(n)
		if randomly_generate == 0:
			if board[row][col] != 0:
				continue
		file.write(str(orient)+","+str(row)+","+str(col)+"\n")
		board[row][col] = 1
		
	


file.close()
