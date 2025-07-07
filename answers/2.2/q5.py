# list variables
suger = 1.5/48
butter = 1/48
flour = 1/24

# ask for number of cookies
wantCookie = int(input("how many cookies u want = "))

# calculate ingredients
suger *= wantCookie
butter *= wantCookie
flour *= wantCookie

# print result
print(f"u need {suger} cups of suger, {butter} cups of butter and {flour} cups of flour")
