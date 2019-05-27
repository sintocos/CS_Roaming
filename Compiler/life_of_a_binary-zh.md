# Life of a binary

[英文版](<https://kishuagarwal.github.io/life-of-a-binary.html>)

待翻译

Almost every one of you must have written a program, compiled it and then ran it to see the fruits of your hard labour. It feels good to finally see your program working, isn’t it? But to make all of this work, we have someone else to thankful too. And that is your compiler (of course, assuming that you are working in a compiled language, not an interpreted one) which also does so much hard work behind the scenes.

In this article, I will try to show you how the source code that you write is transformed into something that your machine is actually able to run. I am choosing Linux as my host machine and C as the programming language here, but the concepts here are general enough to apply to many compiled languages out there.

**Note**: If you want to follow along in this article, then you will have to make sure that you have **gcc, elfutils**installed on your local machine.

Let’s start with a simple C program and see how it get’s converted by the compiler.

```c
#include <stdio.h>


// Main function
int main(void) {
    int a = 1;
    int b = 2;
    int c = a + b;
    printf("%d\n", c);
    return 0;
}
```

This program creates two variables, adds them up and print the result on the screen. Pretty simple, huh?

But let’s see what this seemingly simple program has to go through to finally get executed on your system.

Compiler has usually the following five steps (with the last step being part of the OS)-

![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/1.png>)

Let’s go through each of the step in sufficient detail.

![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/2.png>)First step is the **Preprocessing** step which is done by the Preprocessor. Job of the Preprocessor is to handle all the preprocessor directives present in your code. These directives start with **#**. But before it processes them, it first removes all the comments from the code as comments are there only for the human readability. Then it finds all the **#** commands, and does what the commands says.

In the code above, we have just used **#include** directive, which simply says to the Preprocesssor to copy the **stdio.h** file and paste it into this file at the current location.

You can see the output of the Preprocessor by passing **-E** flag to the **gcc** compiler.

```
gcc -E sample.c
```

You would get something like the following-

```
# 1 "sample.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "sample.c"


# 1 "/usr/include/stdio.h" 1 3 4


-----omitted-----




# 5 "sample.c"
int main(void) {
    int a = 1;
    int b = 2;
    int c = a + b;
    printf("%d\n", c);
    return 0;
}
```

![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/3.png>)

Confusingly, the second step is also called compilation. The compiler takes the output from the Preprocessor and is responsbile to do the following important tasks.

- Pass the output through a lexical analyser to identify various tokens present in the file. Tokens are just literals present in your program like ‘int’, ‘return’, ‘void’, ‘0’ and so on. Lexical Analyser also associates with each token the type of the token, whether the token is a string literal, integer, float, if token, and so on.
- Pass the output of the lexical analyser to the syntax analyser to check whether the program is written in a way that satisfy the grammar rules of the language the program is written in. For example, it will raise syntax error when parsing this line of code,

```
    b = a + ;
```

since **+** is a missing one operand.

- Pass the output of the syntax analyser to the semantic analyser, which checks whether the program satisfies semantics of the language like type checking and variables are declared before their first usage, etc.
- If the program is syntactically correct, then the source code is converted into the assembly intructions for the specified target architecture. By default, it generates assembly for the machine it is running on. But suppose, you are building programs for embedded systems, then you can pass the architecture of the target machine and gcc will generate assembly for that machine.

To see the output from this stage, pass the **-S** flag to the **gcc** compiler.

```
gcc -S sample.c
```

You would get something like the following depending upon on your environment.

```assembly
    .file   "sample.c"                              // name of the source file
    .section    .rodata                             // Read only data
.LC0:                                               // Local constant
    .string "%d\n"                                  // string constant we used
    .text                                           // beginning of the code segment
    .globl  main                                    // declare main symbol to be global
    .type   main, @function                         // main is a function
main:                                               // beginning of main function
.LFB0:                                              // Local function beginning
    .cfi_startproc                                  // ignore them
    pushq   %rbp                                    // save the caller's frame pointer
    .cfi_def_cfa_offset 16
    .cfi_offset 6, -16
    movq    %rsp, %rbp                              // set the current stack pointer as the frame base pointer
    .cfi_def_cfa_register 6
    subq    $16, %rsp                               // set up the space
    movl    $1, -12(%rbp)
    movl    $2, -8(%rbp)
    movl    -12(%rbp), %edx
    movl    -8(%rbp), %eax
    addl    %edx, %eax
    movl    %eax, -4(%rbp)
    movl    -4(%rbp), %eax
    movl    %eax, %esi
    movl    $.LC0, %edi
    movl    $0, %eax
    call    printf
    movl    $0, %eax
    leave
    .cfi_def_cfa 7, 8
    ret                                             // return from the function
    .cfi_endproc
.LFE0:
    .size   main, .-main                            // size of the main function
    .ident  "GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609"
    .section    .note.GNU-stack,"",@progbits        // make stack non-executable
```

If you don’t know assembly language, it all looks pretty scary at first, but it is not that bad. It takes more time to understand the assembly code than your normal high level language code, but given enough time, you can surely read it.

Let’s see what this file contains.

All the lines beginning with ‘.’ are the assembler directives. **.file** denotes the name of the source file, which can be used for debugging purposes. The string literal in our source code **%d\n** now resides in the **.rodata** section (ro means read-only), since it is a read only string. The compiler named this string as **LC0**, to later refer to it in the code. Whenever you see a label starting with .L, it means that those labels are local to the current file and will not visible to the other files.

**.globl** tells that main is a global symbol, which means that the main can be called from other files. **.type** tells that main is a function. Then follows the assembly for the main function. You can ignore the directives starting with **cfi**. They are used for call stack unwinding in case of exceptions. We will ignore them in this article, but you can know more about them [here](https://sourceware.org/binutils/docs/as/CFI-directives.html).

Let’s try to understand now the disassembly of the main function.

![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/4.png>)

**11**. You must be knowing that when you call a function, a new stack frame is created for that function. To make that possible, we need some way of knowing the start of the caller’s function frame pointer when the new function returns. That’s why we push the current frame pointer which is stored in the **rbp** register onto the stack.

**14** Move the current stack pointer into the base pointer. This becomes our current function frame pointer. Fig. 1 depicts the state before pushing the rbp register and Fig. 2 shows after the previous frame pointer is pushed and the stack pointer is moved to the current frame pointer.

**16** We have 3 local variables in our program, all of types int. On my machine, each int occupies 4 bytes, so we need 12 bytes of space on the stack to hold our local variables. The way we create space for our local variables on the stack, is decrement our stack pointer by the number of bytes we need for our local variables. Decrement, because stack grows from higher addresses to lower addresses. But here you see we are decrementing by 16 instead of 12. The reason is, space is allocated in the chunks of 16 bytes. So, even if you have 1 local variable, space of 16 byteswould be allocated on the stack. This is done for performance reasons on some architecures. See Fig. 3 to see how the stack is laid out right now.

**17-22** This code is pretty straight forward. The compiler has used the slot **rbp-12** as the storage for variable **a**, **rbp-8** for **b** and **rbp-4** for **c**. It moves the the values 1 and 2 to address of variable **a** and **b** respectively. To prepare for the addition, it moves the **b** value to **edx** register and the value of the **a** register to the **eax** register. The result of the addition is stored in the **eax** register which is later transferred to the address of the **c** variable.

**23-27** Then we prepare for our printf call. Firstly, the value of the **c** variable is moved to the **esi** register. And then address of our string constant **%d\n** is moved to the **edi** register. **esi** and **edi** registers now hold the argument of our printf call. **edi** holds the first argument and **esi** holds the second argument. Then we call the printf function to print the value of the variable **c** formatted as the integer value. Point to note here is that **printf** symbol is undefined at this point. We would see how this **printf** symbol gets resolved later on in this article.

**.size** tells the size of the main function in bytes. “**.-main**” is an expression where the **.** symbol means the address of the current line. So this expression evaluates to **current_address_of the line - address of the main function**which gives us the size of the main function in bytes.

**.ident** just tell the assembler to add the following line in the **.comment** section. **.note.GNU-stack** is used for telling whether the stack for this program is executable or not. Mostly the value for this directive is null string, which tells the stack is not executable.

![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/5.png>)What we have right now is our program in the assembly language, but it is still in the language which is not understood by the processors. We have to convert the assembly language to the machine language, and that work is done by the Assembler. Assembler takes your assembly file and produces an object file which is a binary file containing the machine instructions for your program.

Let’s convert our assembly file to the object file to see the process in action. To get the object file for your program, pass the **c** flag to the **gcc** compiler.

```
gcc -c sample.c
```

You would get a object file with an extension of **.o**. Since, this is a binary file, you won’t be able to open it in a normal text editor to view it’s contents. But we have tools at our disposal, to find out what is lying inside in those object files.

Object files could have many different file formats. We will be focussing on one in particular which is used on the Linux and that is the [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) file format.

ELF files contains following information-

- ELF Header
- Program header table
- Section header table
- Some other data referred to by the previous tables

**ELF Header** contains some meta information about the object file such as type of the file, machine against which binary is made, version, size of the header, etc. To view header, just pass **-h** flag to **eu-readelf** utility.

```shell
$ eu-readelf -h sample.o
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Ident Version:                     1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              REL (Relocatable file)
  Machine:                           AMD x86-64
  Version:                           1 (current)
  Entry point address:               0
  Start of program headers:          0 (bytes into file)
  Start of section headers:          704 (bytes into file)
  Flags:                             
  Size of this header:               64 (bytes)
  Size of program header entries:    0 (bytes)
  Number of program headers entries: 0
  Size of section header entries:    64 (bytes)
  Number of section headers entries: 13
  Section header string table index: 10
```

From the above listing, we see that this file doesn’t have any **Program Headers** and that is fine. **Program Headers**are only present in the executable files and shared libraries. We will see **Program Headers** when we link the file in the next step.

But we do have 13 sections. Let’s see what are these sections. Use the **-S** flag.

```shell
$ eu-readelf -S sample.o
There are 13 section headers, starting at offset 0x2c0:


Section Headers:
[Nr] Name                 Type         Addr             Off      Size     ES Flags Lk Inf Al
[ 0]                      NULL         0000000000000000 00000000 00000000  0        0   0  0
[ 1] .text                PROGBITS     0000000000000000 00000040 0000003c  0 AX     0   0  1
[ 2] .rela.text           RELA         0000000000000000 00000210 00000030 24 I     11   1  8
[ 3] .data                PROGBITS     0000000000000000 0000007c 00000000  0 WA     0   0  1
[ 4] .bss                 NOBITS       0000000000000000 0000007c 00000000  0 WA     0   0  1
[ 5] .rodata              PROGBITS     0000000000000000 0000007c 00000004  0 A      0   0  1
[ 6] .comment             PROGBITS     0000000000000000 00000080 00000035  1 MS     0   0  1
[ 7] .note.GNU-stack      PROGBITS     0000000000000000 000000b5 00000000  0        0   0  1
[ 8] .eh_frame            PROGBITS     0000000000000000 000000b8 00000038  0 A      0   0  8
[ 9] .rela.eh_frame       RELA         0000000000000000 00000240 00000018 24 I     11   8  8
[10] .shstrtab            STRTAB       0000000000000000 00000258 00000061  0        0   0  1
[11] .symtab              SYMTAB       0000000000000000 000000f0 00000108 24       12   9  8
[12] .strtab              STRTAB       0000000000000000 000001f8 00000016  0        0   0  1
```

You don’t need to understand whole of the above listing. But essentially, for each section, it lists various information, like the name of the section, size of the section and the offset of the section from the start of the file. Important sections for our use are the following-

- **text** section contains our machine code
- **rodata** section contains the read only data in our program. It may be constants or string literals that you may have used in your program. Here it just contains **%d\n**
- **data** sections contains the initialized data of our program. Here it is empty, since we don’t have any initialized data
- **bss** section is like the **data** section but contains the uninitialized data of our program. Uninitalized data could be a array declared like **int arr[100]**, which becomes part of this section. One point to note about the bss section is that, unlike the other sections which occupy space depending upon their content, bss section just contain the size of the section and nothing else. The reason being at the time of loading, all that is needed is the count of bytes that we need to allocate in this section. In this way we reduce the size of the final executable
- **strtab** section list all the strings contained in our program
- **symtab** section is the symbol table. It contains all the symbols(variable and function names) of our program.
- **rela.text** section is the relocation section. More about this later.

You can also view the contents of these sections, just pass the corresponding section number to the **eu-readelf**program. You can also use the **objdump** tool. It can also provide you with the dissembly for some of the sections.

Let’s talk in little more detail about the **rela.text** section. Remember the **printf** function that we used in our program. Now, **printf** is something that we haven’t defined by ourself, it is part of the C library. Normally when you compile your C programs, the compiler will compile them in a way so that C functions that you call are not bundled in with your executable, which thus reduces the size of the final executable. Instead a table is made of all those symbols, called a, **relocation table**, which is later filled by something in called the **loader**. We will discuss more about the **loader** part later on, but for now, the important thing is that the if you look at the **rela.text**section, you would find the **printf** symbol listed down there. Let’s confirm that once here.

```shell
$ eu-readelf -r sample.o


Relocation section [ 2] '.rela.text' for section [ 1] '.text' at offset 0x210 contains 2 entries:
  Offset              Type            Value               Addend Name
  0x0000000000000027  X86_64_32       000000000000000000      +0 .rodata
  0x0000000000000031  X86_64_PC32     000000000000000000      -4 printf


Relocation section [ 9] '.rela.eh_frame' for section [ 8] '.eh_frame' at offset 0x240 contains 1 entry:
  Offset              Type            Value               Addend Name
  0x0000000000000020  X86_64_PC32     000000000000000000      +0 .text
```

You can ignore the second relocation section **.rela.eh_frame**. It has to do with exception handling, which is not of much interest to us here. Let’s see the first section there. There we can see two entries, one of which is our **printf**symbol. What does this entry mean is that, there is a symbol used in this file with a name of **printf** but has not been defined, and that symbol is located in this file at the offset 0x31 from the start of the **.text** section. Let’s check what is at the offset 0x31 right now in the **.text** section.

```
$ eu-objdump -d -j .text sample.o
sample.o: elf64-elf_x86_64


Disassembly of section .text:


       0:    55                       push    %rbp
       1:    48 89 e5                 mov     %rsp,%rbp
       4:    48 83 ec 10              sub     $0x10,%rsp
       8:    c7 45 f4 01 00 00 00     movl    $0x1,-0xc(%rbp)
       f:    c7 45 f8 02 00 00 00     movl    $0x2,-0x8(%rbp)
      16:    8b 55 f4                 mov     -0xc(%rbp),%edx
      19:    8b 45 f8                 mov     -0x8(%rbp),%eax
      1c:    01 d0                    add     %edx,%eax
      1e:    89 45 fc                 mov     %eax,-0x4(%rbp)
      21:    8b 45 fc                 mov     -0x4(%rbp),%eax
      24:    89 c6                    mov     %eax,%esi
      26:    bf 00 00 00 00           mov     $0x0,%edi
      2b:    b8 00 00 00 00           mov     $0x0,%eax
      30:    e8 00 00 00 00           callq   0x35               <<<<<< offset 0x31
      35:    b8 00 00 00 00           mov     $0x0,%eax
      3a:    c9                       leaveq
      3b:    c3                       retq
```

Here you can see the call instruction at offset 0x30. **e8** stands for the opcode of the call instruction followed by the 4 bytes from offset 0x31 to 0x34, which should correspond to our **printf** function actual address which we don’t have right now, so they are just 00’s. (Later on, we will see that is location doesn’t actually hold the printf address, but indirectly calls it using something called **plt** table. We will cover this part later)

![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/6.png>)All the things that we have done till now have worked on a single source file. But in reality, that is the rarely the case. In real production code, you have hundred’s of thousand’s of source code files which you would need to compile and create a executable. Now how the steps that we followed till now would compare in that case?

Well, the steps would all remain the same. All the source code files would individually get preprocessed, compiled, assembed and we would get separate object code files at the end.

Now each source code file wouldn’t have been written in isolation. They must have some functions, global variables which must be defined in some file and used at different locations in other files.

It is the job of the linker to gather all the object files, go through each of them and track which symbol does each file defines and which symbols does it uses. It could find all these information in the symbol table in each of the object files. After gathering all these information, the linker creates a single object file combining all the sections from each of the individual object files into their corresponding sections and relocating all the symbols that can be resolved.

In our case, we don’t have collection of source files, we have just one file, but since we use printf function from the C library, our source file will by dynamically linked with the C library. Let’s now link our program and further investigate the output.

```
gcc sample.c
```

I won’t go into much detail here, since it is also a ELF file that we saw above, with just some new sections. One thing to note here is, when we saw the object file that we got from the assembler, the addresses that we saw were relative. But after having linked all the files, we have pretty much idea, where all the pieces go and thus, if you examine the output of these stage, it contains absolute addresses also.

At this stage, linker has identified all the symbols that are being used in our program, who uses those symbols, and who has defined those symbols. Linker just maps the address of the definition of the symbol to the usage of the symbol. But after doing all this, there still exists some symbols that are not yet resolved at this point, one of the being our **printf** symbol. In general, these are such symbols which are either externally defined variables or externally defined functions. Linker also creates a relocation table, the same as that was created by the Assembler, with those entries which are still unresolved.

At this point, there is one thing you should know. The functions and data you use from other libraries, can be statically linked or dynamically linked. Static linking means that the functions and data from those libraries would be copied and pasted into your executable. Whereas, if you do dynamic linking, then those functions and data are not copied into your executable, thus reducing your final executable size.

For a libray to have facility of dyamic linking against it, the library must be a shared library (**so** file). Normally, the common libraries used by many programs comes as shared libraries and one of them is our libc library. **libc** is used by so many programs that if every program started to statically link against it, then at any point, there would be so many copies of the same code occupying space in your memory. Having dynamic linking saves this problem, and at any moment only one copy of the libc would be occupying space in the memory and all the programs would be referencing from that shared library.

To make the dynamic linking possible, the linker creates two more sections that weren’t there in the object code generated by the assembler. These are the **.plt** (Procedure Linkage table) and the **.got** (Global Offset Table) sections. We will cover about these sections when we come to loading our executable, as these sections come useful when we actually load the executable.![image1](<https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Life_of_a_binary-zh/7.png>)Now it is time to actually run our executable file.

When you click on the file in your GUI, or run it from the command line, indirectly **execev** system call is invoken. It is this system call, where the kernel starts the work of loading your executable in the memory.

Remember the **Program Header Table** from above. This is where it is very useful.

```shell
$ eu-readelf  -l a.out 
Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000400040 0x0000000000400040 0x0001f8 0x0001f8 R E 0x8
  INTERP         0x000238 0x0000000000400238 0x0000000000400238 0x00001c 0x00001c R   0x1
	[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000400000 0x0000000000400000 0x000724 0x000724 R E 0x200000
  LOAD           0x000e10 0x0000000000600e10 0x0000000000600e10 0x000228 0x000230 RW  0x200000
  DYNAMIC        0x000e28 0x0000000000600e28 0x0000000000600e28 0x0001d0 0x0001d0 RW  0x8
  NOTE           0x000254 0x0000000000400254 0x0000000000400254 0x000044 0x000044 R   0x4
  GNU_EH_FRAME   0x0005f8 0x00000000004005f8 0x00000000004005f8 0x000034 0x000034 R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x10
  GNU_RELRO      0x000e10 0x0000000000600e10 0x0000000000600e10 0x0001f0 0x0001f0 R   0x1


 Section to Segment mapping:
  Segment Sections...
   00     
   01      [RO: .interp]
   02      [RO: .interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .plt.got .text .fini .rodata .eh_frame_hdr .eh_frame]
   03      [RELRO: .init_array .fini_array .jcr .dynamic .got] .got.plt .data .bss
   04      [RELRO: .dynamic]
   05      [RO: .note.ABI-tag .note.gnu.build-id]
   06      [RO: .eh_frame_hdr]
   07     
   08      [RELRO: .init_array .fini_array .jcr .dynamic .got]
```



How would the kernel know where to find this table in the file? Well, that information could be found in the **ELF Header** which always starts at offset 0 in the file. Having done that, kernel looks up all the entries which are of type **LOAD** and loads them into the memory space of the process.

As you can see from the above listing, there are two entries of type **LOAD**. You can also see which sections are contained in each segment.

Modern operating systems and processors manage memory in terms of pages. Your computer memory is divided into fixed size chunks and when any process asks for some memory, the operating system allots some number of pages to that process. Apart from the benefit of managing memory efficiently, this also has the benefit of providing security. Operating systems and kernel can set protection bits for each page. Protection bits specifies whether the particular page is Read only, could be written or can be executed. A page whose protection bit is set as Read only, can’t be modified and thus prevents from intentional or unintentional modification of data.

Read only pages have also one benefit that multiple running processes for the same program can share the same pages. Since the pages are read only, no running process can modify those pages and thus, every process would work just fine.

To set up these protection bits we somehow would have to tell the kernel, which pages have to be marked Read only and which could be Written and Executed. These information is stored in the Flags in each of the entries above.

Notice the first **LOAD** entry. It is marked as R and E, which means that these segment could be read and executed but can’t be modified and if you look down and see which sections come in these segment, you can see two familiar sections there, **.text** and **.rodata**. Thus our code and read-only data can only be read and executed but can’t be modified which is what should happen.

Similary, second **LOAD** entry contains the initialized and non initialized data, **GOT** table (more on this later) which are marked as RW and thus can be read and written but can’t be executed.

After loading these segments and setting up their permissions, the kernel checks if there is **.interp** segment or not. In the statically linked executable, there is no need for this segment, since the executable contains all the code that it needs, but for the dynamically linked executable, this segment is important. This segment contains the **.interp** section which contains the path to the dynamic linker. (You can check that there is no **.interp** segment in the statically linked executable by passing **-static** flag to the gcc compiler and checking the header table in the resulting executable)

In our case, it would find one and it points to the dynamic linker at this path **/lib64/ld-linux-x86-64.so.2**. Similarly to our executable, the kernel would start loading these shared object by reading the header, finding its segments and loading them in the memory space of the our current program. In statically linked executablewhere all this is not needed, the kernel would have given control to our program, here the kernel gives control to the dynamic linker and pushes the address of our main function to be called on the stack, so that after dynamic linker finishes it’s job, it knows where to hand over the control to.

We should now understand the two tables we have been skipping over for too long now, **Procedure Linkage Table**and **Global Offset Table** as these are closely related to the function of dynamic linker.

There might be two types of relocations needed in your program. Variables relocations and function relocations. For a variable which is externally defined, we include that entry in the **GOT** table and the functions which are externally defined we include those entries in both the tables. So, essentially, **GOT** table has entries for all the externally defined variables as well as functions, and **PLT** table has entries for only the functions. The reason why we have two entries for functions will be clear by the following example.

Let us take an example of printf function to see how these tables works. In our main function, let’s see the call instruction to printf function.

```
400556:    e8 a5 fe ff ff           callq   0x400400
```

This call instruction is calling an address which is part of the **.plt** section. Let’s see what is there.

```shell
$ objdump -d -j .plt a.out
a.out:     file format elf64-x86-64


Disassembly of section .plt:


00000000004003f0 <printf@plt-0x10>:
  4003f0:	ff 35 12 0c 20 00    	pushq  0x200c12(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  4003f6:	ff 25 14 0c 20 00    	jmpq   *0x200c14(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  4003fc:	0f 1f 40 00          	nopl   0x0(%rax)


0000000000400400 <printf@plt>:
  400400:	ff 25 12 0c 20 00    	jmpq   *0x200c12(%rip)        # 601018 <_GLOBAL_OFFSET_TABLE_+0x18>
  400406:	68 00 00 00 00       	pushq  $0x0
  40040b:	e9 e0 ff ff ff       	jmpq   4003f0 <_init+0x28>


0000000000400410 <__libc_start_main@plt>:
  400410:	ff 25 0a 0c 20 00    	jmpq   *0x200c0a(%rip)        # 601020 <_GLOBAL_OFFSET_TABLE_+0x20>
  400416:	68 01 00 00 00       	pushq  $0x1
  40041b:	e9 d0 ff ff ff       	jmpq   4003f0 <_init+0x28>
```

For each externally defined function, we have an entry in the **plt** section and all look the same and have three instructions, except the first entry. This is a special entry which we will see the use of later.

There we find a jump to the value contained at the address **0x601018**. These address is an entry in the GOT table. Let’s see the content of these address.

```shell
$ objdump -s a.out | grep -A 3 '.got.plt' 
Contents of section .got.plt:
601000 280e6000 00000000 00000000 00000000  (.`.............
601010 00000000 00000000 06044000 00000000  ..........@.....
601020 16044000 00000000                    ..@..... 
```

This is where the magic happens. Except the first time when the printf function is called, the value at this address would be the actual address of the printf function from the C library and we would simply jump to that location. But for the first time, something else happens.

When printf function is called for the first time, value at this location is the address of the next instruction in the **plt** entry of the printf function. As you can see from the above listing, it is **400406** which is stored in little endian format. At this location in the **plt** entry, we have a push instruction which pushes 0 onto the stack. Each **plt** entry have same push instruction but they push different numbers. 0 here denotes the offset of the printf symbol in the relocation table. The push instruction is then followed by the jump instruction which jumps to the first instruction in the first **plt** entry.

Remember from above, when I told you that the first entry is special. It is because here where the dynamic linker is called to resolve the external symbols and relocate them. To do that, we jump to the address contained in the address **601010** in the **got** table. These address should contain the address of the dynamic linker routine to handle the relocation. Right now these entry is filled with 0’s, but this address is filled by the linker when the program actually runs and the kernel calls the dynamic linker.

When the routine is called, linker would resolve the symbol that was pushed earlier(in our case, 0), from external shared objects and put the correct address of the symbol in the **got** table. So, from now on, when the printf function is called, we don’t have to consult the linker, we can directly jump from plt to our printf function in the C library.

This process is called lazy loading. A program may contain many external symbols, but it may not call of them in one run of the program. So, the symbols resolution is deferred till the actual use and this save us some program startup time.

As you can see from the above discussion, we never had to modify the **plt** section, but only the **got** section. And that is why **plt** section is in the first **LOAD** segment and marked as Read only, while **got** section is in the second **LOAD** segment and marked Write.

And this is how dynamic linker works. I have skipped over lots of gory details but if you are interested in knowing in more detail, then you can checkout this [article](https://www.akkadia.org/drepper/dsohowto.pdf).

Let’s go back to our program loading. We have already done most of the work. Kernel has loaded all the loadablesegments, has invoked the dynamic linker. All that is left is to invoke our main function. And that work is done by the linker after it finishes. And when it calls our main function we get the following output in our terminal-

```
3
```

And that my friend, is bliss.

Thank you for reading my article. Let me know if you liked my article or any other suggestions for me, in the comments section below. And please, feel free to share :)

Feel free to share!

  

