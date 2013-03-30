    
from adafruit import PWM
from servo import Continuous, Servo, Futaba3003
from time import sleep
import random
from math import sin, pi

pwm = PWM(address=0x40, debug=True)
pwm.setPWMFreq(50)

elbow = Futaba3003(pwm, 4)
shoulder = Futaba3003(pwm, 5)

dur = 900
freq = 30
factor = 2 * pi * freq/8000

# while (True):
for seg in range(8 * dur):
    # sine wave calculations
    sin_seg = sin(seg * factor)
    # sin_seq 
    deg = (sin_seg*40)+80
    elbow.move_to_deg(int(deg))
    shoulder.move_to_deg(int(deg))
    print "%s" % deg
    # sleep(0.02)
    
#     elbow.move_to_deg(get_angle(prev_elb))
#     sleep(0.5)
#     shoulder.move_to_deg(get_angle(prev_sho))
#     sleep(0.5)

# pwm.reset()