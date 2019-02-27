import circle
import random

class Star(circle.Circle):
    def __init__(self, x, y, world_width, world_height):
        circle.Circle.__init__(self, x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness = random.uniform(0, 255)
        self.mColor = (0,0,255)

    def getBrightness(self):
        return self.mBrightness

    def setBrightness(self, brightness):
        if brightness >= 0 and brightness <= 255:
            self.mBrightness = brightness
            self.mColor = (brightness,brightness,brightness)
        return

    def evolve(self, dt):
        c = 125
        x = random.randrange(3)
        if x == 0:
            self.mBrightness += 10
            c += 10
            self.setBrightness(c)
            return
        elif x == 1:
            self.mBrightness = -10
            c -= 10
            self.setBrightness(c)
            return
        else:
            return
    
            
