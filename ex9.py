ipfile = input("Enter file name with extension : ")
top = ipfile.split('.')
print("Given file extension is  :  ",top[-1])## To PRINT THE GIVEN FILE EXTENSION

exam_st_date = (11, 12, 2014)
print("Converted Date format is : %i/%i/%i "%exam_st_date) ## To convert date format as " 11/12/2014 "

#-----------------------------------------------------------------------------------------------------------------------#
#TO CALCULATE SUM LIKE i.e  IF IP=2 then o/p is 2+22+222 is 246..........
num = int(input("Enter nums : ")) 
n1 = int ("%s"%(num))
n2 = int ("%s%s"%(num,num))
n3 = int ("%s%s%s"%(num,num,num))
print("Nums : ",n1+n2+n3)