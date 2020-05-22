"""CPU functionality."""

import sys

# Operation Tables
binary_op = {
    0b00000001: 'HLT',
    0b10000010: 'LDI',
    0b01000111: 'PRN',
    0b01000101: 'PUSH',
    0b01000110: 'POP',
    0b01010000: 'CALL',
    0b00010001: 'RET',
    0b01010100: 'JMP',
    0b01010101: 'JEQ',
    0b01010110: 'JNE',
}

math_op = {
    "ADD": 0b10100000,
    "SUB": 0b10100001,
    "MUL": 0b10100010,
    'CMP': 0b10100111,
    'SHL': 0b10101100,
    'SHR': 0b10101101,
    'MOD': 0b10100100,
    'AND': 0b10101000,
    'OR': 0b10101010,
    'XOR': 0b10101011,
    'NOT': 0b01101001
}

# Global Constants
SP = 7  # Stack Pointer

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        # Registers
        self.reg = [0] * 8
        self.reg[SP] = 0xF4
        self.operand_a = None
        self.operand_b = None

        # Internal Registers
        self.PC = 0 # program counter
        self.MAR = None # memory address register
        self.MDR = None # memory data register
        self.FL = 0b00000000  # flags

        # Branch Table
        self.instructions = {}
        self.instructions['HLT'] = self.HALT
        self.instructions['LDI'] = self.LOAD
        self.instructions['PRN'] = self.PRINT
        self.instructions['PUSH'] = self.PUSH
        self.instructions['POP'] = self.POP
        self.instructions['CALL'] = self.CALL
        self.instructions['RET'] = self.RET
        self.instructions['JMP'] = self.JMP
        self.instructions['JEQ'] = self.JEQ
        self.instructions['JNE'] = self.JNE 

    def CALL(self):
        # calls a subroutine/function at the address stored in the reg
        self.reg[SP] -= 1

        # address of instruction
        in_address = self.PC + 2

        # push the address onto the stack
        self.ram[self.reg[SP]] = in_address

        # PC is set to address stored in the reg
        self.PC = self.reg[self.operand_a]

    