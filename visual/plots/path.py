import matplotlib.pyplot as plt 
# creation of the first function
# we create a input to enter a x and y values

def coordinates ():
  x_value=int(input("Please enter a x value: "))
  y_value=int(input("Please enter a y value: "))
  return (x_value, y_value)
# creation of the second function
# creation of list of x and y values
# creation of for loop to iterate over the function coordinates()(the   x and y values introduced)
# the loop iterate 4 times because we want to want 4 values for x and   4 for y
# we return the values of x and y, which are list, on a list
def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for values in range(4):
    data=coordinates()
    x_values.append(data[0])
    y_values.append(data[1])
  return [x_values, y_values]
# creation of the third function
# we call the second function in a variable(values)
# use plt.plot to draw a line where values[0] is x_values and values    [1] are the y_values
# labels for indicate the axis
def run():
  values = path()
  plt.plot(values[0], values[1], 'r--o')
  plt.xlabel("X values")
  plt.ylabel("Y values")
  plt.show()

run()
