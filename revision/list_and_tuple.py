# list and tuples


# list (values can be changed)
list = [1,'two',3.0,True]
# tuple (values cannot be changed)
tuple = (1,'two',3.0,True)



# reading lists (works with both list and tuple)
print(tuple)
print(list)
# expected:
# (1, 'two', 3.0, True)
# [1, 'two', 3.0, True]
# program ended.


item1 = tuple[0] # the 0 means 1st value
item2 = list[1] # the 1 means 2nd value
item3 = tuple[-1] # the -1 means last value
item4 = list[-2] # the -2 means 2nd last value
print(item1)
print(item2)
print(item3)
print(item4)
# expected:
# 1
# 'two'
# True
# 3.0
# program ended.



# slicing (works with both list and tuple)
tuple2 = tuple[0:2] # takes 1st and 2nd item [0] and [1]
list2 = list[1:3] # takes 2nd and 3rd item [1] and [2]
print(tuple2)
print(list2)
# expected:
# (1, 'two')
# ['two', 3.0]
# program ended.


# more specific
tuple3 = tuple[:2] # same as [0:2]
list3 = list[2:] # takes from 3rd item to the end of the list [2], [3] ...
print(tuple3)
print(list3)
# expected:
# (1, 'two')
# [3.0, True]
# program ended.




# .append() adds new value into the end of a list (tuple cannot be changed)
list.append(4)
print(list)
# expected:
# [1, 'two', 3.0, True, 4]
# program ended.



# .insert() adds new value into a specific spot in a list
list.insert(1, 'hello') # (1 is the spot between 1st and 2nd number, 'hello' is what to put between)
print(list)
# ecpected:
# [1, 'hello', 'two', 3.0, True, 4]
# program ended.



#
