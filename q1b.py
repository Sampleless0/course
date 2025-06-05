def day(o):
    if o == "monday":
        return "lunes"
    elif o == "tuesday":
        return "martes"
    elif o == "wednesday":
        return "miercoles"
    elif o == "thursday":
        return "jueves"
    elif o == "friday":
        return "viernes"
    elif o == "saturday":
        return "sabado"
    elif o == "sunday":
        return "domingo"
    else:
        return "that is not a valid day of the week"

print(day(input("gib me day -> ").lower()))
