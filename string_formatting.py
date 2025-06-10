# hardest prob

# % formatting
name = "david"
sleep = 3
print('my name is %s and I have slept %d hours' % (name, sleep)) # my name is david and I have slept 3 hours
#types (dont need to know all)
%d # integer
%f # float
%s # string
%e # scientific notation (x10^3), %E for uppercase
%x # hexadecimal, %X for uppercase
%o # octal
%g # switches between %f and %e, %G for uppercase
%c # single character (eg. 5, "a")
%r # string but idk
%a # ascii version of string
%% # just % nothing else



# .format()
name2 = "ashvin"
marks = 90
print('apparently {} cheated and got a score of {}.' .format(name2, marks)) # apparently ash cheated and got a score of 90
# another way to put it is
print('apparently {var1} cheated and got a score of {var2}.' .format(var1 = name2, var2 = marks)) # apparently ash cheated and got a score of 90



# f-strings
grade = "C+"
time = 10
print(f'so somebody completed their programming test in {time} minutes but ended up with a {grade}')
# f strings allow operations inside the print
print(f'so somebody completed their programming test in {time * 60} seconds but ended up with a {grade}')



# template strings (slides say not tested but idk)
from string import Template
example = template('hello, $name, u look like a $look/10')
# in this example $name and $ look are like variables

user = template.substitude(name='bruce', look=3)
print(user) # hello, bruce, u look like a 3/10

