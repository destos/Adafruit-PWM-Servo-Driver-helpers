from adafruit import PWM
from servo import Continuous
from time import sleep

pwm = PWM(address=0x40, debug=True)
pwm.setPWMFreq(50)

wheel = Continuous(pwm, 0)


while (True):
    wheel.setSpeed(0)
    for s in range(11):
        speed = (s*10)
        print('set speed %s' % (speed) )
        wheel.setSpeed(speed)
        sleep(1)
