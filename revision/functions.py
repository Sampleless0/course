# functions


# built in functions
print() # print a result
len() # returns length of string, list or tuple
type() # finds the type of variable (bool, int, string etc)
range() # from a number to another number
input() # user type in smt



# write new function
def function_name():
  print("it ran")

# run the function
function_name()
# expected:
# it ran
# program ended.



# u can run functions inside other functions
def main():
  print('imma run a function')
  # running function inside function
  ifailedSMA()

# other function
def ifailedSMA():
  print('i love mechanics')

# run main
main()
# expected:
# imma run a function
# i love mechanics
# program ended.





# variables (important)
# local varibles
number = 0

def no1():
  number = 10 # this number does NOT affect the main number variable (local variable)

def no2():
  number = 20 # this number does NOT affect the main number variable (local variable)

no1()
no2()
print(number)
# expected:
# 0
# program ended.



# this is cuz the number outside the function is different from the one inside the function
# to fix this
number = 0

def no1():
  global number # calls in the main "number" variable
  number = 10

def no2():
  global number # calls in the main "number" variable
  number = 20

no1()
no2()
print(number)
# expected:
# 20
# program ended.

# while it works, it is not recommended as it is difficult to debug if something goes wrong



# understanding arguments and return (very very important must know)
number = 1

def addition(numberToAdd): # (this contains a variable (any))
  newNumber = numberToAdd += 1
  return newNumber # this makes the function output a value (eg. when u int(a variable) it returns an int)

output = addition(number) # this sets output to number + 1
print(output)
# expected:
# 2
# program ended.



# arguments with multiple variables
def add(first, second): # this asks for 2 variables (any type)
  return first + second # sends back the addition of both variables inputted

print(add(10, 5))
print(add(5, 3))
print(add(2, 1))
# expected:
# 15
# 8
# 3
# program ended.



# returning multiple values
def timesTable(number):
  return number, number*2, number*3 # this returns a tuple of (number, number times 2, number times 3)

print(timesTable(1))
print(timesTable(3))
print(timesTable('hello'))
# expected:
# (1, 2, 3)
# (3, 6, 9)
# ('hello', 'hellohello', 'hellohellohello')
# program ended.



# how to use this info
number = 10

def add10(add):
  return add + 10

def sub10(sub):
  return sub - 10

def multi(times):
  return times, times*10, times*100

def divide(number, number2):
  return number / number2

print(add10(number))
print(sub10(number))
print(multi(number))
print(divide(number, 2))
# expected:
# 20
# 0
# (10, 100, 1000)
# 5.0
# program ended.
