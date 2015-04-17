.global _start

_start:
  xor %eax, %eax
  xor %ebx, %ebx
  xor %ecx, %ecx

  add $0x4, %eax
  imul %ecx, %eax
  sub %ebx, %eax

  xor %eax, %eax
  xor %ebx, %ebx
  xor %ecx, %ecx
  mov $0x1, %eax
  int $0x80
