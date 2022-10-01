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





async def LEDtest(LEDpin):
    newLED = LED(LEDpin)
    newLED.turnON()
    await asyncio.sleep(1)
    newLED.turnOFF()


async def main():
    t1 = asyncio.create_task(LEDtest(17))
    t2 = asyncio.create_task(LEDtest(18))
    await asyncio.gather(t1,t2)



asyncio.run(main())
#tasks = [LEDtest(17),LEDtest(18)]

#for task in tasks:
#    asyncio.run(task)
#sleep(0.2)
#asyncio.run(main(18))




GPIO.cleanup()
