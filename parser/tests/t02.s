.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $20,%esp
movl $100, %eax
movl %eax, -4(%ebp)
movl $2, %eax
movl %eax, -8(%ebp)
movl -4(%ebp), %eax
movl %eax, %edx
movl -8(%ebp), %eax
addl %edx, %eax
movl %eax, -12(%ebp)
movl -12(%ebp), %eax
movl %eax, -16(%ebp)
movl -16(%ebp), %eax
movl %eax, -20(%ebp)
movl -20(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
