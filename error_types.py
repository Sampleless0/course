# errors eww


# syntax error
# usually typos
print("hello world)          ") # this is just for making easier to read
# missing " (SyntaxError: unterminated string literal)



# runtime error
# any errors that happens when the program is running



# ZeroDivisionError
print(1/0)
# cannot divide by 0 (ZeroDivisionError: division by zero)


# NameError
print(brucevin)
# missing "", treats hello world as a variable (NameError: name 'brucevin' is not defined)


# TypeError
print("1"+0)
# mixing different types of variables which do not work (TypeError: can only concatenate str (not "int") to str)


# IndexError
list = [1,2,3]
print(list[100])
# tries to reach a variable inside a array that doesnt exist (IndexError: list index out of range)


# KeyError
dih = dict(length=3, name="TwT")
print(dih["width"])
# tries to read a variable inside a dictionary which doesnt exist (KeyError: 'width')


# ValueError
print(int("bruce"))
# cannot convert a type of variable to another (ValueError: invalid literal for int() with base 10: 'bruce')


# IndentationError
fact = True
if fact == True:
print("truth")
# forgets the "tab/space" for if else and while statements (IndentationError: expected an indented block after 'if' statement)
# corrected code looks like
fact = True
if fact == True:
  print("truth")

#
