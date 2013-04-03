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



# wheel = ContinuousConst(pwm, 0)
# wheel2 = ContinuousConst(pwm, 1)
#
# wheel.set(0)
# # wheel2.set(0)
#
# dur = 10
# freq = 30
# factor = 2 * pi * freq/8000
#
# # while (True):
# for seg in range(10 * dur):
#     # sine wave calculations
#     sin_seg = sin(seg * factor)
#     # sin_seq
#     deg = int((sin_seg))
#     wheel.set(deg)
#     print "%s" % deg
#     sleep(0.05)
#
# wheel.set(0)