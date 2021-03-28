#python doesnt support metyhod overloasding as java do so we have to do the trick

class A:

    def sum(self,a=0,b=0,c=0):
        return a+b+c

a=A()
print(a.sum(5,9,6))