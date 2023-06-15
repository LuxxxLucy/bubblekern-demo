#!/usr/bin/env python

import string

li = list(string.ascii_lowercase) + list(string.ascii_uppercase)

from itertools import product
ret = ";".join([','.join(comb) for comb in product(li, repeat=2)])
print(ret)
