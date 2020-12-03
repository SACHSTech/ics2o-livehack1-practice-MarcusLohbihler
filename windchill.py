temperature = float(input("Insert temperature (celsius) "))
wind_speed = float(input("Insert wind speed here "))
windchill = (13.12 + (0.6215 * temperature) - (11.37 * wind_speed**0.16) + (0.3965 * temperature * wind_speed**0.16))
print ("The windchill factor is " + str(windchill))