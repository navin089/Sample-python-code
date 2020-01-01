# program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Symmetric Difference : ",color_list_1 - color_list_2)

#Accept the base and height of a triangle and compute the area.
base , height =20.0 , 40.0
print("Area of Triangle : ",(0.5 * height * base))

#program to sum of three given integers. However, if two values are equal sum will be zero.
def smofnum(n1,n2,n3) :
	if (n1==n2 or n2==n3 or n1==n3)  :
		return 0
	else:
		return n1+n2+n3
print("Sum : ",smofnum(12,13,10))
	