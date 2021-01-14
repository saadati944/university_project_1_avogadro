import math


class Blob:
    '''
    The blob object contains the coordinates of connected pixels.
    '''

    def __init__(self):
        '''
        create new instance of blob object
        '''
        self.xs = 0
        self.ys = 0
        self.pixels = []

    def check_new_pixel(self, x, y):
        '''
        Check if the [x, y] is in the list of pixels
        '''
        return [x, y] in self.pixels

    def add(self, x, y):
        '''
        add one pixle to pixels list
        '''
        if not self.check_new_pixel(x, y):
            self.pixels.append([x, y])
            self.xs += x
            self.ys += y

    def mass(self):
        '''
        return mass of the Blob
        '''
        return len(self.pixels)

    def distanceTo(self, c):
        '''
        calculate distance to another Blob
        formula :
            d = radical( (x2-x1)^2 + (y2-y1)^2)
        '''
        center1 = self.center()
        center2 = c.center()
        return math.sqrt((center2[0]-center1[0])**2 + (center2[1] - center1[1])**2)

    def center(self):
        '''
        return center of the Blob
        '''
        return self.xs/len(self.pixels), self.ys/len(self.pixels)

    def __str__(self):
        center = self.center()
        return "{mass} ({x:.4f}, {y:.4f})".format(mass=self.mass(), x=center[0], y=center[1])


def main():
    '''
    test blob object
    '''
    import random

    b = Blob()
    for i in range(random.randrange(100, 200)):
        b.add(random.random()*20, random.random()*20)

    c = Blob()
    for i in range(random.randrange(100, 200)):
        c.add(random.random()*20, random.random()*20)

    print('first blob :', b)
    print('second blob :', c)
    print('distance from b to c :', b.distanceTo(c))
    print('distance from b to c :', c.distanceTo(b))


if __name__ == "__main__":
    main()
