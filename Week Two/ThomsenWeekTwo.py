import random

# Global variables for the grid size as well as the number of ships
grid_size = 10
num_ships = 5

# Function to print the board that loops through each row and column for (grid_size) amount of times to add the number headers
def drawBoard(myBoard):
    print("  " + " ".join(str(i) for i in range(grid_size)))
    for i in range(grid_size):
        print(str(i) + " " + " ".join(myBoard[i]))

# Function to set up the board. Randomize location of the ships, then replace the . with an S, then loop for (num_ships) amount of times
# The template has this function using (myBoard) as well as an input, but I did not end up doing it this way
def setupBoard():
    board = [['.'] * grid_size for _ in range(grid_size)]
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if board[row][col] == '.':
            board[row][col] = '\033[34mS\033[0m'
            ships_placed += 1
    return board

# Function to check board (name changed from checkHitorMiss() to keep with naming scheme)
# Takes in the board, as well as the row and column from the user and checks if there is/was a ship, then changes to an X, or if there is nothing, report a miss
def checkBoard(myBoard, row, col):
    if myBoard[row][col] == '\033[34mS\033[0m':
        myBoard[row][col] = '\033[31mX\033[0m'
        return "\033[32mHIT\033[0m\n"
    elif myBoard[row][col] == '\033[31mX\033[0m':
        return "\033[32mHIT\033[0m\n"
    else:
        myBoard[row][col] = 'O'
        return "\033[31mMISS\033[0m\n"

# Function to check if there are any ships left. Checks each row and column for any ships (S).         
def isGameOver(board):
    for row in board:
        if '\033[34mS\033[0m' in row:
            return False
    return True

# Main function
# Creates the board, then continues to loop while the isGameOver() is false. Once it is true, the loop ends as does the game. 
# Asks for user input, the function checks if this is a valid input, then the pair of inputs is checked using the checkBoard() function. Finally, the game state is checked to see if the game ends. 
def main():
    board = setupBoard()
    while not isGameOver(board):
        drawBoard(board)
        try:
            col = int(input("\033[35mEnter column (X): \033[0m"))
            if col < 0 or col >= grid_size:
                print("Invalid column")
                continue
            row = int(input("\033[35mEnter row (Y): \033[0m"))
            if row < 0 or row >= grid_size:
                print("Invalid row")
                continue
        except ValueError:
            print("Invalid input try again.")
            continue
        result = checkBoard(board, row, col)
        print(result)
    drawBoard(board)
    print("\033[33mYOU WIN!! GAME OVER!\033[0m")

# Run the main func
if __name__ == '__main__':
    main()

