.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $24,%esp
movl $4, %eax
movl %eax, -4(%ebp)
movl $5, %eax
movl %eax, -8(%ebp)
movl -8(%ebp), %eax
negl %eax
movl %eax, -12(%ebp)
movl -4(%ebp), %eax
movl %eax, %edx
movl -12(%ebp), %eax
addl %edx, %eax
movl %eax, -16(%ebp)
movl $100, %eax
movl %eax, -8(%ebp)
movl -8(%ebp), %eax
negl %eax
movl %eax, -12(%ebp)
movl $50, %eax
movl %eax, -16(%ebp)
movl -16(%ebp), %eax
negl %eax
movl %eax, -20(%ebp)
movl -12(%ebp), %eax
movl %eax, %edx
movl -20(%ebp), %eax
addl %edx, %eax
movl %eax, -24(%ebp)
movl -24(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
