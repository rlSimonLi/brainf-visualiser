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
        self.loop_pairs = Brainf.get_loop_pairs(instruction)

    @property
    def current_ins(self):
        return self.ins[self.ins_idx]

    @staticmethod
    def get_loop_pairs(instruction):
        stack = []
        pairs = []
        for i in range(len(instruction)):
            ins = instruction[i]
            if ins in ("[", "]"):
                stack.append((i, ins))
                if len(stack) >= 2:
                    if stack[-2][1] == '[' and stack[-1][1] == ']':
                        pairs.append((stack[-2][0], stack[-1][0]))
                        stack.pop()
                        stack.pop()
        if len(stack) != 0:
            raise SyntaxError
        return pairs

    def __execute_ins(self):
        instruction_set = {
            ">": self.move_pointer_right,
            "<": self.move_pointer_left,
            "+": self.inc_node,
            "-": self.dec_node,
            ".": self.stdout,
            ",": self.stdin,
            "[": self.skip_if_zero,
            "]": self.continue_if_nonzero
        }
        output = instruction_set[self.current_ins]()
        return output

    def move_pointer_right(self):
        self.tape.pointer_idx += 1
        self.ins_idx += 1

    def move_pointer_left(self):
        self.tape.pointer_idx -= 1
        self.ins_idx += 1

    def inc_node(self):
        p = self.tape.current_node
        p.set_by_raw(p.get_raw() + 1)
        self.ins_idx += 1

    def dec_node(self):
        p = self.tape.current_node
        p.set_by_raw(p.get_raw() - 1)
        self.ins_idx += 1

    def stdout(self) -> str:
        p = self.tape.current_node
        self.ins_idx += 1
        return p.get_chr()

    def stdin(self):
        p = self.tape.current_node
        char = "@"  # TODO: replace with javascript prompt
        p.set_by_chr(char)
        self.ins_idx += 1

    def continue_if_nonzero(self):
        p = self.tape.current_node
        if p.get_raw() != 0:
            self.ins_idx = self.get_loop_pointer("]")
        else:
            self.ins_idx += 1

    def skip_if_zero(self):
        p = self.tape.current_node
        if p.get_raw() == 0:
            self.ins_idx = self.get_loop_pointer("[")
        else:
            self.ins_idx += 1

    def get_loop_pointer(self, mode):
        for pair in self.loop_pairs:
            if mode == "]":
                if self.ins_idx == pair[1]:
                    return pair[0] + 1
            if mode == "[":
                if self.ins_idx == pair[0]:
                    return pair[1] + 1

    def __str__(self):
        return f"Pointer: {self.tape.pointer_idx} Tape: {[str(n) for n in self.tape.tape]}"

    def has_next(self):
        return self.ins_idx < len(self.ins)

    def step(self):
        if self.has_next():
            return self.__execute_ins()
        else:
            return None


def main():
    a = Brainf(
        "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
    while a.has_next():
        out = a.step()
        if out:
            print(out, end="")


main()
