from z3 import *
from bitvector import *

a = ConcreteBitVector(8, 38)
x = SymbolicBitVector(8, BitVec("x", 8))
y = SymbolicBitVector(8, BitVec("y", 8))

exp = (((a ^ x & (y ^ x)) % 3) >> 3) + (x|y)*2
exp2 = ((((y * 4) & a) ^ x) % 115) >> 2

exp = exp2.get_bits(1,6).concat(exp.get_bits(3,7))

s = Solver()
constraint = exp.expr == 3223
s.add(constraint)
print s.check()
print s.model()
