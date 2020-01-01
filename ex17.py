# Program No : 17 
# program to create a histogram from a given list of integers
def Histogram(lis,sym) :
	for i in lis :
		for j in range(i) :
			print(sym,end=" ")
		print(end="\n")
Histogram([2,5,3,2,1],'9')

#Program to concatenate all elements in a list into a string and return it
def Concate(llist) :
 sert = " "
 for i in llist :
  sert = sert + str(i)
 return sert
print("Concatinated : ",Concate(['A','IM','BI','T','CH','PR','OGRA','M','MER']))

#program to print all even numbers from a given numbers list in the same order and ,
#stop the printing if any numbers that come after 237 in the sequence

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527 ]
new_list = []
for u in numbers :
  if u == 237 :
  	break
  elif u % 2 == 0 :
    new_list.append(u)
  else :
    pass
print("New List : ",new_list)
