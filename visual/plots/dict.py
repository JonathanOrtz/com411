import matplotlib.pyplot as plt
import random as rdm
# import randomd dictionary for get random numbers
def data():

  paths = {}

  lines=input("what type of line would you like (:, -- or -) ?")
  colour=input("what type of color would you like (r, g or b) ?")
  marker=input("what type of marker would you like (o, s or ^) ?")

  paths['lines']=lines
  paths['colour']=colour
  paths['marker']=marker

  return paths
# creation of an empty dictionary
# input of some varibles
# addition of the variables inside of the dictionary
# return the function
def generate():

  number_lines=int(input("How many lines like would like to display?"))

  for count in range(number_lines):
    values = data()
    x_rdm_values = rdm.sample(range(1,10), number_lines)
    y_rdm_values = rdm.sample(range(1,10), number_lines)
    format=(f"{values['lines']}{values['colour']}{values['marker']}")
    plt.plot(x_rdm_values, y_rdm_values, format)
    plt.show()
# input of the number of lines  
# creation of the for loop for iterade the number of lines that the     user has introduced 
# calling of the second first function in a variable(values)
# creation of x and y values for the graphic with random introduced     by the rdm.sample
# format for the values 
# creation of the plot 
def run():
  
  print("Running...")
  generate()
  print("Done!")

run()