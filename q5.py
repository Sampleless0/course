cookie = {
    "suger": 1.5/48,
    "butter": 1/48,
    "flour": 1/24
}
wantCookie = int(input("how many cookies u want = "))

def calculate(wantCookie, cookie):
    suger = wantCookie * cookie["suger"]
    butter = wantCookie * cookie["butter"]
    flour = wantCookie * cookie["flour"]
    return str(f"u need {suger} cups of suger, {butter} cups of butter and {flour} cups of flour")

print(calculate(wantCookie, cookie))
