## to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
num = int(input("Enter Numbers : "))
if num - 17 < 17 :
	print("Simple difference is : ",num-17)
else:
	print("Variant Difference is :  ",(num-17)*2)

## Python program to test whether a number is within 100 of 1000 or 2000.
def near_thousand(n):
     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))
