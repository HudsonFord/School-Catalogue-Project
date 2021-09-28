class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getName(self):
      return self.name
    
  def getLevel(self):
      return self.level
    
  def getNumberOfStudents(self):
      return self.numberOfStudents

  def setNumberOfStudents(self, newNumberOfStudents):
      self.numberOfStudents = newNumberOfStudents
    

  def __repr__(self):
      return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy
    
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". The pickup policy is {cat}".format(cat = self.pickupPolicy)


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'High', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def getsportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    parent = super().__repr__()
    return parent + f" - information on the sports teams {self.sportsTeams}"

#Test School Class
mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.getName())
print(mySchool.getLevel())
mySchool.setNumberOfStudents(200)
print(mySchool.getNumberOfStudents())

print('\n')

#Test Primary School
testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.get_pickupPolicy())
print(testSchool)

print('\n')

#Test HighSchool
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c)