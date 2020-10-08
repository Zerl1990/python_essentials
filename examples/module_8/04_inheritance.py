class CellPhone:
    def __init__(self, width, height, processor, brand):
        self.status = 'OFF'
        self.brand = brand
        self.width = width
        self.height = height
        self.processor = processor

    def on(self):
        self.status = 'ON'

    def off(self):
        self.status = 'OFF'


class IPhone(CellPhone):
    def __init__(self, width, height, processor):
        super().__init__(width, height, processor, 'Apple')

    def on(self):
        self.status = 'ON-IPHONE'


class Android(CellPhone):
    def __init__(self, width, height, processor):
        super().__init__(width, height, processor, 'Google')

    def on(self):
        self.status = 'ON-ANDROID'


android = Android(1000, 1200, 4)
android.on()
print(android.status)

iphone = IPhone(1000, 1200, 4)
iphone.on()
print(iphone.status)


