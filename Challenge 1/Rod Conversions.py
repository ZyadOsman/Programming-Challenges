def rods_to_metres (rods):
    return rods*5.0292

def metres_to_feet (rods):
    return rods_to_metres(rods)/0.3048

def metres_to_miles (rods):
    return rods_to_metres(rods)/1609.34

def rods_to_furlongs (rods):
    return rods/40

def time (rods):
    walking_speed = 3.1/60
    return metres_to_miles(rods)/walking_speed

def user_input():
    rods = float(input("Enter distance in rods:"))
    print(f"You input {rods} rods")
    print("Here are the conversions:")
    return rods

def output(rods):
    print(f"{rods_to_metres(rods)} metres")
    print(f"{metres_to_feet(rods)} feet")
    print(f"{metres_to_miles(rods)} miles")
    print(f"{rods_to_furlongs(rods)} furlongs")
    print(f"{time (rods)} minutes to walk {rods} rods")



if __name__ == "__main__":
    rods = user_input()
    output(rods)









