import calendar
import datetime
print(min.__doc__) # PRINT THE DESCRIPTIVE OF ANY KEYWORDS IN PYTHON
print(abs.__doc__) #;
print("Month and year of given inputs :  ",calendar.month(2024,8))
##---------------------------TO PRINT DIFFERENCE BETWEEN TWO DATES -------------------------------------##
d1 = datetime.date(2014,7,2)
d2 = datetime.date(2014,7,11)
d3 = d2-d1
print("Nu berous days : ",d3.days)

##---------------------------TO FIND THE VOLUME OF A SPHERE BY GIVEN RADIUS --------------------##
rad = 6.0
PI = 3.142
vos = (4/3) * PI * rad**3
print("Radius of Sphere : ",vos)