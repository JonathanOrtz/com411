def display_ladder(steps):
  for i in range(steps):
   print("| |")
   print("===")

print("| |")

def create_ladder():
  print("How many steps remain?")
  steps=int(input())
  display_ladder(steps)

create_ladder()

#steps is the input because it is the parametre for the def display_ladder and the for loop execute with the parametre steps, that's why it must be the int(input())