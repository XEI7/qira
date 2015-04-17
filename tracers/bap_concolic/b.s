.global _start

_start:
  xor %eax, %eax
  xor %ebx, %ebx
  xor %ecx, %ecx

  add $0x4, %eax
  imul %ecx, %eax
  sub %ebx, %eax
  cmp $0x1337b33f, %eax
  jne around
  mov $0x42, %eax

around:
  xor %eax, %eax
  xor %ebx, %ebx
  xor %ecx, %ecx
  mov $0x1, %eax
  int $0x80
