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

'''Funzione che conta il numero di volte in cui una lettera compare in una stringa
'''
def letter_count(letter,book):
    counter=0
    for i in range(len(book)) :
        if book[i]==letter:
            counter+=1
    return counter











