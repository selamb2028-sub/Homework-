Time = int(input("enter hour"))

if Time >= 5 and Time <= 11:
   print("Morning")
elif Time >= 12 and Time <= 16:
    print("Afternoon")
elif Time >= 17 and Time <= 20:
    print("Evening")
else :
   print("Night")
