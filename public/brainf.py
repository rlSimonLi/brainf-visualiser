class Node:
    def __init__(self, value: int = 0, bits = 8):
        self._value = value
        self._upper_bound = 2**bits-1

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

class Tape:
    def __init__(self, instructions, data):
        self.tape = [0, ]
        self.storage_idx = 0
        self.execution_pointer = 1
        self.data_pointer = data
        self.__load_instruction(instructions)

    def __load_instruction(self, instructions):
        for instruction in instructions:
            self.tape.append(ord(instruction))

    def read_pointer(self) -> int:
        return self.tape[self.data_pointer]

    def write_pointer(self, data: int):
        self.tape[self.data_pointer] = data


class Brainf:
    def __init__(self, instruction, data):
        self.tape = Tape(instruction, data)
