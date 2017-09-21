# Defining the initial grid used and assigning each grid value to "-"
grid = [list(range(8)), list(range(8)), list(range(8)), list(range(8)), list(range(8)), list(range(8)), list(range(8)), list(range(8))]
playerList = ["Player 1", "Player 2"]
counter =0
gridString = " | 0 \t 1\t 2\t 3\t 4\t 5\t 6\t 7\t\n"+"-"*(59)+"\n" # Horizontal axis headers 

# This is essentially to initialize the list with ' - '
for lists in grid:
    innerCounter = 0
    for items in lists:
        grid[counter][innerCounter] = " - "
        innerCounter+=1
    counter +=1

# Actual program implementation
def printGrid(gridString): # This functions edits the local gridString but leaves the initial one untouched
    verticalAxisCounter = 0 # The counter for the vertical axis numbering
    for lists in grid:
        gridString += str(verticalAxisCounter)+"|" # This adds an additional | to the vertical axis counter
        verticalAxisCounter +=1
        for items in lists:
            gridString += items+"\t"
        gridString+="\n"
    print(gridString)

# This function evaluates if a correct move is made
def evaluateIfCorrectMove(move, grid):
    blocksUnder=1
    if(grid[move[0]][move[1]] == " X " or grid[move[0]][move[1]] == " O "):
        return False
    while(move[0]+blocksUnder <= 7):
        if(grid[move[0]+blocksUnder][move[1]] == " - " ):
            return False
        else:
            blocksUnder+=1
    return True

# This function checks if person wins horizontally
def checkIfWinHorizontally(grid):
    matchesX = 0
    matchesO = 0
    for lists in grid:
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
    rowIndex =0
    columnIndex=0
    matchesX = 0
    matchesO = 0
    while(rowIndex < 8):
        check = grid[rowIndex][columnIndex]
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

        if(columnIndex == 7 and rowIndex ==7):
            break
        elif(rowIndex == 7):
            columnIndex+=1
            rowIndex=0
        rowIndex+=1
    return False

# Checks for top half of diangonal with positive slope
def checkIfWinDiagonally1(grid):
    initialColumnIndex=0
    initialRowIndex=4
    decrementedRowIndex = 4
    incrementedColumnIndex = 0
    matchesX = 0
    matchesO = 0
    counter =0
    while(incrementedColumnIndex <= 7 and decrementedRowIndex <=7):
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
            incrementedColumnIndex = 0
            matchesO = 0 # reset O counter when reading new line
            matchesX = 0 # reset X counter when reading new line
    return False
# For the second half of the positive slope diagonal
def checkIfWinDiagonally2(grid):
    # We start from [7][4] and move across till we get to [4][7] and the start again from [7][5]
    initialColumnIndex = 4
    incrementedColumnIndex = 4
    decrementedRowIndex = 7
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
        if(incrementedColumnIndex-7 > 0):
            counter+=1
            incrementedColumnIndex  = initialColumnIndex-counter
            decrementedRowIndex = 7
            matchesO = 0 # reset O counter when reading new line
            matchesX = 0 # reset X counter when reading new line

    return False 

def checkIfWinDiagonally3(grid):
    initialColumnIndex = 4
    initialRowIndex = 0
    incrementedColumnIndex = 4
    incrementedRowIndex = 0
    matchesO = 0
    matchesX = 0
    counter=0
    while(incrementedColumnIndex>=0):
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
        if(incrementedColumnIndex > 7):
            counter+=1
            incrementedColumnIndex = initialColumnIndex -counter
            incrementedRowIndex =0
            matchesO = 0 # reset O counter when reading new line
            matchesX = 0 # reset X counter when reading new line
    return False

def checkIfWinDiagonally4(grid):
    initialColumnIndex = 0
    initialRowIndex = 4
    incrementedRowIndex =4
    incrementedColumnIndex =0
    counter =0
    matchesX=0
    matchesO = 0
    while(incrementedRowIndex>=0 and incrementedColumnIndex >=0):
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
        if(incrementedRowIndex > 7):
            counter+=1
            incrementedRowIndex = initialRowIndex - counter
            incrementedColumnIndex = 0

    return False
input("Welcome to Connect Four, press ENTER to see the grid")
print()
printGrid(gridString)
inputtedString = input(playerList[0]+","+" enter your move in format xCoordinate, yCoordinate (e.g 2, 7) ")
splitString = inputtedString.split(",")
numOfPlays =0
while(inputtedString != "exit"):
    if(len(splitString) == 2 and (splitString[0].strip().isdigit() and int(splitString[0].strip())<=7) and (splitString[1].strip().isdigit() and int(splitString[1].strip())<=7 ) ):
        splitString[0] = splitString[0].strip()
        splitString[1] = splitString[1].strip()
        move = [int(splitString[1]), int(splitString[0])]
        if(evaluateIfCorrectMove(move, grid)):
            grid[int(splitString[1])][int(splitString[0])] = " X " if (numOfPlays%2 ==0) else " O "
            print()
            printGrid(gridString)

            if(checkIfWinHorizontally(grid) or checkIfWinVertically(grid) or checkIfWinDiagonally1(grid) or checkIfWinDiagonally2(grid) or checkIfWinDiagonally3(grid) or checkIfWinDiagonally4(grid)):
                break
            else:
                inputtedString = input(playerList[(numOfPlays+1)%2]+","+" enter your move in format xCoordinate, yCoordinate (e.g 2, 7) ")
                splitString = inputtedString.split(",")
                numOfPlays+=1
        else:
            inputtedString = input("You inputted an invalid move: please enter a correct coordinate in the format xCoordinate, yCoordinate (e.g 2, 7) ")
            splitString = inputtedString.split(",")
    else:
        inputtedString = input("You inputted an invalid string: please enter a correct coordinate in the format xCoordinate, yCoordinate (e.g 2, 7) ")
        splitString = inputtedString.split(",")
    