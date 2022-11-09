vowels = ["a", "e", "i", "o", "u"]

def  input_string():
    S = str(input("Enter a string: "))
    while S.isalpha() == False:
        S = str(input("Invalid string"))
    S = S.upper()
    return S

def dictionary(S):
        z = 0
        n = 0
        this_dict= {}
        substring = S[n]
        while n <= (len(S) - 1):
                    if substring in this_dict:
                        a = S[n]
                        b = S[n+1]
                        substring = a + b
                    else:
                        this_dict[substring] = z
                        z = z+1
                    n = n + 1
              
        print (this_dict)



        
            
            
            
             


if __name__ == "__main__":
    S = input_string()
    dictionary(S)

