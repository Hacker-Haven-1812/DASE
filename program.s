.section .text
.global _start
_start:
li x1, 200
li x2, 13
li x3, 800
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
add x1, x1, x2
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
sw x1, 0(x3)
lw x4, 0(x3)
loop:
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
addi x1, x1, -1
bne x1, x0, loop
or x5, x2, x4
and x5, x2, x4
srl x5, x2, x4
and x5, x2, x4
sub x5, x2, x4
sub x5, x2, x4
srl x5, x2, x4
and x5, x2, x4
or x5, x2, x4
sll x5, x2, x4
and x5, x2, x4
srl x5, x2, x4
sub x5, x2, x4
add x5, x2, x4
or x5, x2, x4
xor x5, x2, x4
sub x5, x2, x4
add x5, x2, x4
and x5, x2, x4
srl x5, x2, x4
sll x5, x2, x4
sll x5, x2, x4
add x5, x2, x4
and x5, x2, x4
or x5, x2, x4
or x5, x2, x4
sll x5, x2, x4
sll x5, x2, x4
and x5, x2, x4
sll x5, x2, x4
sub x5, x2, x4
and x5, x2, x4
add x5, x2, x4
srl x5, x2, x4
and x5, x2, x4
add x5, x2, x4
add x5, x2, x4
add x5, x2, x4
sub x5, x2, x4
sub x5, x2, x4
and x5, x2, x4
add x5, x2, x4
srl x5, x2, x4
or x5, x2, x4
xor x5, x2, x4
or x5, x2, x4
and x5, x2, x4
srl x5, x2, x4
sub x5, x2, x4
and x5, x2, x4
sub x5, x2, x4
sll x5, x2, x4
xor x5, x2, x4
or x5, x2, x4
add x5, x2, x4
sll x5, x2, x4
add x5, x2, x4
or x5, x2, x4
sll x5, x2, x4
j _start
