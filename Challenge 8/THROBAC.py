dictionary = {
  "I":1,
  "V" : 5,
  "X" : 10,
  "L" : 50,
  "C" : 100,
}

def firstroman():
    firstnumber = input("Enter First Roman Number with no spaces: ")
    list_firstnumber = list(firstnumber)
    x = 0
    for i in list_firstnumber:
        j = dictionary[i]
        if j > dictionary[list_firstnumber[j-1]]:
            x = x + j
        else:
            x = x - j
    print(f"First roman number is equal to {x}")
    return x

def secondroman():
    secondnumber = input("Enter Second Roman Number with no spaces: ")
    list_secondnumber = list(secondnumber)
    y = 0
    for i in list_secondnumber:
        j = dictionary[i]
    if j > dictionary[list_secondnumber[j-1]]:
            y = y + j
    else:
            y = y - j
    print(f"Second roman number is equal to {y}")
    return y

if __name__ == "__main__":
    print(f"Both numbers added up is:{firstroman()} + {secondroman()} ")
    
