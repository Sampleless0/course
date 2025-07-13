# for loops


# basic for loop
for i in range(1,6)
  print(i)
# expected:
# 1
# 2
# 3
# 4
# 5
# program ended.

# the "i" could be any variable
for number in range(1,6)
  print(number)
# expected:
# 1
# 2
# 3
# 4
# 5
# program ended.



# for loops using arrays
numbers = [1,10,100,1000]
for i in numbers:
  print(i)
print("complete")
# expected:
# 1
# 10
# 100
# 1000
# complete
# program ended.



# how to list numbers with items (important)
names = ['bruce', 'ashvin', 'brucevin']
for i in range(len(names)):
  print(f'{i+1}. {names[i]}')
print("complete")
# expected:
# 1. bruce
# 2. ashvin
# 3. brucevin
# complete
# program ended.



# range has 3 values range(start, stop, step)
# start means when to start
# stop means when to stop (it stops 1 before that number)
# step means how much it jumps between a loop (step of 3 means 3,6,9)
for i in range(1, 3):
  print(i)
# expected:
# 1
# 2
# program ended.


# start and stop can be negative
for i in range(-8, -2, 2):
  print(i)
# expected:
# -8
# -6
# -4
# program ended.


# step can be negative also
for i in range(3, 1, -1):
  print(i)
# expected:
# 3
# 2
# program ended.


# wont run if both start and stop is equal
for i in range(1, 1, 1):
  print(i)
# expected:
# program ended.


# works with variables too
number = 10
for i in range(1, number, 3):
  print(i)
# expected:
# 1
# 4
# 7
# program ended.
