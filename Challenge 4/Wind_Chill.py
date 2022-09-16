air_temp = float(input("Enter AIR TEMPERATURE: "))
wind_spd = float(input("Enter WAVE SPEED: "))

def calculations():
     windchill = 35.74+0.6215*air_temp-35.75*wind_spd**0.16+0.4275*air_temp*wind_spd**0.16
     return windchill

if __name__ == "__main__":
    windchill = calculations()
    print (f"Windchill: {windchill}")
