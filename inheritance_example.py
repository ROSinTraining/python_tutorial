import os

# parent class
class Student():
   # constructor of parent class
   def __init__(self, name, enrollnumber):
      self.name = name
      self.enrollnumber = enrollnumber
   def display(self):
      print(self.name)
      print(self.enrollnumber)

# child class
class College( Student ):
   def __init__(self, name, enrollnumber, admnyear, branch):
      self.admnyear = admnyear
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)


# child class
class University( Student ):
   def __init__(self, name, enrollnumber, refno, branch):
      self.refno = refno
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)

      
# creation of an object for base/derived class
obj_1 = College('Rohit',42414802718,2018,"CSE")
obj_1.display()
obj_2 = University ('Rohit',42414802718,"st2018","CSE")
obj_2.display()