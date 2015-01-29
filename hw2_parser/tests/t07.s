.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $36,%esp
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
movl %eax, -20(%ebp)
movl -20(%ebp), %eax
negl %eax
movl %eax, -24(%ebp)
movl $50, %eax
movl %eax, -28(%ebp)
movl -28(%ebp), %eax
negl %eax
movl %eax, -32(%ebp)
movl -24(%ebp), %eax
movl %eax, %edx
movl -32(%ebp), %eax
addl %edx, %eax
movl %eax, -36(%ebp)
movl -36(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
