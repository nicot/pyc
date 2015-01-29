.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $76,%esp
call input
movl %eax, -4(%ebp)
movl -4(%ebp), %eax
negl %eax
movl %eax, -8(%ebp)
call input
movl %eax, -12(%ebp)
movl -12(%ebp), %eax
negl %eax
movl %eax, -16(%ebp)
movl -8(%ebp), %eax
movl %eax, %edx
movl -16(%ebp), %eax
addl %edx, %eax
movl %eax, -20(%ebp)
movl $1, %eax
movl %eax, -24(%ebp)
movl -20(%ebp), %eax
movl %eax, %edx
movl -24(%ebp), %eax
addl %edx, %eax
movl %eax, -28(%ebp)
movl $10, %eax
movl %eax, -32(%ebp)
movl -32(%ebp), %eax
negl %eax
movl %eax, -36(%ebp)
movl -28(%ebp), %eax
movl %eax, %edx
movl -36(%ebp), %eax
addl %edx, %eax
movl %eax, -40(%ebp)
movl -40(%ebp), %eax
movl %eax, -44(%ebp)
movl -44(%ebp), %eax
movl %eax, -48(%ebp)
movl -44(%ebp), %eax
movl %eax, -52(%ebp)
movl -48(%ebp), %eax
movl %eax, %edx
movl -52(%ebp), %eax
addl %edx, %eax
movl %eax, -56(%ebp)
movl -44(%ebp), %eax
movl %eax, -60(%ebp)
movl -60(%ebp), %eax
negl %eax
movl %eax, -64(%ebp)
movl -56(%ebp), %eax
movl %eax, %edx
movl -64(%ebp), %eax
addl %edx, %eax
movl %eax, -68(%ebp)
movl -68(%ebp), %eax
movl %eax, -72(%ebp)
movl -72(%ebp), %eax
movl %eax, -76(%ebp)
movl -76(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
