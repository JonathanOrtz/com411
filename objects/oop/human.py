class Human:
  #class attribute
  MAX_ENERGY  = 100
  # initializer(special instance method)
  def __init__(self, name="Human", age=0):
    # instance attributes
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  def grow(self):
    self.age+=1

  def eat(amount):
    energy_plus = self.energy + amount
    if (energy_plus>Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
      return energy_plus - self.energy
    else:
     self.energy = energy_plus
     return 0
  #  An instance method (to display)
  def display(self):
    print(f"I am {self.name}")
  # Instance method repr(to return an formal string representation of the object)
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy{Human.MAX_ENERGY})'
  # Instance method str(to return an informal sring of the object)
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} and my energy is {Human.MAX_ENERGY}'

if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(human)
  print(repr(human))
