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
    def _init__(self, width, height, processor):
        super(CellPhone, width, height, processor, 'Apple')


class Android(CellPhone):
    def _init__(self, width, height, processor):
        super(CellPhone, width, height, processor, 'Google')


android = Android(1000, 1200, 4)
android.on()
isinstance(android, Android)

android2 = android
if android is android2:
    print('Same instance')

issubclass(CellPhone, IPhone)



