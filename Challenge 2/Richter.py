def userinput():
    richter = float(input("Enter Richter:"))
    return richter

def energy(richter):
    return 10**(1.5*richter+4.8)

def tnt():
    return energy(richter)/(4.184*10**9)

def output(richter):
    print(f"Richter value: {richter}")
    print(f"Joules: {energy(richter)}")
    print(f"TNT: {tnt()}")

if __name__ == "__main__":
    richter = userinput()
    output(richter)

