def short_pattern ():
  pattern = {"sequence":"101", "occurrences":5}
  return pattern

def medium_pattern ():
  pattern = {"sequences":"111000", "occurrences":25}
  return pattern

def long_pattern ():
  pattern = {"sequence":"1100110011001100", "occurrences":50}
  return pattern


def run():
  print("Analysing patterns...")
  run_dictionary = {"short sequence":short_pattern(), "medium sequence": medium_pattern(), "long sequence": long_pattern()}
  for key, value in run_dictionary.items():
    print(key, "=", value)
<<<<<<< HEAD

run()
=======
  
run()
>>>>>>> 0c0151cef8f7d3039dba14436f8939b89de8cff9
