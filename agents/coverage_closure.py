import subprocess
import random
import json
import statistics
import math
from scipy import stats

# =========================================================
# RESEARCH FREEZE CONFIGURATION (DO NOT MODIFY)
# =========================================================
GENERATIONS = 25
POPULATION = 8
SEEDS = 12

VERSION = "DASE v1.0 Research Freeze"


# =========================================================
# GENOME
# =========================================================
class Genome:
    def __init__(self, raw, hazard, opcode, branch):
        self.raw = raw
        self.hazard = hazard
        self.opcode = opcode
        self.branch = branch

    def mutate(self):
        return Genome(
            max(20, self.raw + random.randint(-20, 30)),
            max(10, self.hazard + random.randint(-10, 30)),
            min(80, max(10, self.opcode + random.randint(-15, 30))),
            max(10, self.branch + random.randint(-15, 30))
        )


# =========================================================
# PROGRAM GENERATOR
# =========================================================
def generate_program(g):

    lines = []
    lines.append(".section .text")
    lines.append(".global _start")
    lines.append("_start:")

    lines.append("li x1, 200")
    lines.append("li x2, 13")
    lines.append("li x3, 800")

    for _ in range(g.raw):
        lines.append("add x1, x1, x2")

    for _ in range(g.hazard):
        lines.append("sw x1, 0(x3)")
        lines.append("lw x4, 0(x3)")

    lines.append("loop:")
    for _ in range(g.branch):
        lines.append("addi x1, x1, -1")
    lines.append("bne x1, x0, loop")

    ops = ["add", "sub", "xor", "or", "and", "sll", "srl"]
    for _ in range(g.opcode):
        op = random.choice(ops)
        lines.append(f"{op} x5, x2, x4")

    lines.append("j _start")

    return "\n".join(lines) + "\n"


# =========================================================
# SIMULATION
# =========================================================
def run_sim(program_text):

    with open("program.s", "w") as f:
        f.write(program_text)

    subprocess.run(
        "riscv64-unknown-elf-gcc -march=rv32i -mabi=ilp32 -nostdlib -Ttext=0x0 program.s -o program.elf",
        shell=True, check=True)

    subprocess.run(
        "riscv64-unknown-elf-objcopy -O binary program.elf program.bin",
        shell=True, check=True)

    subprocess.run(
        "hexdump -v -e '1/4 \"%08x\\n\"' program.bin > program.hex",
        shell=True, check=True)

    subprocess.run("make clean", shell=True)
    subprocess.run("make", shell=True, check=True)


# =========================================================
# FITNESS (LOCKED)
# =========================================================
def compute_fitness(cov):

    raw_score = min(cov["raw_chain_depth"] / 80.0, 1.0)
    hazard_score = min(cov["load_after_store"] / 15.0, 1.0)
    opcode_score = min(len(cov["opcodes"]) / 8.0, 1.0)

    if cov["branch_taken"] == 1 and cov["branch_not_taken"] == 1:
        branch_score = 1.0
    elif cov["branch_taken"] == 1 or cov["branch_not_taken"] == 1:
        branch_score = 0.5
    else:
        branch_score = 0.0

    balance_bonus = 1.0 - abs(raw_score - hazard_score)

    fitness = (
        0.40 * raw_score +
        0.25 * hazard_score +
        0.15 * opcode_score +
        0.10 * branch_score +
        0.10 * balance_bonus
    )

    return round(fitness, 3)


# =========================================================
# DASE
# =========================================================
def run_dase(seed):

    random.seed(seed)
    best = Genome(60, 25, 45, 30)
    best_fit = 0

    for _ in range(GENERATIONS):
        for _ in range(POPULATION):

            candidate = best.mutate()
            program = generate_program(candidate)
            run_sim(program)

            with open("coverage_report.json") as cf:
                cov = json.load(cf)

            fit = compute_fitness(cov)

            if fit > best_fit:
                best_fit = fit
                best = candidate

    return best_fit


# =========================================================
# RANDOM BASELINE
# =========================================================
def run_random(seed):

    random.seed(seed)

    genome = Genome(
        random.randint(20, 60),
        random.randint(10, 30),
        random.randint(10, 60),
        random.randint(10, 40)
    )

    program = generate_program(genome)
    run_sim(program)

    with open("coverage_report.json") as cf:
        cov = json.load(cf)

    return compute_fitness(cov)


# =========================================================
# STATISTICS
# =========================================================
def confidence_interval(data):
    mean = statistics.mean(data)
    std = statistics.stdev(data)
    ci = 1.96 * std / math.sqrt(len(data))
    return round(mean - ci, 3), round(mean + ci, 3)


def cohens_d(a, b):
    mean1 = statistics.mean(a)
    mean2 = statistics.mean(b)
    pooled_std = math.sqrt(
        ((statistics.stdev(a) ** 2) + (statistics.stdev(b) ** 2)) / 2
    )
    return round((mean1 - mean2) / pooled_std, 3)


def welch_ttest(a, b):
    t_stat, p_value = stats.ttest_ind(a, b, equal_var=False)
    return round(t_stat, 3), round(p_value, 6)


# =========================================================
# EXPERIMENT RUN
# =========================================================
def run():

    print("\n======================================")
    print("Running", VERSION)
    print("======================================")

    dase_results = []
    random_results = []

    for s in range(SEEDS):

        print(f"\n===== SEED {s} =====")

        dase_fit = run_dase(s)
        rand_fit = run_random(s)

        dase_results.append(dase_fit)
        random_results.append(rand_fit)

        print("DASE:", dase_fit)
        print("Random:", rand_fit)

    print("\n========== FINAL STATISTICS ==========")

    print("DASE Mean:", round(statistics.mean(dase_results), 3))
    print("Random Mean:", round(statistics.mean(random_results), 3))

    print("DASE CI:", confidence_interval(dase_results))
    print("Random CI:", confidence_interval(random_results))

    print("Effect Size (Cohen's d):", cohens_d(dase_results, random_results))

    t_stat, p_val = welch_ttest(dase_results, random_results)
    print("Welch t-test t-stat:", t_stat)
    print("p-value:", p_val)

    if p_val < 0.05:
        print("Statistically significant (p < 0.05)")
    else:
        print("Not statistically significant")


if __name__ == "__main__":
    run()
