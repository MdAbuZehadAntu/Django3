class Student:
    school_name = "Antus"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def getRoll(self):
        return self.roll

    def setRoll(self, roll):  ### related to obj
        self.roll = roll

    @classmethod  ## related to class
    def getSchool(cls):
        return cls.school_name

    @staticmethod  ### not related to obj
    def info():
        print(Student.school_name + " is a famous school")


s1 = Student("Antu", 1)
s2 = Student("Bush", 2)

print(s1.getRoll(),s1.getSchool())
print(s2.getRoll(),s2.getSchool())
# quit()
print(Student.getSchool())

# quit()
s1.info()
