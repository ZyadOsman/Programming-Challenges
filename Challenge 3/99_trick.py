def your_part():
    answer = int(input("YOUR TURN. Enter a number between 10 and 49: "))
    while answer > 49 or answer < 10:
        answer = int(input("Invalid number entered. Please try again: "))
    factor = 99 - answer
    return factor

def friend_part():
    friendnum = int(input("FRIEND'S TURN. Enter a number between 50 and 99: "))
    while friendnum > 99 or friendnum < 50:
        friendnum = int(input("Invalid number entered. Please try again: "))
    return friendnum

def calculations(factor, friendnum):
    addition = (factor + friendnum) - 100
    subtraction = friendnum - (addition + 1)
    return subtraction

if __name__ == "__main__":
    factor = your_part()
    friendnum = friend_part()
    sub = calculations(factor, friendnum)
    print (f"the calculation result was {sub}")
    
                 
