import rotatable
import pygame
import math

class Polygon(rotatable.Rotatable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        rotatable.Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height)
        self.mOriginalPolygon = []
        self.mColor = (255, 255, 255)

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
    def getPolygon(self):
        return self.mOriginalPolygon
    def getColor(self):
        return self.mColor

    def setPolygon(self, point_list):
        self.mOriginalPolygon = point_list
        return

    def setColor(self, color):
        self.mColor = color
        return

    def draw(self, surface):
        point_list = self.mOriginalPolygon
        new_point_list = self.rotateAndTranslatePointList(point_list)
        color = self.mColor
        pygame.draw.polygon(surface, color, new_point_list,1)
        return

    def getRadius(self):
        d = 0
        c = 0
        t = 0
        if len(self.mOriginalPolygon) >= 1:
            for point in self.mOriginalPolygon:
                d = math.sqrt(point[0]*point[0] + point[1]*point[1])
                c += 1
                t += (d)
            return t/c
        else:
            return 0
            
        
