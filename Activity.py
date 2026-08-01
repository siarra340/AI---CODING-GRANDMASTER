city = input("What is your city? ")
temp = float(input("What is the temperature? "))
print(city)
print(type(temp))

if temp>25:
  print("It's warm")
elif temp>=18 and temp<=25:
  print("Its chilly")
else:
  print("It's cold")

import datetime 
import calendar

now = datetime.datetime.now()
print("City: ", city)
print("Time now: ", now)

print(calendar.calendar(now.year))