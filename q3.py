# receives input as float
item1 = float(input("cost of item 1 = "))
item2 = float(input("cost of item 2 = "))

# print results to 2dp
print(f"cost before gst = ${item1 + item2:.2f}")
print(f"cost of gst = ${(item1 + item2)*0.08:.2f}")
print(f"cost after gst = ${(item1 + item2)*1.08:.2f}")
