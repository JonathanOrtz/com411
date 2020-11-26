def likelihood ():
  likelihood = (50, 38, 27, 99, 4)
  return likelihood

def run ():
  value = likelihood()
  print("Minimum likelihood of falling: {}%".format(min(value)))

run()
