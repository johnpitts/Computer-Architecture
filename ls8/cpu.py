"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    HLT = 0b00000001

    def __init__(self):
        self.ram = [0] * 256             # make this a List instead of a dictionary [0] * 256
        self.register = [0] * 8
        self.pc = 0

    def load(self, program):
        """Load a program into memory."""

        address = 0
        
        for instruction in program:
            self.ram[address] = instruction
            # print(f"instruction: {instruction} for address:{address}")
            address += 1

    def ram_read(self, memory_address_register):

        return self.ram[memory_address_register]


    def ram_write(self, memory_data_register, program):      # pc insert a command (value), set value in ram as new value

        self.ram[address] = memory_data_register

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    

    def run(self):

        # For now, we've just hardcoded a program:

        running = True
        # print(f"program: {program}")

        while running:
            command = self.ram[self.pc]

            # Load following register w number (LGI)
            if command == 0b10000010:
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)
                self.register[operand_a] = operand_b
                self.pc += 3

            # Print the following register (PRN)
            elif command == 0b01000111:
                operand_a = self.ram_read(self.pc+1)
                print(self.register[operand_a])
                self.pc += 2

            # Halt the program
            elif command == self.HLT:
                running = False

        # self.trace()



# each register can hold a "word" which is = to bits computer is rated






        
