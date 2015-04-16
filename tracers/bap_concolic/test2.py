import sys
sys.path.append("../../static2/")
sys.path.append("../../middleware/")

from z3 import *
from bitvector import *
from concolic_executor import *
from bap import *

from copy import copy

def test(regs, instructions, constraints):
  def fetch_mem(addr, size):
      return "\x00"*size

  old_regs = copy(regs)

  executor = ConcolicExecutor(State(regs, fetch_mem), "EIP")
  for i in disasm(instructions):
    adt.visit(executor, i.bil)

  s1 = Solver()
  s2 = Solver()
  for key in constraints:
    cons1 = (executor.state[key] == constraints[key])
    cons2 = (executor.fork.state[key] == constraints[key])
    s1.add(cons1)
    s2.add(cons2)

  for cons in executor.constraints:
    s1.add(cons)

  for cons in executor.fork.constraints:
    s2.add(cons)

  if s1.check().r == 1:
    model = s1.model()
    return True, model
  elif s2.check().r == 1:
    model = s2.model()
    return True, model
  else:
    return False, None


"""
xor eax, ebx
xor ecx, eax
cmp eax, 0x1337b33f
jne 9
mov eax, 42
"""
# Try asking to make eax = 0x1337b33f.
# It should be unsat for only that value

code = "\x31\xD8\x31\xC1\x3D\x3F\xB3\x37\x13\x0F\x85\x05\x00\x00\x00\xB8\x2A\x00\x00\x00"
eax1 = SymbolicBitVector(8, BitVec("EAX1", 8))
eax2 = SymbolicBitVector(8, BitVec("EAX2", 8))
eax3 = SymbolicBitVector(8, BitVec("EAX3", 8))
eax4 = SymbolicBitVector(8, BitVec("EAX4", 8))

ecx1 = SymbolicBitVector(8, BitVec("ECX1", 8))
ecx2 = SymbolicBitVector(8, BitVec("ECX2", 8))
ecx3 = SymbolicBitVector(8, BitVec("ECX3", 8))
ecx4 = SymbolicBitVector(8, BitVec("ECX4", 8))

regs = {"EAX": eax1.concat(eax2).concat(eax3).concat(eax4),
        "EBX": ConcreteBitVector(32, 6),
        "ECX": ecx1.concat(ecx2).concat(ecx3).concat(ecx4)}

print test(regs, code, {"EAX": int(sys.argv[1], 16), "ECX": int(sys.argv[2], 16)})
