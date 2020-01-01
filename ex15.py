# Progrma No : 15
# To  get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 
def copier(string,num) :
 le = len(string)
 store = " "
 if le > 2 :
  for i in range(num) :
   store = store + string[:2] + " "
  return store
 else :
  for j in range(num):
   store = store + string + " "
  return store

stored = copier("A",3)
print("Same Copies : ",stored)