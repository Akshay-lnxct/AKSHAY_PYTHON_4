class Celsius:
    def __init__(self, temperture = 0):
        self._temperature = temperture

    def to_fahreneight(self):
        return (self.temperature *1.8)+32

    @property
    def temperature(self):
        print("gettig value")
        return self._temperature

    @temperature.setter
    def temperater(self,value):
        if value < -273:
            raise ValueError("temperature below -273 is not possible")
        print("setting value")
        self._temperature = value

c = Celsius(5)
print(c.temperater)
c.temperater =100
print(c.temperater)

def multiplier_outer(n):
    def multiplier_inner(x):
        return x*n
    return multiplier_inner

ak = multiplier_outer(3)
vk = multiplier_outer(5)

print(ak(5))
print(vk(6))