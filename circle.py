import rotatable
import pygame

class Circle(rotatable.Rotatable):
    def __init__(self,x,y,dx,dy,rotation,radius,world_width,world_height):
        rotatable.Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height)

        self.mRadius = radius
        self.mColor = (255,255,255)

    def getRadius(self):
        return self.mRadius

    def getColor(self):
        return self.mColor

    def setRadius(self, radius):
        if radius >= 1:
            self.mRadius = radius
            return self.mRadius
        else:
            return False

    def setColor(self, color):
        self.mColor = color
        return

    def draw(self, surface):
        return

    def draw( self, surface ):
        color = self.mColor
        center = ( int( self.mX ), int( self.mY ) )
        pygame.draw.circle( surface, color, center, int( self.mRadius ), 0 )
        return
