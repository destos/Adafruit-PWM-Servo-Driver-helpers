from adafruit import PWM
from servo import Futaba3003
from time import sleep
import random

pwm = PWM(address=0x40, debug=True)
pwm.setPWMFreq(50)

elbow = Futaba3003(pwm, 4)
shoulder = Futaba3003(pwm, 5)

# elbow.move_to_deg(90)
# shoulder.move_to_deg(80)

# def moveit():
#     servo.move_to_deg(0)
#     sleep(1)
#     for a in range(19):
#         angle = (a*10)
#         servo.move_to_deg(angle)
#         sleep(0.3)
#     moveit()
# 
# moveit()

def get_angle(prev):
    prev = random.randrange(prev-30, prev+30)
    prev = max(min(prev, 140), 40)
    return prev
    # return random.randrange(100)+35

prev_elb = 90
prev_sho = 90

while (True):
    elbow.move_to_deg(get_angle(prev_elb))
    sleep(0.5)
    shoulder.move_to_deg(get_angle(prev_sho))
    sleep(0.5)

pwm.reset()