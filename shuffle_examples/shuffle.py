import repycudd
def pylist_to_intarray(lst):
    res = repycudd.IntArray(len(lst))
    for i, x in enumerate(lst):
        res[i] = x
    return res

def intarray_tostr(array):
    res = []
    for i in range(len(array)):
       res.append(str(array[i]))
    return 'IntArray(%s)' % (', '.join(res))
