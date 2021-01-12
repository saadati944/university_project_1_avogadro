import sys
from stdlibrary import picture, color


class Blob:
    pixels = []

    def add(self, x, y):
        pass

    def mass(self):
        pass

    def distanceTo(self, c):
        pass

    def __str__(self):
        return str(len(self.pixels))


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
