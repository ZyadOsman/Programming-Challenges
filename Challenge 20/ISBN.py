dictionary ={
    "0": 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "X" : 10
    }






def isbn_length():
    isbn = input("Enter an ISBN")
    while len(isbn) != 10 or isbn.isdigit() == False:
        isbn = input("Invalid, Enter an ISBN")
    return isbn

def addition(isbn):
    n = 10
    isbn_addition = 0
    for i in range(0, 10):
        isbn_addition = isbn_addition + (dictionary[isbn[i]]*n)
        n = n - 1
    return isbn_addition

def mod(addition):
    
        
    



if __name__ == "__main__":
    isbn = isbn_length()
    addition = addition(isbn)
    
    
        
