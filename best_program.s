.section .text
.globl _start
_start:
add  x11, x9, x2
addi x5, x5, 23
addi x9, x1, 27
sub  x1, x9, x9
lw   x15, 0(x2)
lw   x2, 0(x13)
addi x12, x15, 28
sub  x5, x13, x2
xor  x3, x4, x11
sw   x14, 0(x7)
sub  x9, x3, x10
add  x10, x5, x2
lw   x7, 0(x14)
addi x3, x13, 28
add  x11, x4, x2
xor  x2, x6, x5
addi x8, x11, 25
addi x12, x1, 19
lw   x2, 0(x10)
sw   x12, 0(x14)
xor  x13, x14, x13
xor  x9, x7, x10
add  x10, x12, x3
addi x13, x13, 10
sw   x1, 0(x13)
lw   x7, 0(x3)
sw   x4, 0(x10)
sw   x13, 0(x1)
lw   x4, 0(x2)
sub  x2, x6, x3
add  x5, x7, x14
lw   x3, 0(x10)
sw   x6, 0(x15)
lw   x11, 0(x10)
sw   x5, 0(x8)
j _start