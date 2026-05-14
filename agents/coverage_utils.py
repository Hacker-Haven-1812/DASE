import json
import os


COVERAGE_FILE = "instruction_coverage.json"


def extract_opcode(instr_hex: str) -> str:
    """
    Extract RISC-V major opcode (lowest 7 bits).
    Input: 32-bit instruction as hex string (e.g., '00000093')
    Output: opcode hex string (e.g., '0x13')
    """
    try:
        instr = int(instr_hex, 16)
    except ValueError:
        return None

    opcode = instr & 0x7F  # Correct 7-bit mask
    return hex(opcode)


def extract_coverage_from_trace(trace_lines):
    """
    Parse simulation trace lines and collect unique opcodes.
    """
    opcodes = set()

    for line in trace_lines:
        if "INSTR=" in line:
            try:
                instr_hex = line.split("INSTR=")[1].split()[0]
                if instr_hex != "xxxxxxxx":
                    opcode = extract_opcode(instr_hex)
                    if opcode:
                        opcodes.add(opcode)
            except Exception:
                continue

    return opcodes


def extract_coverage():
    """
    Reads dump.vcd or console trace and extracts opcode coverage.
    Works by parsing stdout log captured in results.xml if available.
    """

    coverage = set()

    if not os.path.exists("results.xml"):
        return coverage

    with open("results.xml", "r") as f:
        lines = f.readlines()

    coverage = extract_coverage_from_trace(lines)

    save_coverage(coverage)

    return coverage


def save_coverage(opcodes: set):
    """
    Save opcode coverage to JSON.
    """
    data = {
        "unique_opcodes": sorted(list(opcodes)),
        "count": len(opcodes)
    }

    with open(COVERAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_coverage():
    """
    Load existing coverage file if present.
    """
    if not os.path.exists(COVERAGE_FILE):
        return set()

    with open(COVERAGE_FILE, "r") as f:
        data = json.load(f)

    return set(data.get("unique_opcodes", []))
