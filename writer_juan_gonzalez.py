#!/usr/bin/env python3
#writer.py
import sys
import random

count = 15  # I choose 15 because why not honestly 
function = "nop_slide"
choices = ['nop', 'fnop']  # just the choices the assignment told us to do

def main():
    #Changed the open function a bit but not by much
    with open(f"{function}.S", 'w') as f:
        # Directives.
        f.write("  .text\n\n")
        f.write(f"  .global {function}\n")
        f.write(f"  .type   {function}, @function\n")
        f.write(f"{function}:\n")
        # Function prologue.
        f.write("  pushq %rbp\n")
        f.write("  movq %rsp, %rbp\n")

        # Read TSC - start.
        f.write("  rdtscp\n")
        f.write("  movl %eax, %ebx\n")

        # Function prologue.
        for _ in range(count):
            instruction = random.choice(choices)  
            f.write(f"  {instruction}\n")

        
        f.write("  rdtscp\n")
        f.write("  subl %ebx, %eax\n")

        # Function epilogue.
        f.write("  popq %rbp\n")
        f.write("  retq\n")

if __name__ == "__main__":
    main()

