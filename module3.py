class A:
    def __init__(self,a):
        self._a=a


    def show(self):
        print("protected variable : " ,self._a)

class B(A):
    def __init__(self,b):
        super().__init__(b)

    def showB(self):
        print("variable value : " , self._a)

obj = B(20)
obj.showB()
obj.show()