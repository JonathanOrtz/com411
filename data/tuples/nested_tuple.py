def steps():
  likelihoods = [("step 1", 50),("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return likelihoods

def run():
  likelihood_ = steps()
  good_steps = []
  bad_steps = []
  for stepss in likelihood_:
    if stepss[1] >= 50:
      bad_steps.append(stepss)
    else:
      good_steps.append(stepss)

  print(f"Good steps:{len(good_steps)} Bad steps:{len(bad_steps)}")

run()