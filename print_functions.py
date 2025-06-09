# print functions lol

print('hello world') # ' ' single quote (hello world)
print("hello world") # " " double quote (hello world)

# printing ' ' or " " inside a print function
print("hello 'world'") # hello 'world'
print('hello "world"') # hello "world"

# another way to do that is with \' or \"
print('hello \'world\'') # hello 'world'
print("hello \"world\"") # hello "world"




# string concatenation (+)
string1 = "I love"
string2 = " coding"
string3 = string1 + string2
print(string3) # "I love coding"

# uses
score = 50
print("I AM TOO GOOD I GOT A " + score + " FOR MY PROGRAMMING TEST!!") # "I AM TOO GOOD I GOT A 50 FOR MY PROGRAMMING TEST!!"



# string concatenation (,)
string1 = "I love"
string2 = "coding"
print(string1,string2) # "I love coding"

# unlike using (+), the (,) automatically puts spaces between the texts
score = 50
print("I AM TOO GOOD I GOT A",score,"FOR MY PROGRAMMING TEST!!" # "I AM TOO GOOD I GOT A 50 FOR MY PROGRAMMING TEST!!"




# end=
print("what")
print("is")
print("this")
# what
# is
# this

print("what", end= " ")
print("is", end= " ")
print("this")
# what is this

print("what", end= " o ")
print("is", end= " u ")
print("this")
# what o is u this


      
# sep=
age = 69
print("i am", age, "years old")
# i am 69 years old

print("i am", age, "years old", sep= "")
# i am69years old

print("i am", age, "years old", sep= "BRO")
# i amBRO69BROyears old



# escape characters
\n # creates new line
\t # for a tab character (indentation ig)
\" # just a "                     \"
\' # just a '                     \'
\\ # just a \

