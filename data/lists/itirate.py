def directions():
  directions["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return list

def menu():
  select_direction=input("Please select a directions: ")
  return_direction=directions()
  for index in range(0,1,1):
    print(f"{index}:{return_directions}")

def run():
  menu()
run()