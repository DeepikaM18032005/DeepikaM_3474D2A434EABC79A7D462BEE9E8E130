
number=int(input("Enter the number:"))
def factorial_function(x):
  if(x>0):
    result=x*factorial_function(x-1) 
  else:
    result = 1
  return result

res=factorial_function(number)
print("The Factorial is:",res)