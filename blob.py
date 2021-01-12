import math


class Blob:
    '''
    The blob object contains the coordinates of connected pixels.
    '''

    def __init__(self):
        '''
        create new instance of blob object
        '''
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
        xs = 0
        ys = 0
        for p in self.pixels:
            xs += p[0]
            ys += p[1]
        return xs/len(self.pixels), ys/len(self.pixels)

    def __str__(self):
        return f"{str(len(self.pixels))} {self.center()}"
