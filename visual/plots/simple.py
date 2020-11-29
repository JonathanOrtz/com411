import matplotlib.pyplot as plt
# use the dictionary and the module pyplot
# create a function 
# use plt.plot(x, y) to display an line with plot
def display (x, y):
  plt.plot(x,y)
  plt.show()
# created a second function
# created a list of values of x and y
# we call the second function and we given the values of x_values and y_values to the x and y
def run ():
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  display(x_values, y_values)

run()
