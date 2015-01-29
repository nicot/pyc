.globl main
main:
pushl %ebp
movl %esp, %ebp
subl $32,%esp
call input
movl %eax, -4(%ebp)
movl -4(%ebp), %eax
movl %eax, -8(%ebp)
movl $1, %eax
movl %eax, -12(%ebp)
movl -12(%ebp), %eax
movl %eax, -8(%ebp)
movl $2, %eax
movl %eax, -16(%ebp)
movl -8(%ebp), %eax
movl %eax, -20(%ebp)
movl -16(%ebp), %eax
movl %eax, %edx
movl -20(%ebp), %eax
addl %edx, %eax
movl %eax, -24(%ebp)
movl -24(%ebp), %eax
movl %eax, -28(%ebp)
movl -28(%ebp), %eax
movl %eax, -32(%ebp)
movl -32(%ebp), %eax
pushl %eax
call print_int_nl
addl $4, %esp
movl $0, %eax
leave
ret
