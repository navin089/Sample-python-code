def cal_sum(num1,num2,num3) :
 mins = num1+num2+num3
 if num1==num2==num3 :
  return int(3*mins)
 else :
  return mins
Sum = cal_sum(10,10,10) 
print("Sum : ",Sum)