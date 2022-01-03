board = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

def solve(bo):
	find = find_empty(bo)

	if not find:
		return True # Solution found.
	else:
		row, col = find

	for i in range(1, 10): # Loop through 1 and 9 inclusively.
		if valid(bo, i, (row, col)): # If number is valid: Add it to board.
			bo[row][col] = i

			if solve(bo): # Keep trying to find solution
				return True

			bo[row][col] = 0
	
	return False

def valid(bo, num, pos):
	# Check row.
	for i in range(len(bo[0])): # Check through each column. See if equal to the number added in.
		if bo[pos[0]][i] == num and pos[1] != i: # If position checking is same as inserted number: Don't check it.
			return False

	# Check column.
	for i in range(len(bo)):
		if bo[i][pos[1]] == num and pos[0] != i:
			return False

	# Check each box.
	box_x = pos[1] // 3 # // = Integer division (0, 1, or 2)
	box_y = pos[0] // 3 # (0, 1, or 2)

	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x * 3 + 3):
			if bo[i][j] == num and (i, j) != pos:
				return False

	return True

def print_board(bo): # bo = board
	for i in range(len(bo)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - -") # Every third row: Print a separator line.

		for j in range(len(bo[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end="") # Prints horizontal separator line.
			if j == 8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j) # Row, column.

	return None # If no squares = 0, return None. Triggers solve(bo).

print("---------NEW BOARD---------")
print_board(board)
solve(board)
print("---------SOLVED BOARD---------")
print_board(board)