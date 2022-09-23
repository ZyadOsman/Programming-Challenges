dictionary = {
    "JAN":"01",
    "FEB":"02",
    "MAR" :"03",
    "APR":"04",
    "MAY":"05",
    "JUN":"06",
   "JUL":"07",
    "AUG":"08",
    "SEP":"09",
    "OCT":"10",
    "NOV":"11",
    "DEC":"12",
    }
def splitdate():
    date = input("Enter date in the form dd-mmm-yy: ")
    split = date.split("-")
    return split


if __name__ == "__main__":
    x = splitdate()
    print(x)
    print(x[0])
    print(dictionary[x[1]])
    print(x[2])
    
    
