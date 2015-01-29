.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $40,%esp
movl $5, %eax
movl %eax, -4(%ebp)
call input
movl %eax, -8(%ebp)
movl -4(%ebp), %eax
movl %eax, %edx
movl -8(%ebp), %eax
addl %edx, %eax
movl %eax, -12(%ebp)
movl $6, %eax
movl %eax, -16(%ebp)
movl -16(%ebp), %eax
negl %eax
movl %eax, -20(%ebp)
movl -12(%ebp), %eax
movl %eax, %edx
movl -20(%ebp), %eax
addl %edx, %eax
movl %eax, -24(%ebp)
call input
movl %eax, -28(%ebp)
movl -24(%ebp), %eax
movl %eax, %edx
movl -28(%ebp), %eax
addl %edx, %eax
movl %eax, -32(%ebp)
movl -32(%ebp), %eax
movl %eax, -36(%ebp)
movl -36(%ebp), %eax
movl %eax, -40(%ebp)
movl -40(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
