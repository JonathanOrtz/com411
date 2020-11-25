def observed ():
  observations = []
  for count in range (0,7,1):
    value = input("Introduce an observations: ")
    observations.append(value)
  return observations
# we put the input into a value and add the value to the list           (observations)
# we return the value of the list(we give the value to the function) 
def run():
  observationss = observed()
  print("\nCounting observations...")
# we call the first function(observed) into a variale(observationss)  
  
  observations_set = set()
# we create a set
  for observation in observationss:
    observation_data = (observation, observationss.count(observation))
    observations_set.add(observation_data)
# we use a loop to put a tuple with the observations that we            introduced
# we created a tuple and inside we put the value of "observation"       each iteration and the tuple's value each iteration with count  
  for observation_data in observations_set:
    print(f"{observation_data[0]} observed {observation_data[1]} times.")
# we use a loop with observation_data as the 'count' and                observations_set as the element to iterate
# we use observation observation_data with the 0 because it goes from   0 to 6(7) and observation_data with 1 because each observation introduced is at least once (ask for explanation)
run()