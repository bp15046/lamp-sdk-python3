from lamp.lamp import Lamp
import time


lamp = Lamp()

lamp.enable()

lamp.on()
time.sleep(3)
lamp.off()

lamp.disable()