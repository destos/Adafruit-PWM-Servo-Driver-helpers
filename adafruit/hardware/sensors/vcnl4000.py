import time

from adafruit.i2c import Adafruit_I2C


class VCNL4000(object):
    i2c = None

    __ADDRESS           = 0x13

    # commands and constants
    __COMMAND           = 0x80
    __PRODUCTID         = 0x81
    __IRLED             = 0x83
    __AMBIENTPARAMETER  = 0x84
    __AMBIENTDATA       = 0x85
    __PROXIMITYDATA     = 0x87
    __SIGNALFREQ        = 0x89
    __PROXINITYADJUST   = 0x8A

    __3M125             = 0
    __1M5625            = 1
    __781K25            = 2
    __390K625           = 3
    __FREQUENCIES = (
        (__3M125, '3.125 MHz'),
        (__1M5625, '1.5625 MHz'),
        (__781K25, '781.25 KHz'),
        (__390K625, '390.625 KHz'))

    __MEASUREAMBIENT    = 0x10
    __MEASUREPROXIMITY  = 0x08
    __AMBIENTREADY      = 0x40
    __PROXIMITYREADY    = 0x20
    
    def __init__(self, address=0x13, debug=False):
        self.i2c = Adafruit_I2C(address, debug=debug)
        self.address = address
        self.debug = debug

        rev = self.i2c.readU8(self.__PRODUCTID)
        if (rev & 0xf0) != 0x10:
            raise Exception('no sensor found on address: %s' % self.address)
        
        # make configurable?
        # set to 20 * 10mA = 200mA
        self.i2c.write8(self.__IRLED, 20)
        if self.debug:
            print 'current = %smA' % self.i2c.read8(self.__IRLED) * 10

        # TODO: be able to set freqency
        # self.write8(self.__SIGNALFREQ, 3)
        if self.debug:
            freq = self.i2c.read8(self.__SIGNALFREQ)
            print "proximity measurement frequency = %s" % self.__FREQUENCIES[freq][1]

    def readProximity(self):
        self.i2c.write8(self.__COMMAND, self.__MEASUREPROXIMITY)
        while True:
            result = self.i2c.read8(self.__COMMAND)
            # proximity sensor has been freed
            if result & self.__PROXIMITYREADY:
                return self.i2c.read16(self.__PROXIMITYDATA)
            time.sleep(1)

    # TODO: similar to proximity, maybe keep it dry?
    def readAmbient(self):
        self.i2c.write8(self.__COMMAND, self.__MEASUREAMBIENT)
        while True:
            result = self.i2c.read8(self.__COMMAND)
            # ambient sensor has been freed
            if result & self.__AMBIENTREADY:
                return self.i2c.read16(self.__AMBIENTDATA)
            time.sleep(1)


FREQUENCIES = dict((v, k) for k, v in VCNL4000.__FREQUENCIES)