class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudnets(self, num):
        self.numberOfStudents = num

    def __repr__(self):
        return f"A {self.level} school name {self.name} with {self.numberOfStudents} students"


class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    schoolrepr = super().__repr__()
    return schoolrepr + "The Pickup Policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)
  

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.SportsTeams
  
  def __repr__(self):
    schoolrepr = super().__repr__()
    return schoolrepr + f"Sports teams are {self.sportsTeams}"


h = HighSchool('UHS', 17, ['basketball', 'lax'])
print(h)
