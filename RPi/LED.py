import RPi.GPIO as GPIO
from time import sleep
import asyncio

GPIO.setmode(GPIO.BCM)


class LED:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)
    def turnON(self):
        GPIO.output(self.pin,GPIO.HIGH)
    def turnOFF(self):
        GPIO.output(self.pin,GPIO.LOW)





async def main(LEDpin):
    newLED = LED(LEDpin)
    newLED.turnON()
    await sleep(1)
    newLED.turnOFF()
    await sleep(1)



tasks = [main(17),main(18)]
asyncio.run(tasks)
#sleep(0.2)
#asyncio.run(main(18))


GPIO.cleanup()
