#Program No : 16
# To find the specifi c number count in a list
def counting(lis) :
 count=0	
 for i in lis :
  if i == 4 :
   count=count+1
 return count
ser = counting([4,4,4,4,4,6,7,4,8,9,21])
print("No of 4s is : ",ser) 

# To find the given letter is vowel or not....
def VowelOrNot(rts) :
 if rts in ['a','e','i','o','u','A','E','I','O','U'] :
 	return "It is Vowel ..  :)"
 else :
 	return "It is not vowel ... :("

# Program to check whether a specified value is contained in a group of values.

def ToCheck(lost,val) :
	if val in lost :
		return True
	else :
		return False
print(end="\n")
print(ToCheck([1,3,6,4,7,89,2,11,5],6))