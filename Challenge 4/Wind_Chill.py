def airtemp():
    air_temp = float(input("Enter AIR TEMPERATURE: "))
    return air_temp

def windspeed():
    wind_spd = float(input("Enter WAVE SPEED: "))
    return wind_spd

def calculations(airtemp, windspeed):
     windchill = 35.74+0.6215*airtemp-35.75*windspeed**0.16+0.4275*airtemp*windspeed**0.16
     return windchill

if __name__ == "__main__":
    airtemp = airtemp()
    windspeed = windspeed()
    windchill = calculations(airtemp, windspeed)
    print (f"Windchill: {windchill}")
    
