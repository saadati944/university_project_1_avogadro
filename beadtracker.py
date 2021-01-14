import sys
import beadfinder

delta = 0


def detect_displacement(beads1, beads2):
    '''
    calculate the displacement of each blob between two frames
    '''
    global delta

    for i in range(len(beads1)):
        
        min_distance = delta+1

        # find minimum distance between the
        # beads[i] and one of the beads2
        for j in range(len(beads2)):
            #calculate distance
            d = beads1[i].distanceTo(beads2[j])
            if d < min_distance and d <= delta:
                min_distance = d
        
        # print min_distance only when the blob
        # moves less than the delta
        if min_distance != delta+1:
            print(min_distance)


def main():
    global delta
    '''
    get min_pixels, tau, delta, filenames ...
    from the standard input and trace beads movements
    '''
    # get data from stdin
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    files = sys.argv[4:]

    # find beads in the pictures
    blobs = []
    for f in files:
        bf = beadfinder.BeadFinder(f, tau)
        blobs.append(bf.getBeads(min_pixels))

    # pass each to continues frame to detect_displacement function
    for i in range(len(blobs)-1):
        detect_displacement(blobs[i], blobs[i+1])


if __name__ == "__main__":
    main()
