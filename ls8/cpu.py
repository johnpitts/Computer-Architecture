"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""
    HLT = 0b00000001
    MULT = 0b10100010

    def __init__(self):
        self.ram = [0] * 256             # make this a List instead of a dictionary [0] * 256
        self.register = [0] * 8
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0
        filename = sys.argv[1]
        
        try:
            with open(filename) as f:
                for line in f:
                    # print(line)

                    # Ignore comments, whether on their one line, or at end of a line of command code
                    comment_split = line.split("#")   # this is obviously a list of codesplits
                    # print(comment_split)

                    # Strip out whitespace
                    instruction_num = comment_split[0].strip()

                    if instruction_num == '':
                        continue

                    # print(f"word! {instruction_num}")
                    self.ram[address] = int(instruction_num, 2)
                    # print(f"instruction: {instruction_num} for address:{address}")
                    address += 1

        except FileNotFoundError:
            print("file not found")
            sys.exit(2)



    def ram_read(self, memory_address_register):

        return self.ram[memory_address_register]


    def ram_write(self, memory_data_register, program):      # pc insert a command (value), set value in ram as new value

        self.ram[address] = memory_data_register

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        elif op == "MULT":
            self.register[reg_a] *= self.register[reg_b]
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
            print(" %02X" % self.register[i], end='')

        print()

    def multiply(self, factor1, factor2):
        product = 0
        for multiplier in range(factor2):
            product += factor1
        return product

    
    

    def run(self):

        running = True

        while running:
            command = self.ram[self.pc]
            # print(f"command: {bin(command)}")

            # Load following register w number (LDI)
            if command == 0b10000010:
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)
                self.register[operand_a] = operand_b
                self.pc += 3
            
            # MULTIPLY NEXT TWO NUMBERS
            elif command == self.MULT:
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)
                self.alu("MULT", operand_a, operand_b)
                self.pc += 3

            # Print the following register (PRN)
            elif command == 0b01000111:
                operand_a = self.ram_read(self.pc+1)
                print(self.register[operand_a])
                self.pc += 2

            # Halt the program
            elif command == self.HLT:
                running = False
                self.pc = 0
            else:
                print(f"Whoops! unrecognized command: {command}")
                running = False

        self.trace()



# each register can hold a "word" which is = to bits computer is rated, so 8-bit words.






        
