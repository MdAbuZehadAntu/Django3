class Computer:

    def __init__(self,cpu="Normal",ram=4): ### constructor for python
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print(f"Config is ram= {self.ram}gb and cpu ={self.cpu}")

com1=Computer()
com2=Computer('i7',8)
com3=Computer('Ryzen',12)

com1.config()
com2.config()
com3.config()