#important ahh stuff

# f strings
print("") # not a f string
print(f"") # f string



# variables
sleep = 3
print(f"i slept for {sleep} hours yesterday") # i slept for 3 hours yesterday
print(f"i was supposed to sleep for {sleep+5} hours yesterday") # i was supposed to sleep for 8 hours yesterday
# f strings allow writing equations inside the print function



# text modification
money = 123456789.987654321
print(f"i wish i had ${money} rn") # i wish i had $123456789.987654321 rn
# for 2dp (.2f is 2dp, .4f is 4dp)
print(f"i wish i had ${money:.2f} rn") # i wish i had $123456789.99 rn

# if digit after is 0-5, round down. if digit after is 6-9, round up
money = 1.115
print(f"i wish i had ${money:.2f} rn") # i wish i had $1.11 rn (rounded down)
money = 1.116
print(f"i wish i had ${money:.2f} rn") # i wish i had $1.12 rn (rounded up)



# percentage (.1% is 1dp, .10% is 10dp)
grade = 0.955
print(f"i got {grade*100}% for gooning") # i got 95.5% for gooning (ok but not good)
print(f"i got {grade:.1%} for gooning") # i got 95.5% for gooning (better)



# alignment (VERY IMPORTANT)
first_name = "bruce"
last_name = "lim"
print(f"hello-there-{first_name}-{last_name}-the-human") # hello-there-bruce-lim-the-human

# :<x creates gap on the right side
print(f"hello-there-{first_name:<10}-{last_name}-the-human") # hello-there-bruce   -lim-the-human
print(f"hello-there-{first_name:<20}-{last_name}-the-human") # hello-there-bruce           -lim-the-human
print(f"hello-there-{first_name}-{last_name:<10}-the-human") # hello-there-bruce-lim     -the-human
print(f"hello-there-{first_name}-{last_name:<20}-the-human") # hello-there-bruce-lim             -the-human

# :>x creates gap on the left side
print(f"hello-there-{first_name:>10}-{last_name}-the-human") # hello-there-   bruce-lim-the-human
print(f"hello-there-{first_name:>20}-{last_name}-the-human") # hello-there-          bruce-lim-the-human
print(f"hello-there-{first_name}-{last_name:>10}-the-human") # hello-there-bruce-     lim-the-human
print(f"hello-there-{first_name}-{last_name:>20}-the-human") # hello-there-bruce-             lim-the-human

# :^x creates a gap both on the left and right and centres itself
print(f"hello-there-{first_name:^10}-{last_name}-the-human") # hello-there-  bruce   -lim-the-human
print(f"hello-there-{first_name:^20}-{last_name}-the-human") # hello-there-      bruce       -lim-the-human
print(f"hello-there-{first_name}-{last_name:^10}-the-human") # hello-there-bruce-   lim    -the-human
print(f"hello-there-{first_name}-{last_name:^20}-the-human") # hello-there-bruce-       lim        -the-human
