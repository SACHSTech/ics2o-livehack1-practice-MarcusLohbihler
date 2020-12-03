minutes = float(input("Insert number of minutes "))
days = (minutes / 1440 // 1.000)
hours = (minutes // 60)
print (str(days) + " days, " + str(hours) + " hours and " + str(minutes) + " minutes" )
