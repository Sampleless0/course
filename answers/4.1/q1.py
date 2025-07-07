# function that takes in "temp" as a variable
def convert_cel_to_far(temp):
    return 9 * temp / 5 + 32

# function that takes in "temp" as a variable
def convert_far_to_cel(temp):
    return (temp-32) * 5 / 9

# print results to 2dp
print(f'the temperature in fahrenheit is: {convert_cel_to_far(float(input("Enter the temperature in Celsius: "))):.2f} degrees F')
print(f'the temperature in celcius is: {convert_far_to_cel(float(input("Enter the temperature in fahrenheit: "))):.2f} degrees C')
