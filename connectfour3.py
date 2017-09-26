# Defining the initial grid used and assigning each grid value to "-"

input("Welcome to Connect Four, press ENTER to create your grid ")
columns = input("Please input the number of columns (4 or more): ")

while not (columns.isdigit() and int(columns)>=4):
    columns = input("You inputted and invalid number of columns, please input a valid number: ")

rows = input("Please input the number of rows (4 or more): ")
while not (rows.isdigit() and int(rows)>=4):
    rows = input("You inputted and invalid number of rows, please input a valid number: ")

grid = [[" - " for x in range(int(columns))] for y in range(int(rows))] 
playerList = ["Player 1", "Player 2"]
counter =0
gridString = "" # Horizontal axis headers 
for (index, lists) in enumerate(grid[0]):
    gridString += " "+str(index)+"\t"
gridString+="\n"+"-"*((8*(len(grid[0])-1))+3)+"\n"

# Actual program implementation
def printGrid(gridString): # This functions edits the local gridString but leaves the initial one untouched
    for lists in grid:
        for items in lists:
            gridString += items+"\t"
        gridString+="\n"
    print(gridString)

# This function checks if person wins horizontally
def checkIfWinHorizontally(grid):
    for lists in grid:
        matchesO = 0 # Resets matches on new rows
        matchesX = 0
        for items in lists:
            if(items == " X "):
                matchesX += 1 # Increase matches if finds X
                matchesO = 0 # Return O count to 0 because it means O is not continuous
            elif(items == " O "):
                matchesO += 1
                matchesX = 0
            else:
                matchesO = 0 # Return both to 0 because it indicates no continuity
                matchesX = 0
            if(matchesX == 4):
                print("Player 1 has won \n GAME OVER")
                return True
            elif(matchesO == 4):
                print("Player 2 has won \n GAME OVER")
                return True

    return False  

def checkIfWinVertically(grid):
    matchesX = 0
    matchesO = 0
    counter = 0
    while counter< len(grid[0])-1:
        matchesX = 0
        matchesO = 0
        for rows in grid:
            check = rows[counter]
            if(check == " X "):
                matchesX += 1 # Increase matches if finds X
                matchesO = 0 # Return O count to 0 because it means O is not continuous
            elif(check == " O "):
                matchesO +=1
                matchesX = 0
            else:
                matchesO = 0
                matchesX = 0
        
            if(matchesX == 4):
                print("Player 1 has won \n GAME OVER")
                return True

            elif(matchesO == 4):
                print("Player 2 has won \n GAME OVER")
                return True
        counter+=1
    return False

def checkIfWinDiagonally1(grid):
    initialColumnIndex=0
    initialRowIndex=len(grid)-4
    decrementedRowIndex = 4
    incrementedColumnIndex = 0
    matchesX = 0
    matchesO = 0
    counter =0
    while(incrementedColumnIndex <= (len(grid[0])-1) and decrementedRowIndex <= (len(grid)-1)):
        check = grid[decrementedRowIndex][incrementedColumnIndex]
        
        if(check == " X "):
            matchesX += 1 # Increase matches if finds X
            matchesO = 0 # Return O count to 0 because it means O is not continuous

        elif(check == " O "):
            matchesO +=1
            matchesX = 0

        else:
            matchesO = 0
            matchesX = 0
        
        if(matchesX == 4):
            print("Player 1 has won \n GAME OVER")
            return True

        elif(matchesO == 4):
            print("Player 2 has won \n GAME OVER")
            return True

        decrementedRowIndex -=1
        incrementedColumnIndex+=1

        if(decrementedRowIndex < 0):
            counter+=1
            decrementedRowIndex = initialRowIndex+counter
            incrementedColumnIndex = initialColumnIndex
            matchesO = 0 # reset O counter when reading new line
            matchesX = 0 # reset X counter when reading new line
    return False
# For the second half of the positive slope diagonal


def checkIfWinDiagonally2(grid):
    # We start from [7][4] and move across till we get to [4][7] and the start again from [7][5]
    initialColumnIndex = len(grid[0])-4
    initialRowIndex = len(grid)-1
    incrementedColumnIndex = len(grid[0])-4
    decrementedRowIndex = len(grid)-1
    matchesX = 0
    matchesO = 0
    counter=0
    while(incrementedColumnIndex >=0):
        check = grid[decrementedRowIndex][incrementedColumnIndex]
        if(check == " X "):
            matchesX += 1 # Increase matches if finds X
            matchesO = 0 # Return O count to 0 because it means O is not continuous

        elif(check == " O "):
            matchesO +=1
            matchesX = 0

        else:
            matchesO = 0
            matchesX = 0
        
        if(matchesX == 4):
            print("Player 1 has won \n GAME OVER")
            return True

        elif(matchesO == 4):
            print("Player 2 has won \n GAME OVER")
            return True

        decrementedRowIndex -=1
        incrementedColumnIndex +=1
        if(incrementedColumnIndex > len(grid[0])-1):
            counter+=1
            incrementedColumnIndex  = initialColumnIndex-counter
            decrementedRowIndex = initialRowIndex
            matchesO = 0 # reset O counter when reading new line
            matchesX = 0 # reset X counter when reading new line

    return False 


# Check if  a win is present diagonally (negative slope) from [0][4] to [0][0]
def checkIfWinDiagonally3(grid):
    initialColumnIndex = len(grid[0])-4
    initialRowIndex = 0
    incrementedColumnIndex = len(grid[0])-4
    incrementedRowIndex = 0
    matchesO = 0
    matchesX = 0
    counter=0
    while(incrementedColumnIndex>=0 and incrementedRowIndex>=0 and incrementedColumnIndex<len(grid[0]) and incrementedRowIndex<len(grid)):
        check = grid[incrementedRowIndex][incrementedColumnIndex]
        if(check == " X "):
            matchesX += 1 # Increase matches if finds X
            matchesO = 0 # Return O count to 0 because it means O is not continuous

        elif(check == " O "):
            matchesO +=1
            matchesX = 0

        else:
            matchesO = 0
            matchesX = 0
        
        if(matchesX == 4):
            print("Player 1 has won \n GAME OVER")
            return True

        elif(matchesO == 4):
            print("Player 2 has won \n GAME OVER")
            return True

        incrementedRowIndex+=1
        incrementedColumnIndex+=1
        if(incrementedColumnIndex > len(grid[0])-1):
            counter+=1
            incrementedColumnIndex = initialColumnIndex -counter
            incrementedRowIndex = initialRowIndex
            matchesO = 0 # reset O counter when reading new line
            matchesX = 0 # reset X counter when reading new line
    return False

def checkIfWinDiagonally4(grid):
    initialColumnIndex = 0
    initialRowIndex = len(grid)-4
    incrementedRowIndex = len(grid)-4
    incrementedColumnIndex =0
    counter =0
    matchesX=0
    matchesO = 0
    while(incrementedRowIndex>=0 and incrementedColumnIndex >=0 and incrementedColumnIndex<len(grid[0]) and incrementedRowIndex<len(grid)): 
        check = grid[incrementedRowIndex][incrementedColumnIndex]

        if(check == " X "):
            matchesX += 1 # Increase matches if finds X
            matchesO = 0 # Return O count to 0 because it means O is not continuous

        elif(check == " O "):
            matchesO +=1
            matchesX = 0

        else:
            matchesO = 0
            matchesX = 0
        
        if(matchesX == 4):
            print("Player 1 has won \n GAME OVER")
            return True

        elif(matchesO == 4):
            print("Player 2 has won \n GAME OVER")
            return True

        incrementedRowIndex+=1
        incrementedColumnIndex+=1
        if(incrementedRowIndex > len(grid)-1):
            counter+=1
            incrementedRowIndex = initialRowIndex - counter
            incrementedColumnIndex = 0

    return False


def getLastIndex(column, grid):
    for rowIndex, rows in enumerate(grid[::-1]):
        if(rows[column] == " - "):
            return [len(grid)-1- rowIndex]
    print("Out of rows ")
    return False


print()
print("Your grid is displayed below, if at any time during the course of the game, you want to exit, type 'exit' \n")
printGrid(gridString)
inputtedString = input(playerList[0]+","+" enter the column in which you'd like to place your move: ")
numOfPlays =0
while(inputtedString != "exit"):
    if(inputtedString.strip().isdigit() and int(inputtedString.strip())<len(grid[0]) and getLastIndex(int(inputtedString.strip()), grid)):
        move = int(inputtedString)
        grid[getLastIndex(move, grid)[0]][move] = " X " if (numOfPlays%2 ==0) else " O "
        print()
        printGrid(gridString)
        if(checkIfWinHorizontally(grid) or checkIfWinVertically(grid) or checkIfWinDiagonally1(grid) or checkIfWinDiagonally2(grid) or checkIfWinDiagonally3(grid) or checkIfWinDiagonally4(grid)):
                break
        else:
            inputtedString = input(playerList[(numOfPlays+1)%2]+","+" enter a column to play your move: ")
            print()

    else:
        inputtedString = input("You inputted an invalid move: please enter a correct column: ")
    numOfPlays+=1





