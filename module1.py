class A1:
    def myfunction1(self):
        print("class A1 function called")

class A2(A1):
    def myfunction2(self):
        print("class A2 function called")

class A3(A1):
    def myfunction3(self):
        print("class A3 function called")

class A4(A2,A3):
    def myfunction4(self):
        print("class A4 function called")

a = A4()
a.myfunction1()
a.myfunction2()
a.myfunction3()
a.myfunction4()
