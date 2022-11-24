def sentence():
    sentence = input("Enter the sentence you would like to encrypt:")
    return sentence
    
def encryption():
    key = int(input("Enter your key"))
    encrypted_sentence = ""
    encrypted_letter = ""
    for i in range(0, len(sentence)) :
        if sentence[i] == " ":
            encrypted_letter = " "
        elif sentence[i].islower():
            if ord(sentence[i]) + key <= 122:
                encrypted_letter = chr(ord(sentence[i]) + key)
            else:
                encrypted_letter = chr(97 + (ord(sentence[i]) + key) - 123) 
        elif sentence[i].isupper():
            if ord(sentence[i]) + key <= 90 :
                encrypted_letter = chr(ord(sentence[i]) + key)
            else:
                encrypted_letter = chr(65 + (ord(sentence[i]) + key) - 91)
        encrypted_sentence = encrypted_sentence + encrypted_letter
    return encrypted_sentence
        
        
if __name__ == "__main__":
    sentence = sentence()
    enc = encryption()
    print(enc)
    








    
    
