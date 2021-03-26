class Human:

    def __init__(self, name, gender, h_color, h_type):
        self.name = name
        self.gender = gender
        self.hand = self.Hands(h_color, h_type,self)

    def show(self):
        print(self.name, self.gender)
        self.hand.show()

    class Hands:
        fingers = 5

        def __init__(self, color, type,other):
            self.color = color
            self.type = type
            self.parent=other

        def show(self):
            print(self.parent.name+" : "+self.color, self.type,Human.Hands.fingers)


h1 = Human("Antu", "Male", "dark", "hard")
h2 = Human("Bush", "Female", "fair", "soft")


h1.show()
# h1.hand.show()
h2.show()
# h2.hand.show()