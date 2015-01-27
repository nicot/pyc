.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $4,%esp
movl $129, %eax
movl %eax, -4(%ebp)
movl -4(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
