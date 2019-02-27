import ship
import rock
import rotatable
import polygon
import pygame
import random
import star
import bullet
import sys

class Asteroids:
    def __init__(self, world_width, world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = ship.Ship(300, 300, world_width, world_height)
        self.mRocks = []
        self.mObjects = []
        self.mBullets = []
        self.mStars = []
        for i in range(20):
            x = random.randint(0, self.mWorldWidth)
            y = random.randint(0, self.mWorldHeight)
            self.mStars.append(star.Star(x, y, world_width, world_height))
        #add randrange for x and y
        for i in range(10):
            x = random.randint(0, self.mWorldWidth)
            y = random.randint(0, self.mWorldHeight)
            self.mRocks.append(rock.Rock(x,y, world_width, world_height))
        self.mObjects = self.mRocks + self.mStars + [self.mShip]
        return

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getBullets(self):
        return self.mBullets

    def getStars(self):
        return self.mStars

    def getObjects(self):
        return self.mObjects

    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
        return

    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
        return

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
        return

    def fire(self):
        if len(self.mBullets) < 3:
            x = self.mShip.fire()
            self.mBullets.append(x)
            self.mObjects.append(x)
            return

    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)

    def collideShipAndBullets(self):
        for bullet in self.mBullets:
            if self.mShip.hits(bullet):
                self.mShip.setActive(False)
        return

    def collideShipAndRocks(self):
        for rock in self.mRocks:
            if self.mShip.hits(rock):
                self.mShip.setActive(False)
                print('Ship was destroyed')
        return

    def collideRocksAndBullets(self):
        if len(self.mBullets) >= 1:
            for bullet in self.mBullets:
                i = 0
                while i < len(self.mRocks):
                    if bullet.hits(self.mRocks[i]):
                        self.mRocks[i].setActive(False)
                        bullet.setActive(False)
                    i += 1
                
        else:
            return

    def removeInactiveObjects(self):
        for i in self.mObjects:
            if not i.getActive():
                if isinstance(i, rock.Rock):
                    self.mRocks.remove(i)
                    self.mObjects.remove(i)
                elif isinstance(i, bullet.Bullet):
                    self.mBullets.remove(i)
                    self.mObjects.remove(i)
                elif isinstance(i, ship.Ship):
                    self.mObjects.remove(i)
                    sys.exit(0)
                    

    def evolve(self, dt):
        if len(self.mRocks) == 0:
            print('You Won!')
            return
        self.evolveAllObjects(dt)
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.collideRocksAndBullets()
        self.removeInactiveObjects()

    def draw(self, surface):
        rect = pygame.Rect( int (0), int (0), int ( self.mWorldWidth), int ( self.mWorldHeight))
        pygame.draw.rect(surface,(0,0,0), rect,0)
        for star in self.mStars:
            star.draw(surface)
        self.mShip.draw(surface)
        for r in self.mRocks:
            r.draw(surface)
        for bullet in self.mBullets:
            bullet.draw(surface)
        return
