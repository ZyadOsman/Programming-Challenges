def calculator():
    numbers = input("Enter your calculation: ")
    split = numbers.split()
    split0 = int(split[0])
    split1 = int(split[1])
    while numbers != "q":
      if split[2] == "+":
          x = split0 + split1
          print(x)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      elif split[2] == "-":
          y = split0 - split1
          print(y)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      elif split[2] == "*":
          z = split0 * split1
          print(z)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      elif split[2] == "/":
          a = split0 / split1
          print(a)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      elif split[2] == "//":
          b = split0 // split1
          print(b)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      elif split[2] == "%":
          c = split0 % split1
          print(c)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      elif split[2] == "**":
          d = split0 ** split1
          print(d)
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])
      else:
          print("Invalid operator. Please Try Again.")
          numbers = input("Enter your calculation: ")
          split = numbers.split()
          split0 = int(split[0])
          split1 = int(split[1])



if __name__ == "__main__":
    x = calculator()
