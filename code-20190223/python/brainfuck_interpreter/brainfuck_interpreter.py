"""
a simple interpreter written in python
source:https://www.jianshu.com/p/9bc08cce4579

what is the brain fuck lang:、
wikipedia:brainfuck
> -> 右移一格
< -> 左移一格
+ -> 指针指向的字节的值加一
- -> 指针指向的字节的值减一
. -> 输出指针指向的单元内容（ASCII码）
, -> 输入内容到指针指向的单元（ASCII码）
[ -> 向後跳转到对应的]
] -> 向前跳转到对应的[指令的次一指令处，如果指针指向的字节非零
"""
# not complete

import os

# 纸带


class Tape:
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def get(self):
        return self.thetape[self.position]

    def set(self, value):
        self.thetape[self.position] = value

    def inc(self):
        self.thetape[self.position] += 1

    def dec(self):
        self.thetape[self.position] -= 1

    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)

    def devance(self):
        self.position -= 1


def mainloop(program, bracket_map):
    pc = 0
    # pc program pointer
    tape = Tape()
    while pc < len(program):
        code = program[pc]
        if code == ">":
            tape.advance()
        elif code == "<":
            tape.devance()
        elif code == "+":
            tape.inc()
        elif code == "-":
            tape.dec()
        elif code == ".":
            # print
            print(chr(tape.get()), end='')
        elif code == ",":
            # read from stdin
            tape.set(ord(os.read(0, 1)[0]))
        elif code == "[" and tape.get() == 0:
            pc = bracket_map[pc]
        elif code == "]" and tape.get() != 0:
            # skip back to the matching [
            pc = bracket_map[pc]
        pc += 1


def parse(program):
    parsed = []
    bracket_map = {}
    leftstack = []
    pc = 0
    for char in program:
        if char in ("[", "]", ">", "<", "+", "-", ",", "."):
            parsed.append(char)
            if char == "[":
                leftstack.append(pc)
            elif char == "]":
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1
    return "".join(parsed), bracket_map


def run(fp):
    program_contents = ""
    with open(fp, 'r') as f:
        program_contents = ''.join(f.readlines())
    program, bm = parse(program_contents)
    mainloop(program, bm)


run(r'C:\Users\gusto\myscripts\hello.bf')
