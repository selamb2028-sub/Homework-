# Created on iPad.

classify_person = int(input("enter age"))

if classify_person >= 0 and classify_person <= 12:
   print("child")
elif classify_person>= 13 and classify_person<= 17:
    print("teenager")
elif classify_person>= 18 and classify_person<= 64:
    print("Adult")
else :
   print("senior")


