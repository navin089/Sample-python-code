# program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# progrma No : 20
def summ(num1,num2) :
  if (num1+num2) in range(15,21) :
   return 20
  else:
   return num1+num2
print(summ(8,7))

# program that will return true if the two given integer values are equal or their sum or difference is 5
# program no . 21

def sumdif(num1,num2) :
 if (num1==num2) or (num1+num2==5) or abs(num1-num2)==5 :
  return True
 else:
 	return False
print(sumdif(5,10))

# program to add two objects if both objects are an integer type.
# program no. 22
def typecmp(num1,num2) :
 if type(num1) == type(num2) :
  return num1+num2
 else:
 	return "Type Error"
print(typecmp(20,10.9))
 