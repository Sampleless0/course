# mixed operations (my nightmare)
int = 5
float = 5.0
str = "five"
bool = True
error = None

# addition
int = int + int # 10 | int + int = int
float = float + float # 10.0 | float + float = float
str = str + str # fivefive | string + string = string
int = bool + bool # 2 | bool is 1 for True, 0 for False

float = int + float # 10.0 | int + float = float
int = int + bool # 6 | bool is treated as 1 for True, 0 for False
float = float + bool # 6.0 | bool is treated as 1 for True, 0 for False
error = int + str # NO | int cannot add with string
error = float + str # NO | float cannot add with string
error = str + bool # NO | string cannot add with bool



# subtraction
int = int - int # 0 | int - int = int
float = float - float # 0.0 | float - float = float
#error = str - str # NO | string cannot subtract string
int = bool - bool # 0 | bool is 1 for True, 0 for False

float = int - float # 0.0 | int - float = float
int = int - bool # 4 | bool is treated as 1 for True, 0 for False
float = float - bool # 4.0 | bool is treated as 1 for True, 0 for False
#error = int - str # NO | int cannot subtract with string
#error = float - str # NO | float cannot subtract with string
#error = str - bool # NO | string cannot subtract with bool



# multiplication
int = int * int # 25 | int * int = int
float = float * float # 25.0 | float * float = float
error = str * str # NO | string cannot mutliply string
int = bool * bool # 1 | bool is 1 for True, 0 for False

float = int * float # 25.0 | int * float = float
int = int * bool # 5 | bool is treated as 1 for True, 0 for False
float = float * bool # 5.0 | bool is treated as 1 for True, 0 for False
str = int * str # fivefive | string gets multiplied int number of times
error = float * str # NO | float cannot multiply with string
str = str * bool # five | bool is treated as 1 for True, 0 for False



# division
float = int / int # 1.0 | int / int = float
float = float / float # 1.0 | float * float = float
error = str / str # NO | string cannot divide string
int = bool / bool # 1 | bool is 1 for True, 0 for False

float = int / float # 1.0 | int * float = float
float = int / bool # 1.0 | bool is treated as 1 for True, 0 for False
float = float / bool # 1.0 | bool is treated as 1 for True, 0 for False
error = int / str # NO | int cannot divide by string
error = float / str # NO | float cannot divide by string
error = str / bool # NO | string cannot divide by bool
