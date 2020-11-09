import random
minimun_value=int(input("\nPlease enter the minimum value: "))
maximun_value=int(input("\nPlease enter the maximum value: "))
random_number=random.randrange(minimun_value, maximun_value)
#we use randrange to get a random number between the min and the max
print(f"I am thinking of a number between {minimun_value} and {maximun_value} \nCan you guess what it is?")

guess=0
while(guess!=random_number):
  print("Plese introduce a number")
  guess=int(input())
  
  if guess==random_number:
    print("Congratulations")
    break
  #this break is use to stop the while loop cause the the parametre is that while is not the same but if it is the same the while loop must stop
  elif guess>random_number:
    print("Your guess is too high")
  else:
    print("Your guess is too low")
print("Game Over!")