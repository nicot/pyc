.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $100,%esp
movl $1, %eax
movl %eax, -4(%ebp)
movl -4(%ebp), %eax
movl %eax, -8(%ebp)
movl $10, %eax
movl %eax, -12(%ebp)
movl -12(%ebp), %eax
movl %eax, -16(%ebp)
movl -16(%ebp), %eax
movl %eax, -20(%ebp)
movl -20(%ebp), %eax
movl %eax, -24(%ebp)
movl -16(%ebp), %eax
movl %eax, -28(%ebp)
movl -28(%ebp), %eax
movl %eax, -32(%ebp)
movl -8(%ebp), %eax
movl %eax, -36(%ebp)
movl -36(%ebp), %eax
movl %eax, -40(%ebp)
movl -16(%ebp), %eax
movl %eax, -44(%ebp)
movl -44(%ebp), %eax
movl %eax, -48(%ebp)
movl -16(%ebp), %eax
movl %eax, -52(%ebp)
movl $3, %eax
movl %eax, -56(%ebp)
movl -52(%ebp), %eax
movl %eax, %edx
movl -56(%ebp), %eax
addl %edx, %eax
movl %eax, -60(%ebp)
call input
movl %eax, -64(%ebp)
movl -60(%ebp), %eax
movl %eax, %edx
movl -64(%ebp), %eax
addl %edx, %eax
movl %eax, -68(%ebp)
movl -8(%ebp), %eax
movl %eax, -72(%ebp)
movl -72(%ebp), %eax
movl %eax, -76(%ebp)
movl -16(%ebp), %eax
movl %eax, -80(%ebp)
movl -80(%ebp), %eax
movl %eax, -84(%ebp)
movl -32(%ebp), %eax
movl %eax, -88(%ebp)
movl -88(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl -24(%ebp), %eax
movl %eax, -92(%ebp)
movl -92(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl -76(%ebp), %eax
movl %eax, -96(%ebp)
movl -96(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl -84(%ebp), %eax
movl %eax, -100(%ebp)
movl -100(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
