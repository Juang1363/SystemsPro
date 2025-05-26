  .text

  .global nop_slide
  .type   nop_slide, @function
nop_slide:
  pushq %rbp
  movq %rsp, %rbp
  rdtscp
  movl %eax, %ebx
  nop
  nop
  fnop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  fnop
  nop
  nop
  nop
  nop
  rdtscp
  subl %ebx, %eax
  popq %rbp
  retq
