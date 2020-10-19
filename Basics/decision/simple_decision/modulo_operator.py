#asking for a whole number
print("Please enter a whole number.")
number = int(input())
# use 2 to know if it is a odd number 
if(number%2==1):
  print("The number {} is an odd number". format(number))
else:
  print("The Number {} is an even number". format(number))
