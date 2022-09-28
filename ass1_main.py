''''!/usr/bin/env python
Copyright (C) 2022 m.pellegrini33@studenti.unipi.it

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import numpy as np
import argparse
import letter_counter

alphabeth=[
           'a','b','c','d','e','f','g','h',
           'i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','z','x']

upper_alphabeth=[
                 'A','B','C','D','E','F','G',
                 'H','I','J','K','L','M','N',
                 'O','P','Q','R','S','T','U','V','W','Z','X']

k=np.full(len(alphabeth),0)
K=np.full(len(alphabeth),0)

parser = argparse.ArgumentParser(description='Print some book statistics')
parser.add_argument('infile', type=str, help='path to the input file')
args = parser.parse_args()


input_file=open(args.infile,'r')
book=input_file.read()

'''count numer of letters
'''


for i in range(len(alphabeth)):
    k[i]=letter_counter.letter_count(alphabeth[i],book)

for i in range(len(alphabeth)):
    K[i]=letter_counter.letter_count(upper_alphabeth[i],book)

f=(k+K)/(np.sum(k)+np.sum(K))



for i in range(len(alphabeth)):
    print('relative frequency of letter', alphabeth[i], 'is', f[i])

print('warning: this program does not distinguish lower and upper case.')


