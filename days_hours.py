hours = float(input("Insert number of hours "))
days = (hours / 24 // 1.000)
total_hours = (hours % 24)
print (str(days) + " days and " + str(total_hours) + " hours" )