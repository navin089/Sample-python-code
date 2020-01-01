#Program no. 14
#program to print given text with given no of times as given by user...
def rep_count(srt,nom) :
 sttr = " "
 for i in range(nom):
  sttr = sttr + srt + " " 
 return sttr

srt = input("String : ")
nom = int(input("Counting : "))
op = rep_count(srt,nom)
print("Final  :",op)