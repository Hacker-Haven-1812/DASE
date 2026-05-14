import json

def compute_fitness():

    with open("coverage_report.json") as f:
        cov = json.load(f)

    score = 0

    # RAW chain depth normalized
    raw_score = min(cov["raw_chain_depth"] / 1000.0, 1.0)

    # Branch coverage
    branch_score = 0
    if cov["branch_taken"] == 1:
        branch_score += 0.5
    if cov["branch_not_taken"] >= 1:
        branch_score += 0.5

    # Load-after-store
    las_score = min(cov["load_after_store"] / 2.0, 1.0)

    # Opcode diversity
    opcode_score = min(len(cov["opcodes"]) / 10.0, 1.0)

    score = (
        0.35 * raw_score +
        0.25 * branch_score +
        0.20 * las_score +
        0.20 * opcode_score
    )

    return round(score, 3)
