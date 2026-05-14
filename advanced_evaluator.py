import json
import re
import time
import subprocess
from collections import defaultdict

PROGRAM_FILE = "program.s"

# =========================================================
# 1️⃣ INSTRUCTION DISTRIBUTION
# =========================================================

def instruction_distribution():

    histogram = defaultdict(int)

    with open(PROGRAM_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(".") or ":" in line:
                continue
            opcode = line.split()[0]
            histogram[opcode] += 1

    return dict(histogram), len(histogram)


# =========================================================
# 2️⃣ REGISTER COVERAGE
# =========================================================

def register_access_coverage():

    reg_access = defaultdict(int)

    with open(PROGRAM_FILE) as f:
        for line in f:
            regs = re.findall(r'x\d+', line)
            for r in regs:
                reg_access[r] += 1

    return dict(reg_access), len(reg_access)


# =========================================================
# 3️⃣ IMMEDIATE COVERAGE
# =========================================================

def immediate_coverage():

    immediates = set()

    with open(PROGRAM_FILE) as f:
        for line in f:
            nums = re.findall(r'[-]?\d+', line)
            for n in nums:
                try:
                    immediates.add(int(n))
                except:
                    pass

    return len(immediates)


# =========================================================
# 4️⃣ INSTRUCTION COUNT
# =========================================================

def count_instructions():

    count = 0

    with open(PROGRAM_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(".") or ":" in line:
                continue
            count += 1

    return count


# =========================================================
# 5️⃣ SIMULATION THROUGHPUT
# =========================================================

def simulation_throughput():

    start = time.time()
    subprocess.run("make clean", shell=True)
    subprocess.run("make", shell=True, check=True)
    end = time.time()

    sim_time = end - start
    instr_count = count_instructions()

    ips = instr_count / sim_time if sim_time > 0 else 0

    return round(ips, 2)


# =========================================================
# 6️⃣ STAGE COVERAGE PROXY
# =========================================================

def stage_specific_proxy():

    fetch = count_instructions()
    memory = 0
    writeback = 0

    with open(PROGRAM_FILE) as f:
        for line in f:
            if "lw" in line or "sw" in line:
                memory += 1
            if re.search(r'x\d+', line):
                writeback += 1

    return {
        "fetch": fetch,
        "decode": fetch,
        "execute": fetch,
        "memory": memory,
        "writeback": writeback
    }


# =========================================================
# MAIN
# =========================================================

def run():

    print("\n===== ADVANCED DVCON METRICS (CLEAN VERSION) =====")

    instr_hist, spread = instruction_distribution()
    reg_access, unique_regs = register_access_coverage()
    imm_cov = immediate_coverage()
    ips = simulation_throughput()
    stage_cov = stage_specific_proxy()

    results = {
        "instruction_histogram": instr_hist,
        "instruction_spread": spread,
        "unique_registers_used": unique_regs,
        "immediate_value_coverage": imm_cov,
        "simulation_throughput_ips": ips,
        "stage_specific_coverage": stage_cov
    }

    with open("advanced_evaluation.json", "w") as f:
        json.dump(results, f, indent=4)

    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    run()
