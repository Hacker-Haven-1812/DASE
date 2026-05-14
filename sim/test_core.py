import cocotb
from cocotb.triggers import RisingEdge, Timer
import json

@cocotb.test()
async def coverage_test(dut):

    cocotb.log.info("=== Deep Structural Coverage Started ===")

    clk = dut.clk

    # Wait for reset release
    for _ in range(10):
        await RisingEdge(clk)

    reg_depth = {}
    raw_chain_depth = 0
    load_after_store = 0
    opcodes = set()

    branch_taken = 0
    branch_not_taken = 0

    last_store_reg = None

    MAX_CYCLES = 300

    for _ in range(MAX_CYCLES):

        await RisingEdge(clk)

        # Skip cycles if signal is unresolved
        if dut.mem_valid.value.is_resolvable is False:
            continue

        if int(dut.mem_valid.value) != 1:
            continue

        instr_val = dut.mem_rdata.value

        if instr_val.is_resolvable is False:
            continue

        instr = int(instr_val)

        opcode = instr & 0x7F
        opcodes.add(opcode)

        rs1 = (instr >> 15) & 0x1F
        rs2 = (instr >> 20) & 0x1F
        rd  = (instr >> 7)  & 0x1F

        # RAW depth
        src_depth = max(
            reg_depth.get(rs1, 0),
            reg_depth.get(rs2, 0)
        )

        new_depth = src_depth + 1

        if rd != 0:
            reg_depth[rd] = new_depth
            raw_chain_depth = max(raw_chain_depth, new_depth)

        # STORE
        if opcode == 0x23:
            last_store_reg = rs1

        # LOAD after STORE
        if opcode == 0x03:
            if last_store_reg is not None and rs1 == last_store_reg:
                load_after_store += 1

        # BRANCH
        if opcode == 0x63:
            if dut.branch_taken.value.is_resolvable:
                if int(dut.branch_taken.value) == 1:
                    branch_taken = 1
                else:
                    branch_not_taken = 1

    coverage = {
        "raw_chain_depth": raw_chain_depth,
        "load_after_store": load_after_store,
        "branch_taken": branch_taken,
        "branch_not_taken": branch_not_taken,
        "opcodes": list(opcodes),
        "trap": False
    }

    with open("coverage_report.json", "w") as f:
        json.dump(coverage, f, indent=4)

    cocotb.log.info("Deep Coverage Report Generated")


