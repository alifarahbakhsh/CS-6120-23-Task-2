import json
import sys

COMMANDS_OF_INTEREST = ["add", "mul"]

def func():
    code = json.load(sys.stdin)
    out = code
    for func_idx, funct in enumerate(code["functions"]):
        for instr_idx, instr in enumerate(funct["instrs"]):
            if "op" in instr:
                if instr["op"] in COMMANDS_OF_INTEREST:
                    #print(instr["args"])
                    out["functions"][func_idx]["instrs"][instr_idx]["args"].reverse()
                    #print(instr["args"])
    return out
if __name__ == "__main__":
    out = func()
    with open("example.json", "w") as f:
        json.dump(out, f)