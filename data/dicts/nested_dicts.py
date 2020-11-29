def short_pattern():
  pattern={"sequence":"101", "occurrences":5}
  return pattern
# create the dictionary with the values and return it
def medium_pattern():
  pattern={"sequence":"111000", "occurrences":25}
  return pattern
# create the second dictionary with the values and return it
def long_pattern():
  pattern={"sequence":"1100110011001100", "occurrences":50}
  return pattern
# create the third dictionary with the values and return it
def run():
  print("Analysing patterns...")
  all_patterns={"short sequence": short_pattern(), "medium sequence": medium_pattern(), "long sequence": long_pattern() }
  for key, value in all_patterns.items():
    print(f"{key}:{value}")
# create a new dictionary and each key has the return of each function
# use for loop, items function with key, value to display the           dictionary
# the value, key is the "count" and the disctionary which will be iterade is with the items function, which return the key, value. 
run()
