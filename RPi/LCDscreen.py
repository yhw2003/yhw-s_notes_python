import RPi.GPIO as GPIO
import sleep from time

GPIO.setmode(GPIO.BOARD)
wDATA = 1
wCMD =0


class screen:
    def __init__(self,RWpin,RSpin,Epin,DATApins):
        self.status = 0
        self.RWpib = RWpin
        self.Epin = Epin
        self.RSpin = RSpin
        self.DATApins = DATApins
        GPIO.setup(RSpin,GPIO.OUT)
        GPIO.setup(RWpin,GPIO.OUT)
        GPIO.setup(Epin,GPIO.OUT)
        self.DATApins = DATApins
        GPIO.output(Epin,GPIO.LOW)
        for _pin in DATApins:
            GPIO.setup(_pin,GPIO.OUT)

    def write(mode,DATA):
        i = 0
        GPIO.OUT(self.RWpin,GPIO.LOW)
        if mode == wDATA:
            GPIO.output(self.RSpin,GPIO.LOW)
        if mode == wCMD:
            GPIO.output(self.RSpin,GPIO.HIGH)
        for tPIN in self.DATApins:
            if DATA[i] == 1:
                GPIO.output(tPIN,GPIO.HIGH)
            if DATA[i] == 0:
                GPIO.output(tPIN,GPIO.LOW)
            i = i + 1
        sleep(0.001)
        GPIO,output(self.Epin,GPIO.HIGH)
        sleep(0.001)
        GPIO.output(self.Epin,GPIO.LOW)

    def init():


    def refresh(self):
        if self.status == 0:
            GPIO.output(self.Epin,GPIO.HIGH)
            self.status = 1
        if self.status == 1:
            GPIO.output(self.Epin,GPIO.LOW)
            self.status = 0

if __name__ == "__main__":
    DATApins = [35,36,37,38]
    myScreen = screen(7,40,DATApins)
    myScreen.refresh()
    GPIO.cleanup()

