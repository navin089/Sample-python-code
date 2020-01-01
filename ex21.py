# program to display your details like name, age, address in three different lines
# program no. 37
def listdet(name,age,address) :
 print("Name : ",name )
 print("Age : ",age )
 print("Address : ",address)
listdet("Onkar",21,"solapur")
listdet("navin",21,"solapur")
listdet("xyz",11,"zz")


#Python program to solve (x + y) * (x + y). Go to the editor   ....Test Data : x = 4, y = 3
# program no. 38

def calc(x,y) :
 return (x + y) * (x + y)
print(calc(4,3))

#  program to compute the distance between the points (x1, y1) and (x2, y2)
# program no. 39
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)

