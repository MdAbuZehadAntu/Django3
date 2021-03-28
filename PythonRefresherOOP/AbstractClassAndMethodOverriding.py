from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def haha(self):
        pass

class B(A):
    def haha(self):
        print("Abstract method")

b=B()
b.haha()
