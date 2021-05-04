import os
import random
os.chdir('BocchettiPy\Haiku')

with open('Versi da 5.txt') as f1, open('Versi da 7.txt') as f2:
    for line1, line2, line3 in zip(f1, f2):
        print(line1+line2+line3)
