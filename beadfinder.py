import sys
from stdlibrary import picture, color
import blob


class BeadFinder:
    def __init__(self, pic, tau):
        '''
        create new instance of beadfinder object
        and initialization self.pic and self.tau
        '''
        self.tau = tau
        self.pic = picture.Picture(pic)
        self.blobs = []
        # filter the pic and delete the extras
        # self.__filter()
        # find all beads
        self.__findBeads()

    def __getavg(self, clr):
        '''
        calculate average of R, G, B values of a color
        like converting colors to gray scale
        '''
        return (clr.getRed()+clr.getGreen()+clr.getBlue())/3

    def __detect_blob(self, blob, x, y):
        '''
        detect blob

        How this function works:
        - If the pixel [x, y] is already added to the list, return.
        - If the pixel [x, y] is not white, return.
        - Add pixel [x, y] to the list.
        - Check back all four neighbor pixels [x, y] (if possible).
        '''
        # only check red because after filtering the pic,
        # the red, green and blue values are the same
        if self.__getavg(self.pic.get(x, y)) >= self.tau:
            # return if pixel was added before
            if blob.check_new_pixel(x, y):
                return
            blob.add(x, y)
        else:
            # return if pixel was black
            return

        # check all neighbor pixels
        w = self.pic.width()
        h = self.pic.height()
        if x > 0:
            self.__detect_blob(blob, x-1, y)
        if x < w-1:
            self.__detect_blob(blob, x+1, y)
        if y > 0:
            self.__detect_blob(blob, x, y-1)
        if y < h - 1:
            self.__detect_blob(blob, x, y+1)

    def __findBeads(self):
        '''
        this function will find all beads in the pic step by step :

        1. filter images
        2. scan rows and find first white pixel
        3. detect_blob according to that white pixel
        4. continue scanning from first black pixel after that white pixel
        '''
        # rows
        for y in range(self.pic.height()):

            # this variable will remember whether the last pixel checked is white or not
            last_pixel_was_white = False

            # columns
            for x in range(self.pic.width()):

                if self.__getavg(self.pic.get(x, y)) >= self.tau:
                    # if last checked pixel was white so this pixel was added to a blob before
                    # and there is no need to re-check
                    if last_pixel_was_white:
                        continue

                    # if this pixel has already been added to a blob
                    # then there is no need to re-check
                    duplicate_pixel = False
                    for b in self.blobs:
                        if b.check_new_pixel(x, y):
                            last_pixel_was_white = True
                            duplicate_pixel = True
                            break
                    if duplicate_pixel:
                        continue

                    # detect new blob and add it to blobs list
                    new_blob = blob.Blob()
                    self.__detect_blob(new_blob, x, y)
                    self.blobs.append(new_blob)
                    last_pixel_was_white = True
                else:
                    last_pixel_was_white = False

    def getBeads(self, min_pixels):
        '''
        return blobs with at least min_pixels of pixels
        '''
        return [b for b in self.blobs if b.mass() >= min_pixels]


def main():
    '''
    main function
    pass parameters in this format :
    $python beadfinder.py min_pixels threshold filename 
    '''
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    input_file = sys.argv[3]

    bf = BeadFinder(input_file, tau)

    for blb in bf.getBeads(min_pixels):
        print(blb)


if __name__ == "__main__":
    main()
