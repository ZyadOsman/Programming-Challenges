cardnum = input("ENTER YOUR CARD NUMBER")
cardnumdigit = cardnum.isdigit()
while len(cardnum) > 16:
    cardnum = input("Too long. ENTER YOUR CARD NUMBER")
while len(cardnum) < 16:
    cardnum = input("Too short. ENTER YOUR CARD NUMBER")
print("Valid card number entered.")

def task2():
    pan = cardnum[6:14]
    return pan
    
def task3():
    checkdigit = cardnum[15]
    return checkdigit

def luhn_checksum(cardnum):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(cardnum)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

#print('Valid') if luhn_checksum(cardnum)==0 else print('Invalid')
    

if __name__ == "__main__":
    print(task2())
    print(task3())
    if luhn_checksum(cardnum) == 0:
      print("VALID NUMBER ENTERED")
    else:
      print("INVALID")
