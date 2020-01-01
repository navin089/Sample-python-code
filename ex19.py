# program No : 19
# program to get the least common multiple (LCM) of two positive integers

def findLCM(a1,a2) :
	if a1 > a2 :
		x = a1
	else:
		x = a2
	while True:
	 if (a1%x == 0) and (a2%x == 0) :
	  return x
	  
	 x+=1
	

print("LCM :",findLCM(10,20))