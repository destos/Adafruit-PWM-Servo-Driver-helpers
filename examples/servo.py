from adafruit import PWM
from servo import Servo
from time import sleep

pwm = PWM(address=0x40, debug=True)
pwm.setPWMFreq(50)

servo = Servo(pwm, 0)

while (True):
    servo.move_to_deg(0)
    sleep(1)
    for a in range(19):
        angle = (a*10)
        servo.move_to_deg(angle)
        sleep(0.3)