class Car:
    company="Antu's"

    def __init__(self,mil,wheels):
        self.wheels=wheels
        self.mil=mil

c1=Car(10,4)
c2=Car(8,4)

Car.company="aaa"
print(c1.wheels,c1.mil,c1.company)
print(c2.wheels,c2.mil,c2.company)