.text

.global _start

_start:
  xor %eax, %eax
  xor %ebx, %ebx
  xor %ecx, %ecx
  xor %edx, %edx
  lea str, %edx
  mov %eax, (%edx)
  xor %eax, %eax
  xor %ebx, %ebx
  xor %ecx, %ecx
  xor %edx, %edx
  mov $0x1, %eax
  int $0x80


.data
str:
  .string "hack4lyfe"
