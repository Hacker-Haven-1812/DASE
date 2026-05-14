import random

def generate_program():

    lines = []
    lines.append(".section .text")
    lines.append(".global _start")
    lines.append("_start:")

    # Initialize registers
    lines.append("li x1, 1")
    lines.append("li x2, 2")
    lines.append("li x3, 3")
    lines.append("li x4, 100")

    # Deep RAW chain
    for i in range(20):
        rd = random.randint(5, 15)
        rs = rd - 1 if rd > 5 else 5
        lines.append(f"add x{rd}, x{rs}, x1")

    # Store + Load hazard
    lines.append("sw x5, 0(x4)")
    lines.append("lw x6, 0(x4)")

    # Branch stress
    lines.append("loop:")
    lines.append("addi x1, x1, -1")
    lines.append("bne x1, x0, loop")

    # Mixed opcodes
    for _ in range(15):
        op = random.choice(["add", "sub", "xor", "or", "and"])
        rd = random.randint(10, 20)
        rs1 = random.randint(1, 10)
        rs2 = random.randint(1, 10)
        lines.append(f"{op} x{rd}, x{rs1}, x{rs2}")

    lines.append("j _start")

    return "\n".join(lines)
