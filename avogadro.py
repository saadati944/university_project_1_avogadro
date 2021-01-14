import math
import stdlibrary.stdio as stdio

def main():
    '''
    this function will receive resaults of beadtracker
    '''
    inp = input().split('\n')
    while not stdio.isEmpty():
        inp.append(stdio.readFloat())

    D = 0
    for i in inp:
        D += float(i)**2
    D /= 2*len(inp)
    D *= (175e-9)**2

    # boltzman constant
    k = (6 * D * math.pi * 9.135e-4 * 5e-7) / 297

    # print resaults
    print('Boltzman :', k, '\nAvogadro :', (8.31446/k))

    

if __name__ == "__main__":
    main()