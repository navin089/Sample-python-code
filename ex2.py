import datetime 
# TO PRINT THE CURRENT DATE AND TIME OF THE SYSTEM
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d  %H:%M:%S"))

#TO CALCULATE THE  AREA OF CIRCLE BY GIVEN RADIUS 
num = input("Enter the radius :")
area = 3.14 * float(num) * float(num)
print("Area id %f"%area)

#TO PRINT THE NAME IN REVERSE ORDER AS WORD
#E.G navin kodam result = kodam navin
n1 = input("first name :")
n2 = input("second name :")

print("Original order :     "+ n1 +" "+ n2)
print("Reversed order :     "+ n2 +" "+ n1) 