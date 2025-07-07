# if else
number = 1
fact = True


# basic if statement
if fact == True: # checks if "fact" is True
  print("True") # runs only if "fact" is True
print("complete") # runs regardless if "fact" is True or False


# basic if else statement
if fact == True: 
  print("True") 
if fact == False: 
  print("False") 
print("complete") 
# this is fine but use if else instead

# basic if else statement (proper)
if fact == True: # checks if "fact" is True
  print("True") # runs only if "fact" is True
else: # if "fact" is NOT true
  print("False") # runs only if "fact" is not True
print("complete") # runs regardless if "fact" is True or False


# elif
if number == 1:
  print("number is 1")
else:
  if number == 2:
    print("number is 2")
  else:
    if number == 3:
      print("number is 3")
    else:
      print("idk what number")
# this is fine but use elif instead


if number == 1:
  print("number is 1")
elif number == 2: # if number is not 1 and checks if number is 2
  print("number is 2") # wont run if number is 1
elif number == 3:
  print("number is 3")
else:
  print("idk what number")
  

# variable checking
a == b # a is equal to b
a > b # a is larger than b (if a = b then false)
a < b # a is smaller than b (if a = b then false)
a >= b # a is larger or equal to b
a <= b # a is smaller or equal to b
a != b # a is not equal to b

# special ones
c = [1,2,3]
a is b # same thing as a == b
a in c # checks if a is inside c
a not in c # checks if a is not inside c

# condition
a and b == 1 # checks if a == 1 and b == 1
a == 1 and b == 2 # checks if a == 1 and b == 2

a or b == 1 # checks if a == 1 or b == 1
a == 1 or b == 2 # checks if a == 1 or b == 2

not a == b # checks if a is not equal to b (same as a != b)


# nested if statements
if number == 1 and fact:
  print("number is 1")
elif number == 2 and fact:
  print("number is 2")
elif number == 3 and fact:
  print("number is 3")
else:
  print("idk what number")
# this is fine but if you wanna used nested if statements
if fact: # it checks if fact is true first
  if number == 1: # only runs this check if fact is true (note that)
    print("number is 1")
  elif number == 2:
    print("number is 2")
  elif number == 3:
    print("number is 3")
  else:
    print("idk what number")
else:
  print("fact is not true")
# if fact is false, the checks for the numbers is entirely skipped


# extra info
# for bool, u can simplify
if fact == True:
  print("truth")
# to
if fact:
  print("truth")


# for numbers,
if number != 0:
  print("not 0")
# to
if number:
  print("not 0")


# for string,
if string == "":
  print("string is empty")
# to
if string:
  print("string is empty")
