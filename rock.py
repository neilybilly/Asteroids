import polygon
import random, math

class Rock(polygon.Polygon):
    def __init__(self, x, y, world_width, world_height):
        polygon.Polygon.__init__(self, x, y, 0, 0, 0, world_width, world_height)
        self.mRotation = random.uniform(1, 359.9)
        self.accelerate(random.uniform(10,20))
        self.mSpinRate = random.uniform(-90,90.0)
        self.setPolygon(self.createRandomPolygon(30, 8))
        return
        

    def getX(self):
        return self.mX
    def getY(self):
        return self.mY
    def getDX(self):
        return self.mDX
    def getDY(self):
        return self.mDY
    def getWorldWidth(self):
        return self.mWorldWidth
    def getWorldHeight(self):
        return self.mWorldHeight
    def getRotation(self):
        return self.mRotation

    def createRandomPolygon(self, radius, number_of_points):
        tuples = []
        np = number_of_points
        p = (360//np)
        for i in range(0,360,p):
            r = radius * random.uniform(.7,1.3)
            point = (r * math.cos(math.radians(i)),r * math.sin(math.radians(i)))
            tuples.append(point)
        return tuples

    def getSpinRate(self):
        return self.mSpinRate

    def setSpinRate(self, spin_rate):
        self.mSpinRate = spin_rate

    def evolve(self, dt):
        
        self.rotate(self.getSpinRate() * dt)
        self.move(dt)
