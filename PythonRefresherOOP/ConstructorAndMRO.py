class A:
    def __init__(self):
        print("init A ")

    def f1(self):
        print("In A")


class B:
    def __init__(self):
        print("Init B")

    def f1(self):
        print("In B")


class D:
    def __init__(self):
        print("Init D")

    def f1(self):
        print("In D")


class E:
    def __init__(self):
        print("Init E")

    def f1(self):
        print("In E")


class C(A, B, D, E):
    def __init__(self):
        super().__init__()
        super(D, self).__init__()
        super(B, self).f1()


c = C()
