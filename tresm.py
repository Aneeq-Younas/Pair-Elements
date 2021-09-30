import itertools
from functools import partial

a = [10, 30, 20, 30, 10]
b = [20, 30, 40, 30, 30]
c = [30, 30, 20, 30, 40]
x = 80


def arr_num(ele, *y):
    if sum(i for i in y) == ele:
        return (True, y)

    else:
        return (False, y)


itr = itertools.product(a, b, c)
prt = partial(arr_num, x)
lst = list(itertools.starmap(prt, itr))

final = set()

for v in lst:
    if v[0] == True and v[1] not in final:
        final.add(v[1])
        print(final)