import sys
import os
sys.path.append(os.path.abspath("/home/zephaniah/Documents/shuffle/EECS_598_lib"))
from shuffle import *
import repycudd
mgr = repycudd.DdManager()

# Define variables
x0 = mgr.IthVar(0)
y0 = mgr.IthVar(1)
x1 = mgr.IthVar(2)
y1 = mgr.IthVar(3)
x2 = mgr.IthVar(4)
y2 = mgr.IthVar(5)
x3 = mgr.IthVar(6)
y3 = mgr.IthVar(7)

t0 = mgr.And(x0, y0)
t1 = mgr.And(x1, y1)
t2 = mgr.And(x2, y2)
t3 = mgr.And(x3, y3)

f = mgr.Or(mgr.Or(t1,t0),mgr.Or(t2,t3))


size = 8
arr = pylist_to_intarray([0,2,4,6,1,3,5,7])
print(intarray_tostr(arr))

mgr.ShuffleHeap(arr)
r = mgr.BddToAdd(f)
mgr.DumpDot(r)
