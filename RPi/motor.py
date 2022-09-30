import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)


class motor:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)
    def turnUP(self):
        GPIO.output(self.pin,GPIO.HIGH)
    def turnDOWN(self):
        GPIO.output(self.pin,GPIO.LOW)



thedefmotor = motor(17)
thedefmotor.turnUP()
sleep(0.5)
thedefmotor.turnDOWN()

GPIO.cleanup()
