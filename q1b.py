# get input
day = input("gib me day -> ").lower()
result = ""

# if else
if day == "monday":
    result = "lunes"
elif day == "tuesday":
    result = "martes"
elif day == "wednesday":
    result = "miercoles"
elif day == "thursday":
    result = "jueves"
elif day == "friday":
    result = "viernes"
elif day == "saturday":
    result = "sabado"
elif day == "sunday":
    result = "domingo"
else:
    result = "that is not a valid day of the week"

# print result
print(result)
