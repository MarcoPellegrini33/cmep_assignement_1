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

from matplotlib import pyplot as plt
import numpy as np

def hist(xdatas,frequencies,figname):
    '''plot a histogram of xdatas'
       frequencies. Histogram will be
       saved as 'figname'
    '''
    plt.bar(xdatas,frequencies)
    plt.savefig(figname)
    plt.show()

