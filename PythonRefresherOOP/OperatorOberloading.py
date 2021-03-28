class PC:
    def __init__(self, p1):
        self.p1 = p1

    def __mul__(self, other):
        return self.p1 * other.p1


pc1 = PC(2)
pc2 = PC(5)

print(pc1 * pc2)
