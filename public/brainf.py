from collections import deque


class Node:
    def __init__(self, value: int = 0, bits=8):
        self._value = value
        self._upper_bound = 2 ** bits - 1

    def get_raw(self) -> int:
        return self._value

    def get_chr(self) -> str:
        return chr(self._value)

    def set_by_raw(self, raw):
        if 0 <= raw <= self._upper_bound:
            self._value = raw

    def set_by_chr(self, char):
        raw = ord(char)
        self.set_by_raw(raw)

    def __str__(self):
        return str(self._value)


class Tape:
    def __init__(self, byte_size: int):
        self.tape = [Node() for x in range(byte_size)]
        self.pointer_idx = 0

    @property
    def current_node(self) -> Node:
        return self.tape[self.pointer_idx]


class Brainf:
    def __init__(self, instruction, byte_size: int = 16):
        self.tape = Tape(byte_size)
        self.ins = instruction
        self.ins_idx = 0
        self.loop_stack = deque([])

    @property
    def current_ins(self):
        return self.ins[self.ins_idx]

    def execute_ins(self):
        instruction_set = {
            ">": self.move_pointer_right,
            "<": self.move_pointer_left,
            "+": self.inc_node,
            "-": self.dec_node,
            ".": self.stdout,
            ",": self.stdin,
        }
        output = instruction_set[self.current_ins]()
        self.ins_idx += 1
        return output

    def move_pointer_right(self):
        self.tape.pointer_idx += 1

    def move_pointer_left(self):
        self.tape.pointer_idx -= 1

    def inc_node(self):
        p = self.tape.current_node
        p.set_by_raw(p.get_raw() + 1)

    def dec_node(self):
        p = self.tape.current_node
        p.set_by_raw(p.get_raw() - 1)

    def stdout(self) -> str:
        p = self.tape.current_node
        return p.get_chr()

    def stdin(self):
        p = self.tape.current_node
        char = "@"  # TODO: replace with javascript prompt
        p.set_by_chr(char)

    def __str__(self):
        return str([str(n) for n in self.tape.tape])


def main():
    a = Brainf(",++>++<.")
    for ins in a.ins:
        out = a.execute_ins()
        print(a)
        if out:
            return out


main()
