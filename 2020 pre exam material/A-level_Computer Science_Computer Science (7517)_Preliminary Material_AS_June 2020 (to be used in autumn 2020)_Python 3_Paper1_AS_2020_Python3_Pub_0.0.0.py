# Skeleton Program for the AQA AS1 Summer 2020 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0

EMPTY_STRING = ""
MAX_WIDTH = 100
MAX_HEIGHT = 100
import math
class FileHeader:
  def __init__(self):
    self.Title = EMPTY_STRING
    self.Width = MAX_WIDTH
    self.Height = MAX_HEIGHT
    self.FileType = EMPTY_STRING
def FindSecretChar(PixelValue, Key):
  Decryption = ""
  Number = PixelValue - Key
  if Number == 0:
    Decryption = " "
  elif Number == 1:
    Decryption = "A"
  elif Number == 2:
    Decryption = "B"
  elif Number == 3:
    Decryption = "C"
  elif Number == 4:
    Decryption = "D"
  elif Number == 5:
    Decryption = "E"
  elif Number == 6:
    Decryption = "F"
  elif Number == 7:
    Decryption = "G"
  elif Number == 8:
    Decryption = "H"
  elif Number == 9:
    Decryption = "I"
  elif Number == 10:
    Decryption = "J"
  elif Number == 11:
    Decryption = "K"
  elif Number == 12:
    Decryption = "L"
  elif Number == 13:
    Decryption = "M"
  elif Number == 14:
    Decryption = "N"
  elif Number == 15:
    Decryption = "O"
  elif Number == 16:
    Decryption = "P"
  elif Number == 17:
    Decryption = "Q"
  elif Number == 18:
    Decryption = "R"
  elif Number == 19:
    Decryption = "S"
  elif Number == 20:
    Decryption = "T"
  elif Number == 21:
    Decryption = "U"
  elif Number == 22:
    Decryption = "V"
  elif Number == 23:
    Decryption = "W"
  elif Number == 24:
    Decryption = "X"
  elif Number == 25:
    Decryption = "Y"
  elif Number == 26:
    Decryptipn = "Z"
  else:
    Decryption = "_"
  return Decryption

def CompressFile():
  count = 1
  FileName = input("Enter a file name: ")
  FileIn = open(FileName + ".txt", 'r')
  Header = FileIn.readline()
  Array = Header.split(",")
  Array[3] = "C"
  Header_String = Array[0]+","+ Array[1] + "," + Array[2] + "," + Array[3]
  FileOut = open("CMP" + FileName + ".txt", "w")
  FileOut.write(Header_String+"\n")
  Next_line = FileIn.readline()
  for i in range(0, len(Next_line) - 1):
    if Next_line[i] ==  Next_line[i+1]:
      count = count + 1
    else:
      FileOut.write(f"{count}, {Next_line[i]}")
      FileOut.write("\n")
      count = 1
    
    

def HorizontalFlip(Grid, Header):
  Mirror = Grid
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      if (Header.Width -  Column) >= Column:
        temporary = Mirror[Row][Column]
        Mirror[Row][Column] = Mirror[Row][Header.Width - Column-1]
        Mirror[Row][Header.Width - Column-1] = temporary

  print()
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width):
      print(Mirror[ThisRow][ThisColumn], end='')
    print()




def VerticalFlip(Grid, Header):
  Mirror = Grid
  for Column in range(Header.Width):
    for Row in range(Header.Height):
      if (Header.Height -  Row) >= Row:
        temporary = Mirror[Row][Column]
        Mirror[Row][Column] = Mirror[Header.Height - Row - 1][Column]
        Mirror[Header.Height - Row - 1][Column] = temporary

  print()
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width):
      print(Mirror[ThisRow][ThisColumn], end='')
    print()


def DoubleFlip(Grid, Header):




def DisplayError(ErrorMessage):
  """
   Parameters: string
   Description: it displays an error message
   """
  print("Error: ", ErrorMessage)

def PrintHeading(Heading):
  """
   Parameters: string
   Description: it prints heading and a line of equals
  """

  print(Heading)
  HeadingLength = len(Heading)
  for Position in range(1, HeadingLength + 1):
    print('=', end='')
  print()

def DisplayImage(Grid, Header):
  """
   Parameters: Grid is a list. Header is an object
   Description: it displays the image by printing symbols line at a time
"""

  print()
  PrintHeading(Header.Title)
  for ThisRow in range(Header.Height):
    for ThisColumn in range(Header.Width):
      print(Grid[ThisRow][ThisColumn], end='')
    print()

def SaveImage(Grid, Header):
  """
   Parameters: Grid is a list. Header is an object
   Description: It allows for the user to edit the title and save the file.
"""

  print("The current title of your image is: " + Header.Title)
  Answer = input("Do you want to use this as your filename? (Y/N) ")
  if Answer == "N" or Answer == "n":
    FileName = input("Enter a new filename: ")
  else:
    FileName = Header.Title
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
    FileOut.write('\n')
  FileOut.close()

def EditImage(Grid, Header):
  """
   Parameters: Grid is an array, header is an object
   Return type: it returns grid (grid is an array)
   Description: it allows the user to edit the image by replacing a symbol with a new symbol
"""

  DisplayImage(Grid, Header)
  Answer = EMPTY_STRING
  while Answer != "N":
    Symbol = EMPTY_STRING
    NewSymbol = EMPTY_STRING
    while len(Symbol) != 1:
      Symbol = input("Enter the symbol you want to replace: ")
    while len(NewSymbol) != 1:
      NewSymbol = input("Enter the new symbol: ")
    for ThisRow in range(Header.Height):
      for ThisColumn in range(Header.Width):
        if Grid[ThisRow][ThisColumn] == Symbol:
          Grid[ThisRow][ThisColumn] = NewSymbol
    DisplayImage(Grid, Header)
    Answer = input("Do you want to make any further changes? (Y/N) ")
  return Grid

def ConvertChar(PixelValue):
  """
   Parameters: integer
   Return type: it returns AsciiChar which is a string
   Description: it returns an ascii character depending on the pixel value.
"""

  if PixelValue <= 32:
    AsciiChar = '#'
  elif PixelValue <= 64:
    AsciiChar = '&'
  elif PixelValue <= 96:
    AsciiChar = '+'
  elif PixelValue <= 128:
    AsciiChar = ';'
  elif PixelValue <= 160:
    AsciiChar = ':'
  elif PixelValue <= 192:
    AsciiChar = ','
  elif PixelValue <= 224:
    AsciiChar = '.'
  else:
    AsciiChar = ' '
  return AsciiChar

def LoadGreyScaleImage(FileIn, Grid, Header):
  """
   Parameters: Fileln reads inside the file. Grid is an array. Header is an object.
   Return type: Returns the grid which is an array
   Description: It loads the greyscale image
"""
  Key = 0
  try:
    Decrypted_Message = ""
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        NextPixel = FileIn.readline()
        PixelValue = int(NextPixel)
        #Decrypted_Message = Decrypted_Message + FindSecretChar(PixelValue, Key)
        Grid[Row][Column] = ConvertChar(PixelValue)
  except:
    DisplayError("Image data error")
  
  return Grid

    
def LoadAsciiImage(FileIn, Grid, Header):
    
  """
   Parameters: Fileln reads inside the file. Grid is an array. Header is an object.
   Return type: returns the grid which is an array
   Description: it loads the ascii image
"""
  try:
    ImageData = FileIn.readline()
    NextChar = 0
    for Row in range(Header.Height):
      for Column in range(Header.Width):
        Grid[Row][Column] = ImageData[NextChar]
        NextChar += 1
  except:
    DisplayError("Image data error")
  return Grid

def LoadFile(Grid, Header):
  """
   Parameters: Fileln reads inside the file. Header is an object.
   Return type: returns the grid which is an array and the header which is an object
   Description: asks user to enter filename and checks if it exists. If not, it outputs an error message
"""
  FileFound = False
  FileTypeOK = False
  FileName = input("Enter filename to load: ")
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileFound = True
    HeaderLine = FileIn.readline()
    Fields = HeaderLine.split(',')
    Header.Title = Fields[0]
    Header.Width = int(Fields[1])
    Header.Height = int(Fields[2])
    Header.FileType = Fields[3]
    Header.FileType = Header.FileType[0]
    if Header.FileType == 'A':  
      Grid = LoadAsciiImage(FileIn, Grid, Header)
      FileTypeOK = True
    elif Header.FileType == 'G': 
      Grid = LoadGreyScaleImage(FileIn, Grid, Header)
      FileTypeOK = True
    FileIn.close()
    if not FileTypeOK:
      DisplayError("Unknown file type")
    else:
      DisplayImage(Grid, Header)
  except:
    if not FileFound:
      DisplayError("File not found")
    else:
      DisplayError("Unknown error")
  return Grid, Header

def SaveFile(Grid, Header):
  """
   Parameters:  Grid is an array. Header is an object.
   Description: it writes the file and saves it
"""
  FileName = input("Enter filename: ")
  FileOut = open(FileName + ".txt", 'w')
  FileOut.write(Header.Title + ',' + str(Header.Width) + ',' + str(Header.Height) + ',' + 'A' + '\n')
  for Row in range(Header.Height):
    for Column in range(Header.Width):
      FileOut.write(Grid[Row][Column])
  FileOut.close()

def ClearGrid(Grid):
  """
   Parameters: Grid is an array. 
   Return type: returns the grid which is an array
   Description: it creates a grid of dots. It outputs a cleargrid
"""
  for Row in range(MAX_HEIGHT):
    for Column in range(MAX_WIDTH):
      Grid[Row][Column] = '.'
  return Grid
   
def DisplayMenu():
  """
   Description: it displays the menu
"""
  print()
  print("Main Menu")
  print("=========")
  print("L - Load graphics file") 
  print("D - Display image")
  print("E - Edit image")
  print("S - Save image")
  print("X - Exit program")
  print("V - Mirror Image Vertically")
  print("H - Mirror Image Horizontally")
  print("B - Mirror Image in both directions")
  print("C - Compress Image")
  print()

def GetMenuOption():
  """
   Description: it allows the user to enter a letter in order to choose what option they want to use
"""
  MenuOption = EMPTY_STRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption
  
def Graphics():
  """
   Description: it runs getmenuoption() subroutine and then runs a subroutine based on the user input. It then allows the user to save the image as a graphics file
"""
  Grid = [['' for Column in range(MAX_WIDTH)] for Row in range(MAX_HEIGHT)]
  Grid = ClearGrid(Grid)
  Header = FileHeader()
  ProgramEnd = False
  while not ProgramEnd:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      Grid, Header = LoadFile(Grid, Header)
    elif MenuOption == "C":
      CompressFile()
    elif MenuOption == 'D':
      DisplayImage(Grid, Header)
    elif MenuOption == 'V':
      VerticalFlip(Grid, Header)
    elif MenuOption == 'H':
      HorizontalFlip(Grid, Header)
    elif MenuOption == "B":
      DoubleFlip(Grid, Header)
    elif MenuOption == 'E':
      Grid = EditImage(Grid, Header) 
    elif MenuOption == 'S':    
      SaveImage(Grid, Header)
    elif MenuOption == 'X':
      ProgramEnd = True
    else:
      print("You did not choose a valid menu option. Try again")
  print("You have chosen to exit the program")
  Answer = input("Do you want to save the image as a graphics file? (Y/N) ")
  if Answer == "Y" or Answer == "y":
    SaveFile(Grid, Header)
      
if __name__ == "__main__":
  Graphics()         
