import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
wDATA = 1
wCMD =0


class screen:
    def __init__(self,RWpin,RSpin,Epin,DATApins):
        self.status = 0
        self.RWpin = RWpin
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

    def write(self,mode,DATA):
        GPIO.OUT(self.RWpin,GPIO.LOW)
        if mode == wDATA:
            GPIO.output(self.RSpin,GPIO.LOW)
        if mode == wCMD:
            GPIO.output(self.RSpin,GPIO.HIGH)
        for tpin in self.DATApins():
            GPIO.output(tpin,GPIO.LOW)
        if DATA&0x10==0x10:
            GPIO.output(self.DATApins[0],GPIO.HIGH)
        if DATA&0x20==0x20:
            GPIO.output(self.DATApins[1],GPIO.HIGH)
        if DATA&0x40==0x40:
            GPIO.output(self.DATApins[2],GPIO.HIGH)
        if DATA&0x80==0x80:
            GPIO.output(self.DATApin[[3],GPIO.HIGH)
        
        self.refresh()
        if DATA&0x01==0x01:
            GPIO.output(self.DATApins[0],GPIO.HIGH)
        if DATA&0x02==0x02:
            GPIO.output(self.DATApins[1],GPIO.HIGH)
        if DATA&0x04==0x04:
            GPIO.output(self.DATApins[2],GPIO.HIGH)
        if DATA&0x08==0x08:
            GPIO.output(self.DATApins[0],GPIO.HIGH)
        self.refresh()


    def init(self):


    def refresh(self):
        sleep(0.001)
        GPIO.output(Epin,GPIO.HIGH)
        sleep(0.001)
        GPIO.output(Epin,GPIO.LOW)


if __name__ == "__main__":
    DATApins = [35,36,37,38]
    myScreen = screen(7,33,40,DATApins)
    myScreen.init()
    GPIO.cleanup()

