# type casting yay



x_int = 5 # integer 5

x_str = str(x_int) # '5' | int -> string
x_float = float(x_int) # 5.0 | int -> float
x_bool = bool(x_int) # True | int -> bool (any number is True except 0 which is False)



x_str = " " # string 'hello'

x_int = int(x_str) # NO | only works if the string is a integer (5.0 not accepted)
x_float = float(x_str) # NO | only works if the string is a number
x_bool = bool(x_str) # True | True if theres anything in the string, else false (spaces = True)



x_float = 5.0 # float 5.0

x_int = int(x_float) # 5 | rounds down to the nearest number (4.9 -> 4, -2.9 -> -2)
x_str = str(x_float) # '5.0' | float -> string
x_bool = bool(x_float) # True | 0.0 = False, else True



x_bool = True # bool True

x_int = int(x_bool) # 1 | converts True to 1, False to 0
x_str = str(x_bool) # 'True' | bool -> string
x_float = float(x_bool) # 1.0 | converts True to 1.0, False to 0.0

