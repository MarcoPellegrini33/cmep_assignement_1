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

''' Program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in the
book.
'''


import numpy as np
import argparse
import letter_counter
import histogram
import time


parser = argparse.ArgumentParser(description='Print some book statistics')
parser.add_argument('infile', type=str, help='path to the input file')
args = parser.parse_args()

t0 = time.process_time()
'''open file
'''
input_file = open(args.infile,'r')
book = input_file.read().lower()


alphabeth=[
           'a','b','c','d','e','f','g','h',
           'i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z']


k=np.full(len(alphabeth),0)

'''count number of letters
'''
for i in range(len(alphabeth)):
    k[i] = letter_counter.letter_count(alphabeth[i],book)


frequency = k/np.sum(k)

for i in range(len(alphabeth)):
    print('relative frequency of letter', alphabeth[i], 'is', frequency[i])

'''uncomment to see letters' frequencies
print(k)
'''

print('warning: this program does not distinguish lower and upper case.')

'''print a histogram of letters'
   frequencies
'''
histogram.hist(alphabeth,k,'book_histo')

t_elapsed = time.process_time() - t0

print('time elapsed =',t_elapsed)



