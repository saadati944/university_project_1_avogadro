import sys
import beadfinder

def main():
    '''
    get min_pixels, tau, delta, filenames ...
    from the standard input and trace beads movements
    '''
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    files = sys.argv[4:]

    # find beads in the pictures
    blobs = []
    for f in files:
        bf = beadfinder.BeadFinder(f, tau)
        blobs.append(bf.getBeads(min_pixels))

    for beads in blobs:
        print("+++++++++++++++++++++++++++++++")
        for b in beads:
            print(b)


if __name__ == "__main__":
    main()