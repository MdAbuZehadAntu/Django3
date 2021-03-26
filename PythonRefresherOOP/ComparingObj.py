class Guy:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def compare(self,other):
        if self.name==other.name and self.age==other.age:
            return True
        return False



guy1=Guy("Antu",24)
guy2=Guy("Ant",24)

if guy1.compare(guy2):
    print("Same")
else:
    print("Not same")