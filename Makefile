# ============================================
# Cocotb + Icarus + RISC-V Program Pipeline
# ============================================

# First target MUST be all
all: program.hex

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# --------------------------------------------
# RISC-V Toolchain
# --------------------------------------------
RISCV_PREFIX = riscv64-unknown-elf
RISCV_GCC = $(RISCV_PREFIX)-gcc
RISCV_OBJCOPY = $(RISCV_PREFIX)-objcopy

# --------------------------------------------
# Assembly → ELF → BIN → WORD-HEX
# --------------------------------------------

program.elf: program.s
	$(RISCV_GCC) -march=rv32i -mabi=ilp32 -nostdlib -Ttext=0x0 program.s -o program.elf

program.bin: program.elf
	$(RISCV_OBJCOPY) -O binary program.elf program.bin

program.hex: program.bin
	hexdump -v -e '1/4 "%08x\n"' program.bin > program.hex

# --------------------------------------------
# Verilog Sources
# --------------------------------------------

VERILOG_SOURCES += $(PWD)/rtl/picorv32.v
VERILOG_SOURCES += $(PWD)/rtl/memory.v
VERILOG_SOURCES += $(PWD)/rtl/top.v

TOPLEVEL = top
MODULE = sim.test_core

# --------------------------------------------
# Include Cocotb
# --------------------------------------------

include $(shell cocotb-config --makefiles)/Makefile.sim
