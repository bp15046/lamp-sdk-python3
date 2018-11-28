import pigpio


class Lamp():
    def __init__(self, pin=18):
        self._pin = pin
        self._gpio = pigpio.pi()

    def enable(self):
        self._gpio.set_mode(self._pin, pigpio.OUTPUT)

    def disable(self):
        self._gpio.stop()

    def on(self):
        self._gpio.write(self._pin, 1)
    
    def off(self):
        self._gpio.write(self._pin, 0)