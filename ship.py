import polygon
import bullet

class Ship(polygon.Polygon):

    def __init__(self, x, y, world_width, world_height):
        polygon.Polygon.__init__(self, x, y, 0, 0, 0, world_width, world_height)
        self.setPolygon([(30,0), (-10, 15), (-10,-15)])
        self.mActive = True
        return

    def fire(self):
        a = self.getPolygon()[0]
        a = self.rotateAndTranslatePoint(a[0],a[1])
        b = bullet.Bullet(a[0], a[1],0, 0, self.getRotation(), self.mWorldWidth, self.mWorldHeight)
        return b
    def evolve(self, dt):
        self.move(dt)
        return
