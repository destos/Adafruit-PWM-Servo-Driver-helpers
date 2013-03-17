# from adafruit.pwm import PWM
import math

class BaseServo(object):
    """BaseServo functions"""
    def __init__(self, pwm, channel=0):
        try:
            self.debug = pwm.debug
        except:
            self.debug = False
        
        self.pwm = pwm
        self.channel = channel

        # check pwm 
        self.min = 1000
        self.max = 2000
        self.range = ((self.max - self.min) / 2)
        self.mid = self.max - self.range
        self.cycle = 50 # 50hz cycle
        self.pulseLength = 1000000 / self.cycle
        self.tick = self.pulseLength / 4096 # 12 bit resolution

    def set_pulse(self, pulse):
        """set the pulse on this servo's channel"""
        pulse = max(min(pulse, self.max), self.min)
        self.pwm.setPWM(self.channel, 0, pulse/self.tick)


class Continuous(BaseServo):
    """Continuous Servo"""
    def __init__(self, *args, **kwargs):
        self.default_dir = kwargs.pop('default_dir', True)
        self.dir = self.default_dir
        super(Continuous, self).__init__(*args, **kwargs)

    def set_speed(self, speed=0):
        """set continuous speed, 0-100"""
        self.curSpeed = speed
        # never above 100 or below 0
        speed = max(min(speed, 100), 0)
        mod = 0
        if speed != 0:
            adjust = (speed * self.range) / 550 # scale down for more accurate control
            mod = -(adjust) if self.dir else adjust
        newPulse = self.mid+mod
        if self.debug:
            print 'set_pulse %s, mod: %s' % (newPulse, mod)
        self.set_pulse(newPulse)

    def forward(self):
        """docstring for forward"""
        if self.debug:
            print 'going forward'
        self.dir = not self.default_dir
        self.setSpeed(self.curSpeed)

    def backwards(self):
        if self.debug:
            print 'going backwards'
        """docstring for backwards"""
        self.dir = self.default_dir
        self.setSpeed(self.curSpeed)

    def toggle_direction(self):
        if self.debug:
            print 'toggling direction'
        self.dir = not self.dir
        self.setSpeed(self.curSpeed)


class Servo(BaseServo):
    """Servo Handle"""
    def __init__(self, *args, **kwargs):
        super(Servo, self).__init__(*args, **kwargs)
        self.total_deg = 180

    # functions to set angle and stuff.
    def radians(self, deg, minutes=0, sec=0):
        return math.radians(deg + minutes / 60.0 + sec / 3600.0)

    def _get_pulse_for_deg(self, deg):
        return (((self.max - self.min) * deg) / self.total_deg) + self.min

    def move_to_deg(self, deg):
        if self.debug:
            print "moving to %s degrees" % deg
        self.set_pulse(self._get_pulse_for_deg(deg))


# Configurations
class Futaba3003(Servo):
    def __init__(self, *args, **kwargs):
        super(Futaba3003, self).__init__(*args, **kwargs)
        self.total_deg = 178
        self.min = 400
        self.max = 1950