# Skeleton Program for the AQA AS Summer 2022 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0

import random

EMPTY_STRING = ""
SPACE = ' '
GRID_SIZE = 9

def ResetDataStructures():
  """
      Parameteres: None
      Return type: It is a function as it returns PuzzleGrid (2D array), Puzzle (1D array), Solution (1D array), Answer (1D array)
      Description: It empties out the values stored in the array
  """
  Puzzle = [EMPTY_STRING for Line in range(GRID_SIZE * GRID_SIZE)]
  PuzzleGrid = [[SPACE for Column in range(GRID_SIZE + 1)] for Row in range(GRID_SIZE + 1)]
  Solution = [EMPTY_STRING for Line in range(GRID_SIZE + 1)]
  Answer = [EMPTY_STRING for Line in range(2 * GRID_SIZE * GRID_SIZE)]
  return PuzzleGrid, Puzzle, Answer, Solution

def LoadPuzzleFile(PuzzleName, Puzzle):
  """
      Parameters: PuzzleName (String inputed by user), Puzzle (1D array)
      Return type: It is a function as it returns Puzzle (1D array) and OK (Boolean)
      Description: Uses the PuzzleName entered by user to read the file. Removes \n from end of each line (\n is ENTER). Loads the information from file into the Puzzle until the information is empty. If it doesn't enter the while loop, Line = 0 prints an error message.
  """  
  try:
    Line = 0
    FileIn = open(f"{PuzzleName}.txt", 'r')
    CellInfo = FileIn.readline()
    CellInfo = CellInfo[:-1]
    while CellInfo != EMPTY_STRING:
      Puzzle[Line] = CellInfo
      CellInfo = FileIn.readline()
      CellInfo = CellInfo[:-1]
      Line += 1
    FileIn.close()
    if Line == 0:
      print("Puzzle file empty")
      OK = False
    else:
      OK = True
  except:
    print("Puzzle file does not exist")
    OK = False
  return Puzzle, OK

def LoadSolution(PuzzleName, Solution):
  """
     Parameters: PuzzleName (String inputed by user), Solution (1D array)
     Return type: It is a function as it returns Solution (1D array) and OK (Boolean)
     Description: It reads puzzle1S which contains the solution to the puzzle. 
  """
  OK = True
  try:
    FileIn = open(f"{PuzzleName}S.txt", 'r')
    for Line in range(1, GRID_SIZE + 1):
      Solution[Line] = SPACE + FileIn.readline()
      Solution[Line] = Solution[Line][:-1]
      if len(Solution[Line]) != GRID_SIZE + 1:
        OK = False
        print("File data error")
    FileIn.close()  
  except:
    print("Solution file does not exist")
    OK = False
  return Solution, OK

def ResetAnswer(PuzzleName, Answer):
  """
     Parameters: PuzzleName (String inputed by user), Answer (1D array)
     Return type: It returns Answer, a 1D array which contains the name of the puzzle, your score, and the number of changes that you have made
     Description: It places an empty string instead of the changes that have been made 
  """
  Answer[0] = PuzzleName
  Answer[1] = "0"
  Answer[2] = "0"
  for Line in range(3, 2 * GRID_SIZE * GRID_SIZE):
    Answer[Line] = EMPTY_STRING
  return Answer

def TransferPuzzleIntoGrid(PuzzleName, PuzzleGrid, Puzzle, Answer):
  """
     Parameters: PuzzleName (String inputed by user), PuzzleGrid (2D array), Puzzle (1D array), Answer (1D array)
     Return Type: returns PuzzleGrid(2D array), Answer(1D array), OK (Boolean)
     Description: CellInfo[0] is the row. CellInfo[1] is the column. CellInfo[2] is the digit. Using these 3 digits, it is able to take the 3 integers contained in the file and place values in the puzzle grid accordingly.
  """
  OK = True
  try:
    Line = 0
    CellInfo = Puzzle[Line]
    while CellInfo != EMPTY_STRING:
      Row = int(CellInfo[0])
      Column = int(CellInfo[1])
      Digit = CellInfo[2]
      PuzzleGrid[Row][Column] = Digit
      Line += 1
      CellInfo = Puzzle[Line]
    PuzzleGrid[0][0] = 'X'
    Answer = ResetAnswer(PuzzleName, Answer)
  except:
    print("Error in puzzle file")
    OK = False
  return PuzzleGrid, Answer, OK

def LoadPuzzle(PuzzleGrid, Puzzle, Answer, Solution):
  """
     Parameters: PuzzleGrid (2D array), Puzzle (1D array), Answer (1D array), Solution (1D array)
     Return Type: returns PuzzleGrid (2D array), Puzzle (1D array), Answer (1D array), Solution (1D array)
     Description: Asks user to input name of puzzle. Runs LoadPuzzleFile which uses the PuzzleName entered by user to read the file. Runs LoadSolution which reads puzzle1S which contains the solution to the puzzle. Runs TransferPuzzleIntoGrid which is able to take the 3 integers contained in the file and place values in the puzzle grid accordingly. 
  """
  PuzzleGrid, Puzzle, Answer, Solution = ResetDataStructures()
  PuzzleName = input("Enter puzzle name to load: ")
  Puzzle, OK = LoadPuzzleFile(PuzzleName, Puzzle)
  if OK:
    Solution, OK = LoadSolution(PuzzleName, Solution)
  if OK:
    PuzzleGrid, Answer, OK = TransferPuzzleIntoGrid(PuzzleName, PuzzleGrid, Puzzle, Answer)
  if not OK:
    PuzzleGrid, Puzzle, Answer, Solution = ResetDataStructures()
  return PuzzleGrid, Puzzle, Answer, Solution

def TransferAnswerIntoGrid(PuzzleGrid, Answer):
  """
     Parameters: PuzzleGrid (2D array), Answer (1D array)
     Return type: returns PuzzleGrid (2D array)
     Description: Answer contains the number of changes, Answer[2], and all the changes done. This subroutine uses this to place the digits entered by user in the right row and column. 
  """
  for Line in range(3, int(Answer[2]) + 3):
    CellInfo = Answer[Line]
    Row = int(CellInfo[0])
    Column = int(CellInfo[1])
    Digit = CellInfo[2]
    PuzzleGrid[Row][Column] = Digit
  return PuzzleGrid

def LoadPartSolvedPuzzle(PuzzleGrid, Puzzle, Answer, Solution):
  """
     Parameters: PuzzleGrid (2D array), Puzzle (1D array), Answer (1D array), Solution (1D array)
     Return type: returns PuzzleGrid (2D array), Puzzle (1D array), Answer (1D array), Solution (1D array)
     Description: Opens partially solved puzzle. Takes the values placed in there and transfers it into grid by calling TransferAnswerIntoGrid.
  """
  PuzzleGrid, Puzzle, Answer, Solution = LoadPuzzle(PuzzleGrid, Puzzle, Answer, Solution)
  try:
    PuzzleName = Answer[0]
    FileIn = open(f"{PuzzleName}P.txt", 'r')
    CellInfo = FileIn.readline()
    CellInfo = CellInfo[:-1]
    if PuzzleName != CellInfo:
      print("Partial solution file is corrupt")
    else:
      Line = 0
      while CellInfo != EMPTY_STRING:
        Answer[Line] = CellInfo
        Line += 1
        CellInfo = FileIn.readline()
        CellInfo = CellInfo[:-1]
    FileIn.close()
    PuzzleGrid = TransferAnswerIntoGrid(PuzzleGrid, Answer)
  except:
    print("Partial solution file does not exist")
  return PuzzleGrid, Puzzle, Answer, Solution

def DisplayGrid(PuzzleGrid):
  """
     Parameters: PuzzleGrid (2D array)
     Return type: This is a procedure and does not return anything
     Description: Prints a series of numbers and symbols to display a PuzzleGrid to the user.
  """
  print()
  print("   1   2   3   4   5   6   7   8   9  ")
  print(" |===.===.===|===.===.===|===.===.===|")
  for Row in range(1, GRID_SIZE + 1):
    print(f"{Row}|", end='')    
    for Column in range(1, GRID_SIZE + 1):
      if Column % 3 == 0:
        print(f"{SPACE}{PuzzleGrid[Row][Column]}{SPACE}|", end='')
      else:
        print(f"{SPACE}{PuzzleGrid[Row][Column]}{SPACE}.", end='')
    print()
    if Row % 3 == 0:
      print(" |===.===.===|===.===.===|===.===.===|") 
    else:
      print(" |...........|...........|...........|")
  print()

def SolvePuzzle(PuzzleGrid, Puzzle, Answer):
"""
     Parameters: PuzzleGrid (2D array), Puzzle (1D array), Answer (1D array)
     Return type: returns PuzzleGrid (2D array) and Answer (1D array)
     Description: Allows user to enter the row, column, and digit of his desired answer, allows user to essentially solve the puzzle
"""
  CellInfoS = "0"
  DisplayGrid(PuzzleGrid)
  if PuzzleGrid[0][0] != 'X':
    print("No puzzle loaded")
  else:
    print("Enter row column digit: ")
    print("(Press Enter to stop)")
    CellInfo = input()
    while CellInfo != EMPTY_STRING:
      InputError = False
      if len(CellInfo) != 3:
        InputError = True
      else:
        Digit = CellInfo[2]
        try:
          Row = int(CellInfo[0])
        except:
          InputError = True
        try:
          Column = int(CellInfo[1])
        except:
          InputError = True
        if (Digit < '1' or Digit > '9'):
          InputError = True
        FileIn = open(f"{Answer[0]}.txt", 'r')
        CellInfoS = FileIn.readline()
        while CellInfoS != EMPTY_STRING:
          CellInfoS = CellInfoS[:-1]
          if CellInfoS[0] == CellInfo[0] and CellInfoS[1] == CellInfo[1]:
            InputError = True
        
      if InputError:
        print("Invalid input")
      else:
        PuzzleGrid[Row][Column] = Digit
        Answer[2] = str(int(Answer[2]) + 1)
        Answer[int(Answer[2]) + 2] = CellInfo
        DisplayGrid(PuzzleGrid)
      print("Enter row column digit: ")
      print("(Press Enter to stop)")
      CellInfo = input()
  
  return PuzzleGrid, Answer

def DisplayMenu():
"""
     Parameters: None 
     Return type: This is a procedure and doesnt return anything
     Description: Prints the Menu options for the user.
"""
  print()
  print("Main Menu")
  print("=========")
  print("L - Load new puzzle")
  print("P - Load partially solved puzzle")
  print("S - Solve puzzle") 
  print("C - Check solution")
  print("K - Keep partially solved puzzle")
  print("X - Exit") 
  print()

def GetMenuOption():
"""
     Parameters: None 
     Return type: Choice (1 letter String)
     Description: Allows user to enter their choice for the menu options
"""
  Choice = EMPTY_STRING
  while len(Choice) != 1:
    Choice = input("Enter your choice: ")
  return Choice[0]

def KeepPuzzle(PuzzleGrid, Answer):
"""
     Parameters: PuzzleGrid (1D array), Answer (1D array)
     Return type: This is a procedure and doesnt return anything
     Description: Allows user to keep his answers.
"""
  if PuzzleGrid[0][0] != 'X':
    print("No puzzle loaded")
  else:
    if int(Answer[2]) > 0:
      PuzzleName = Answer[0]
      FileOut = open(f"{PuzzleName}P.txt", 'w')
      for Line in range(int(Answer[2]) + 3):
        FileOut.write(Answer[Line])
        FileOut.write('\n')
      FileOut.close()
    else:
      print("No answers to keep")

def CheckSolution(PuzzleGrid, Answer, Solution):
"""
     Parameters: PuzzleGrid (2D array), Answer (1D array), Solution (1D array) 
     Return type: ErrorCount (Integer), Solved (Boolean)
     Description: Compares user's answers to SPACE (nothing) to check if incomplete and to Solution to check if correct.
"""
  ErrorCount = 0
  Solved = False
  Correct = True
  Incomplete = False
  for Row in range(1, GRID_SIZE + 1):
    for Column in range(1, GRID_SIZE + 1):
      Entry = PuzzleGrid[Row][Column]
      if Entry == SPACE:
        Incomplete = True
      if not (Entry == Solution[Row][Column] or Entry == SPACE):
        Correct = False
        ErrorCount += 1
        print(f"You have made an error in row {Row} column {Column}")
  if not Correct:
    print(f"You have made {ErrorCount} error(s)")
  elif Incomplete:
    print("So far so good, carry on")
  elif Correct:
    Solved = True
  return ErrorCount, Solved

def CalculateScore(Answer, ErrorCount):
"""
     Parameters: Answer (1D array), ErrorCount(Integer)
     Return type: Answer (1D array)
     Description: Calculates a score by minusing the number of errors from the amount of correct digits he has inputed into the puzzle
"""
  Answer[1] = str(int(Answer[1]) - ErrorCount)
  return Answer

def DisplayResults(Answer):
"""
     Parameters: Answer (1D array)
     Return type: This is a procedure and doesnt return anything.
     Description: Answer[1] is score. Answer[0] is the puzzle's name. Answer[Line] is the answer inputed by user. Checks if user made a start
"""
  if int(Answer[2]) > 0:
    print(f"Your score is {Answer[1]}")
    print(f"Your solution for {Answer[0]} was: ")
    for Line in range(3, int(Answer[2]) + 3):
      print(Answer[Line])
  else:
    print("You didn't make a start")

def NumberPuzzle():
"""
     Parameters: None
     Return type: This is a procedure and doesnt return anything
     Description: Start of the code (top of hierarchy chart). Executes subroutine depending on the user's input. Prints statements based on the score and prints 5 random statements depending on the user's input for menuoption (Nice one AQA you bunch of melons)
"""
  Finished = False
  PuzzleGrid, Puzzle, Answer, Solution = ResetDataStructures()
  while not Finished:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      PuzzleGrid, Puzzle, Answer, Solution = LoadPuzzle(PuzzleGrid, Puzzle, Answer, Solution)
    elif MenuOption == 'P':
      PuzzleGrid, Puzzle, Answer, Solution = LoadPartSolvedPuzzle(PuzzleGrid, Puzzle, Answer, Solution)
    elif MenuOption == 'K':
      KeepPuzzle(PuzzleGrid, Answer) 
    elif MenuOption == 'C':
      if PuzzleGrid[0][0] != 'X':
        print("No puzzle loaded")
      else:
        if int(Answer[2]) > 0:
          ErrorCount, Solved = CheckSolution(PuzzleGrid, Answer, Solution)
          Answer = CalculateScore(Answer, ErrorCount) 
          if Solved:
            print("You have successfully solved the puzzle")
            Finished = True
          else:
            print(f"Your score so far is {Answer[1]}")
        else:
          print("No answers to check")
    elif MenuOption == 'S':
        PuzzleGrid, Answer = SolvePuzzle(PuzzleGrid, Puzzle, Answer)
    elif MenuOption == 'X':
      Finished = True
    else:
      ResponseNumber = random.randint(1, 5)
      if ResponseNumber == 1:
        print("Invalid menu option. Try again")
      elif ResponseNumber == 2:
        print("You did not choose a valid menu option. Try again")
      elif ResponseNumber == 3:
        print("Your menu option is not valid. Try again")
      elif ResponseNumber == 4:
        print("Only L, P, S, C, K or X are valid menu options. Try again")
      elif ResponseNumber == 5:
        print("Try one of L, P, S, C, K or X ")
  if Answer[2] != EMPTY_STRING:
    DisplayResults(Answer)

if __name__ == "__main__":
  NumberPuzzle()
