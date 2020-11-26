def observed():
  observations = []
  for count in range(0,5,1):
    value = input("Please introduced observations: ")
    observations.append(value)

  return observations

def remove_observations(observations):
  running=True
  while(running):
    print("\nWould you like remove any observations(yes/no)?")
    answer=input()
    if (answer == "yes"):
     print("\nWhat observation would youb like remove? ")
     observation_removed = input()
     observations.remove(observation_removed)
     print("\nRemoved")
    else:
     running = False

def run():
  observations=observed()
  remove_observations(observations)
  observation_set = set()
  print("\nObservations sumary:")
  for observation in observations:
    data = (observation, observations.count(observation))
    observation_set.add(data)

  for data in sorted(observation_set):
    print(f"{data[0]} counted {data[1]}")
run()