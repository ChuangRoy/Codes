    .intel_syntax noprefix
    .section .rdata,"dr"
LC0:
    .ascii "Hello World!\0"
    .text
    .globl    _main
    .def    _main;    .scl    2;    .type    32;    .endef
_main:
    push    ebp
    mov    ebp, esp
    and    esp, -16
    sub    esp, 16
    call    ___main
    mov    DWORD PTR [esp], OFFSET FLAT:LC0
    call    _puts
    leave
    ret
    .def    _puts;    .scl    2;    .type    32;    .endef
