import math
import stdlibrary.stdio as stdio

def main():
    '''
    this function will receive resaults of beadtracker
    file and calculate the D. and according to this equation

           k T
    D = ―――――――――
         6 π Ƞ ρ

    calculate the k.
    k is the boltzmann constant

    and then calculate avogadro number with this formula

         R
    A = ―――
         k
    '''

    D = 0
    count=0
    while not stdio.isEmpty():
        D += stdio.readFloat()**2
        count += 1
    D /= 2*count
    D *= (175e-9)**2

    # boltzman constant
    k = (6 * D * math.pi * 9.135e-4 * 5e-7) / 297

    # print resaults
    print('Boltzman :', k, '\nAvogadro :', (8.31446/k))



if __name__ == "__main__":
    main()
