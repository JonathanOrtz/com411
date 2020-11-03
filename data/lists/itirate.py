def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
 print("Selec a direction")
 dirs = directions()
 # range(start_value, end_value, step=1)
 for index in range(len(dirs)):
  print(f"{index}: {directions}")


 selec_direction = int(input())
 return dirs[selec_direction]

def run():
  menu()
