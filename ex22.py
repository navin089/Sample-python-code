# a Python program to check whether a file exists
# program no. 40
import os
import platform 
print(os.path.isfile("ex17.py"))

#   program to get OS name, platform and release information
# program no. 41
print(os.name)
print(platform.release())
print(platform.system())