class Node:
    def __init__(self):
        self.value = 0


class Tape:
    def __init__(self, instructions, data):
        self.tape = [b'0' for x in range(len(instructions + 16))]
        self.storage_idx = 0
        self.execution_pointer = 1
        self.data_pointer = data

    def __load_instruction(self, instructions):
        idx = 1
        for instruction in instructions:
            self.tape[idx] = instruction

    def read_pointer(self) -> bytes:
        return self.tape[self.data_pointer]

    def write_pointer(self, data: bytes):
        self.tape[self.data_pointer] = data


class Brainf:
    def __init__(self, instruction, data):
        self.tape = Tape(instruction, data)
