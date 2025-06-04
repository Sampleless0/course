item1 = float(input("cost of item 1 = "))
item2 = float(input("cost of item 2 = "))

def calculate(firstItem, secondItem):
    print(f"cost before gst = ${firstItem + secondItem:.2f}")
    print(f"cost of gst = ${(firstItem + secondItem)*0.08:.2f}")
    print(f"cost after gst = ${(firstItem + secondItem)*1.08:.2f}")

calculate(item1, item2)
