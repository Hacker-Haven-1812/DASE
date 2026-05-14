/* * Linker Script for PicoRV32 
 * Maps code to Address 0x00000000
 */
MEMORY {
    mem : ORIGIN = 0x00000000, LENGTH = 0x00000400
}

SECTIONS {
    .text : {
        *(*.text);
    } > mem
}
