import sys
import math
from stdlibrary import picture, color


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


class BeadFinder:
    def __init__(self, pic, tau):
        '''
        create new instance of beadfinder object
        and initialization self.pic and self.tau
        '''
        self.tau = tau
        self.pic = picture.Picture(pic)
        self.blobs = []

    def __getavg(self, clr):
        '''
        calculate average of R, G, B values of a color
        like converting colors to gray scale
        '''
        return (clr.getRed()+clr.getGreen()+clr.getBlue())/3

    def __filter(self):
        '''
        filter pic according to threshold
        colors under tau => black
        colors above tau => white
        '''
        for i in range(self.pic.width()):
            for j in range(self.pic.height()):
                if self.__getavg(self.pic.get(i, j)) < self.tau:
                    self.pic.set(i, j, color.Color(0, 0, 0))
                else:
                    self.pic.set(i, j, color.Color(255, 255, 255))

    def getBeads(self, min_pixels):
        '''
        this function will find all beads in the pic step by step :

        1. filter images
        2. scan rows and find first white pixel
        3. detect_blob according to that white pixel
        4. continue scanning from first black pixel after that white pixel
        '''
        self.__filter()
        for y in range(self.pic.height()):
            for x in range(self.pic.width()):
                pass


def main():
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    input_file = sys.argv[3]

    bf = BeadFinder(input_file, tau)

    for blb in bf.getBeads(min_pixels):
        print(blb)
