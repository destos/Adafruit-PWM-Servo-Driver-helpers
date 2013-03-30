class MecanumDrive(object):
    def __init__(self, *args, **kwargs):
        self.wheels = kwargs.pop('wheels', None)
        self.js = kwargs.pop('joystick', None)
        
    def calc_speeds(self):
        raise NotImplemented

class TankDrive(MecanumDrive):
    # tuning params
    Kf = 0
    Kt = 0
    Ks = 0
    
    # average both x axis?
    def calc_speeds(self):
        Yf = (self.js.y1 + self.js.y2)/2
        Yt = (self.js.y1 - self.js.y2)/2
        
        W1 = self.Kf*Yf + self.Kt*Yt + self.Ks*self.js.x1
        W2 = self.Kf*Yf + self.Kt*Yt - self.Ks*self.js.x1
        W3 = self.Kf*Yf - self.Kt*Yt + self.Ks*self.js.x1
        W4 = self.Kf*Yf - self.Kt*Yt - self.Ks*self.js.x1
        
        print "%s %s - %s %s" % (W1, W2, W3, W4)