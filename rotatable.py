import movable
import math

class Rotatable(movable.Movable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        movable.Movable.__init__(self, x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation
        return

    def getRotation(self):
        return self.mRotation
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
    
    def rotate(self, delta_rotation):
        self.mRotation += delta_rotation
        if self.mRotation < 0:
            self.mRotation = 360 + self.mRotation
        elif self.mRotation >= 360:
            self.mRotation = self.mRotation - 360
            
    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        x = math.cos(math.radians(rotation)) * delta_velocity
        y = math.sin(math.radians(rotation)) * delta_velocity
        return (x, y)
        
    def accelerate(self, delta_velocity):
        (a, b) = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        self.mDX += a
        self.mDY += b
        return
    
    def rotatePoint(self, x,y):
        (a,b) = (0,0)
        rad = math.radians(self.mRotation)
        x1 = x*math.cos(rad) - y*math.sin(rad)
        y1 = y*math.cos(rad) + x*math.sin(rad)
        a = x1
        b = y1
        return (a,b)
    
    def translatePoint(self, x,y):
        x += self.mX
        y += self.mY
        return (x, y)
    
    def rotateAndTranslatePoint(self, x,y):
        point = self.rotatePoint(x,y)
        point = self.translatePoint(point[0], point[1])
        return point
    
    def rotateAndTranslatePointList(self, point_list):
        new_points = []
        for points in point_list:
            points = self.rotateAndTranslatePoint(points[0],points[1])
            new_points.append(points)
        return new_points
