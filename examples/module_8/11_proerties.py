class Celsius:
    def __init__(self, value):
        self.__temperature = value

    def to_fahrenheit(self):
        return (self.__temperature * 1.8) + 32

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError('Invalid value')
        self.__temperature = value


temp = Celsius(10)
print(temp.temperature)
temp.temperature = 45
print(temp.temperature)
