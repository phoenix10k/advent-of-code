from typing import Tuple, List
from enum import Enum


class OpCode(Enum):
    ACC = 'acc'
    JMP = 'jmp'
    NOP = 'nop'


program: List[Tuple[OpCode, int]] = []
with open('input.txt') as file:
    for line in file:
        op, arg = line.split()
        for o in OpCode.__members__.values():
            if op == o.value:
                op = o
                break
        else:
            raise RuntimeError(f"unknown opcode: {op}")
        program.append((op, int(arg)))

print(program)

for i in range(len(program)):
    pc = 0
    acc = 0
    visited = set()

    program_copy = program.copy()
    if program[i][0] == OpCode.NOP:
        program_copy[i] = (OpCode.JMP, program[i][1])
    elif program[i][0] == OpCode.JMP:
        program_copy[i] = (OpCode.NOP, program[i][1])
    else:
        continue

    while pc < len(program_copy):
        if pc in visited:
            break
        visited.add(pc)
        op, arg = program_copy[pc]
        if op == OpCode.ACC:
            acc += arg
            pc += 1
        if op == OpCode.JMP:
            pc += arg
        if op == OpCode.NOP:
            pc += 1
    else:
        print(acc)
        exit(0)
