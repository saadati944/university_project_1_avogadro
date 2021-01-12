import sys
from stdlibrary import picture, color


class Blob:
    pixels = []

    def add(self, x, y):
        '''
        add one pixle to pixels list
        '''
        if [x, y] not in self.pixels:
            self.pixels.append([x, y])

    def mass(self):
        '''
        return mass of the Blob
        '''
        return len(self.pixels)

    def distanceTo(self, c):
        pass

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
        pass

    def getBeads(self, min_pixels):
        pass


def main():
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    input_file = sys.argv[3]

    bf = BeadFinder(input_file, tau)

    for blb in bf.getBeads(min_pixels):
        print(blb)
