#sttr = input("Get the string : ")
def getone(sttr):
 ptr = sttr.split(" ")
 if ptr[0] == 'Is' :
 	return sttr 
 else:
 	return 'Is ' + sttr
sert = getone('my name is navin ')
print("Sent : ",sert) 
