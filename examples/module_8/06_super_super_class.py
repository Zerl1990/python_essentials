class Level1:
    var = 10
    __private_var = 100

    def function(self):
        return self.__private_var


class Level2(Level1):
    var = 20
    __private_var = 200

    def function(self):
        return self.__private_var


class Level3(Level2):
    var = 30
    __private_var = 300

    def function(self):
        return self.__private_var


my_instance = Level3()
print(my_instance.var)
print(my_instance.function())