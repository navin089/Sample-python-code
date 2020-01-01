import sys
import datetime
print("Python Version : ",sys.version)##Getting the curret python version on system..
now = datetime.datetime.now()
print("Current DateTime Format : ",now.strftime("%Y-%m-%d %H:%M:%S"))

seq_num = input("Enter set of inputs :")
opt = seq_num.split(",")
print("List is : ",list(opt))
print("Tuple is : ",tuple(opt)) ## to convert comma separated nums in lists and tuples..