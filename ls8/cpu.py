"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        self.ram = {}
        self.register = [0] * 8
        self.pc = 0

    def load(self, program=[0b00000001]):
        """Load a program into memory."""

        address = 0
        
        for instruction in program:
            self.ram[address] = instruction
            print(f"instruction: {instruction} for address:{address}")
            address += 1

    def ram_read(self):

        self.load()


    def ram_write(self, program):

        self.load(program)

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

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        self.ram_write(program) # load the program from RAM
        running = True
        self.load()
        print(program)

        while running:
            print(self.pc)
            command = self.ram[self.pc]
            print(command)

            # Load following register w number (LGI)
            if command == 0b10000010:
                reg_num = self.ram[self.pc + 1]
                num = self.ram[self.pc + 2]
                self.register[reg_num] = num
                self.pc += 3

            # Print the following register (PRN)
            elif command == 0b01000111:
                reg_num = self.ram[self.pc+1]
                print(f"Here: {self.register[reg_num]}")
                pc += 2

            # Halt the program (HLT)
            elif command == 0b00000001:
                print("halted")
                running = False

            self.pc += 1
        # self.trace()



# each register can hold a "word" which is = to bits computer is rated






        
