class A:
    def feat1(self):
        print("from A")


class B:
    def feat2(self):
        print("from B")


class C(B):
    def feat3(self):
        print("from C")


class D(A,C):
    def feat4(self):
        print("from B")


a = A()
b = B()
c = C()
d = D()

print(a.feat1())  # can only access 1 method
print(b.feat2())  # can only access 1 method
print( c.feat3())  ## can access 2 methods
print(d.feat1(), d.feat2(), d.feat4()) # can  access all methods
