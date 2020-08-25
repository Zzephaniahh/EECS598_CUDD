# Type your name, UMID, assignment number (single decimal digit), and problem and part number (e.g. 1c)
# Name:
# UMID:
# Assignment: 1
# Problem: 1a

# The following instructions import all necessary files to allow repycudd to run
# You need to replace PATH_TO with the path to the repycudd directory on your machine
import sys
import os
sys.path.append(os.path.abspath("/PATH_TO/shuffle_example/"))	# lib path to the shuffle.py directory
from shuffle import *		# import shuffle functions
import repycudd			# import cudd

# Access to BDD operations must be through a so-called BDD manager.
# The following instructions creates a manager called mgr
mgr = repycudd.DdManager()

"""
To create and print a BDD you need to:
1. Create variables
2. Create functions in terms of these variables
3. Put these functions in a function array to enable the construction of a multi-rooted BDD
4. Dump the function array into a .dot file which can be visualized with the unix dot command
"""

# Create variables
# Variable names can be arbitrary strings that start with a letter.
a = mgr.IthVar(0)
b = mgr.IthVar(1)
c = mgr.IthVar(2)

# Create functions.
# The sample functions here are f = (a | (~b & c)) and g = (b xor c) & a
# For complex expressions, it is better to build the functions incrementally for better readability
# This is uncessary for these sample functions, but is presented here (for function g) for illustration purposes
f = mgr.Or(a, mgr.And(mgr.Not(b), c))
g = mgr.Xor(b, c)
g = mgr.And(g, a)

# Create function array for printing to a .dot file
# You need to specify the size of the array (2 in this case), and push the functions into the array
# CUDD labels the resulting BDD with variable numbers instead of names.
# It also labels the functions F0, F1, etc. based on the order in which they were pushed into the function array.
farray = repycudd.DdArray(mgr,2)
farray.Push(mgr.BddToAdd(f))
farray.Push(mgr.BddToAdd(g))

# Generate BDD
# If you want to generate a BDD using your variable and function names, simply open the .dot file with a text editor
# and use find/replace to map back variable and function numbers to their names.
mgr.DumpDotArray(farray, "repycudd_template.dot")
