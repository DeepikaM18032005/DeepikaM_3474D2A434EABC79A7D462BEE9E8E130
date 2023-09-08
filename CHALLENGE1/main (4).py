year=int(input("Enter the Year to check whether it is a leap year or not a leap year:"))
if(year%4==0 and year%100!=0)or year%400==0:
  print("it's a leap year")
else:
  print("its not a leap year")
