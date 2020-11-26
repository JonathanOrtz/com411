def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods), likelihoods()

def run():
  probabilities_value = likelihood()
  print(f"Minimun likelihood of falling is {probabilities_value[0]}%")
  print(f"Maximun likelihood of falling is {probabilities_value[1]}%")
run()
