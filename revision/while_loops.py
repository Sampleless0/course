# while loops

# while loops
while True:
  print("will repeat forever")


state = False
while state:
  print("will only run and repeat if state is True")

while state == False:
  print("will only run and repeat if state is False")


number1 = 0
number2 = 10
while number1 < number2:
  print("will repeat until number1 = or > number2")

while number1 < number2:
  number1 += 1
  print("will repeat about 10 times")



# break and continue (important)
while True:
  print("this will only run once cuz break stops the loop (regardless of loop condition)")
  break
# expected print result:
# this will only run once cuz break stops the loop (regardless of loop condition)
# program ended.


while True:
  print("this will run repeatedly")
  continue
  print("this will never run cuz continue restarts the loop (start from start again) but continues running")
# expected print result:
# this will run repeatedly
# this will run repeatedly
# this will run repeatedly
# ...



# how to use this info

# counter
number = 0
while True:
  number += 1
  print(f'number is {number}')
# expected print result:
# number is 1
# number is 2
# number is 3
# ...


# print only all even numbers
number = 0
while number 0 <= 1000
  number += 1
  if number % 2 == 0:
    print(f"number is {number}")
# expected print result:
# number is 2
# number is 4
# number is 6
# ...
# number is 998
# number is 1000
# program ended.


# input checker
while True:
  age = input("what is ur age --> ")
  # checks for isdigit()
  if age.isdigit():
    # if number is a number
    print(f"age inputted is {age}")
    break # stops loop
  else:
    # if number is not a number
    print("must input a number")
    continue # repeats loop
  print("this will never run")
  
# expected print result:
  
# what is ur age --> bruce
# must input a number
  
# what is ur age --> 69
# age inputted is 69
  
# program ended.
