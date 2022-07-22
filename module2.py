class RBI:
    def Interest(self):
        pass

class SBI(RBI):
    def Interest(self):
        print("SBI Interest is 5%")

class HDFC(RBI):
    def Interest(self):
        print("HDFC Interest is 2%")

s = SBI()
s.Interest()


b = HDFC()
b.Interest()


class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I CAN BARK")

class Snake(Animal):
    def move(self):
        print("I CAN HISSS")

A = Dog()
A.move()


B = Snake()
B.move()