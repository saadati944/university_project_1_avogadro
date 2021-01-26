# Estimate Avogadro

This is my first university project and I should calculate the Avogadro number according to displacements of some blobs in water.

The original name is : `the Princeton University Atomic Nature of Matter problem.`

For more information about this project, take a look at these files :

- refrence : `atomic_nature_of_matter.pdf`
- persian : `Atomic-Nature.pdf`

## how to run ?

just open a terminal window and execute this command
```bash
python3 beadtracker.py 25 180.0 25.0 ./testCase_1/frame00* | python3 avogadro.py
```

And if you want to measure execution time, use the following code
```bash
time (python3 beadtracker.py 25 180.0 25.0 ./testCase_1/frame00* | python3 avogadro.py)
```

sample output
```
Boltzman : 1.2557e-23 
Avogadro : 6.6210e+23
```
and measured time :
> 68.70s user 0.12s system 92% cpu 1:14.23 total

## requirements

1. **python3**
1. **pygame**

installing pygame :
```
python3 -m pip install pygame
```
