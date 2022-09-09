rods = float(input("Enter distance in rods:"))
print("You input", rods, "rods")
print("Here are the conversions:")
meters = rods*5.0292
feet = meters/0.3048
miles = meters/1609.34
furlongs = rods/40
speed = 3.1/60
time = miles/speed
print(meters, "metres")
print(feet, "feet")
print(miles, "miles")
print(furlongs, "furlongs")
print(time, "minutes to walk", rods, "rods")


