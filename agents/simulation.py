# agents/simulation.py

import subprocess

def run_sim():
    subprocess.run([
        "riscv64-unknown-elf-gcc",
        "-march=rv32i",
        "-mabi=ilp32",
        "-nostdlib",
        "-Ttext=0x0",
        "program.s",
        "-o",
        "program.elf"
    ], check=True)

    subprocess.run([
        "riscv64-unknown-elf-objcopy",
        "-O", "binary",
        "program.elf",
        "program.bin"
    ], check=True)

    subprocess.run([
        "hexdump", "-v", "-e", "1/4 \"%08x\\n\"",
        "program.bin"
    ], stdout=open("program.hex", "w"), check=True)

    subprocess.run(["make"], check=True)
