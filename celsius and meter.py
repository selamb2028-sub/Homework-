def celsius():
    celsius = float(input("Enetr temperature in celsius: "))
    fahrenheit = (celsius * 9/5 + 32)
    print(f"{celsius}C = {fahrenheit}F")
def feet():
    feet= float(input("Enter measurment in feet: "))
    meter = (feet * 3.28)
    print(f"{feet}ft={meter}meter)")
    
print("press 1 for Fahrenheit to celsius")
print("press 2 for feet to meter")
conversion=int(input())
if conversion== 1:
    celsius()
elif conversion== 2:
    feet()
else:
    print("invalid input")                   