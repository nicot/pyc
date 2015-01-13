.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $16,%esp
call input
movl %eax, -4(%ebp)
movl $20, %eax
movl %eax, -8(%ebp)
movl -8(%ebp), %eax
movl %eax, -12(%ebp)
movl -12(%ebp), %eax
movl %eax, -16(%ebp)
movl $0, %eax
leave
ret
