
# shoulder = Futaba3003(pwm, 5)

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


# def get_angle(prev):
#     prev = random.randrange(prev-30, prev+30)
#     prev = max(min(prev, 140), 40)
#     return prev
#     # return random.randrange(100)+35
# 
# prev_elb = 90
# prev_sho = 90
# 
# while (True):
#     elbow.move_to_deg(get_angle(prev_elb))
#     sleep(0.5)
#     shoulder.move_to_deg(get_angle(prev_sho))
#     sleep(0.5)

pwm.reset()

# left = Continuous(pwm, 0)
# right = Continuous(pwm, 1, default_dir=False)
# 
# # wheel.setSpeed(0)
# for s in range(11):
#     speed = (s*10)
#     print('set speed %s' % (speed) )
#     left.setSpeed(speed)
#     right.setSpeed(speed)
#     sleep(1)


# wheel.setSpeed(10)
# wheel2.setSpeed(10)

# for s in range(5):
#     wheel.toggleDirection()
#     sleep(0.6)
#     

# left.setSpeed(0)
# right.setSpeed(0)

# sleep(2)
# wheel.toggleDirection()
# sleep(1)
# wheel.toggleDirection()
# sleep(1)
# wheel.forward()
# sleep(1)
# wheel.backwards()
# sleep(1)

# wheel2.setSpeed(0)
# wheel.setSpeed(0)


# from adafruit import PWM
# from mecanum.types import TankDrive, Drive
# from hardware import ServoWheels
# from time import sleep
# from math import sin, pi
# 
# def main():
#     pwm = PWM(address=0x40, debug=False)
#     pwm.setPWMFreq(50)
# 
#     # drive = TankDrive(wheels=ServoWheels(pwm))
#     
#     drive = Drive(wheels=ServoWheels(pwm))
# 
#     dur = 100
#     freq = 30
#     factor = 2 * pi * freq/8000
# 
#     # while (True):
#     for seg in range(8 * dur):
#         # sine wave calculations
#         sin_seg = sin(seg * factor)
#         #tank
#         # drive.js.pos=[1,-1,sin_seg,-sin_seg]
#         drive.js.pos=[sin_seg,0,1,0]
#         drive.calc_speeds()
#         # print "sin_seq: %s" % sin_seg
#         # print drive.wheels.pos
#         sleep(0.05)
#     
#     # reset joystick and re-calculate wheel speeds, should stop servos
#     drive.js.pos=[0,0,0,0]
#     drive.calc_speeds()
#     
#     pwm.reset()
# 
# def zero():
#     pwm = PWM(address=0x40, debug=False)
#     pwm.setPWMFreq(50)
#     drive = Drive(wheels=ServoWheels(pwm))
#     # joystick at zero so we should have zeroed out drive commands
#     drive.calc_speeds()
#     
# if __name__ == "__main__":
#     zero()