class Computer:
    def __init__(self, name, ram, price, processor):
        self.name = name
        self.ram = ram
        self.price = price
        self.processor = processor

    def input_computer_info(self):
        self.name = input("Computer Nomi: ")
        self.ram = int(input("Computer RAMi: "))
        self.price = float(input("Computer narxi: "))
        self.processor = input("Computer processori: ")

    def print_computer_info(self):
        print("\n*********\n")
        print("Computer Nomi:", self.name)
        print("Computer RAM:", self.ram)
        print("Computer narxi:", self.price)
        print("Computer processori:", self.processor)

    def has_ram_between_4_and_16(self):
        return 4 < self.ram < 16

def main():
    computers = []
    for i in range(4):
        computer = Computer("", 0, 0, "")
        computer.input_computer_info()
        computers.append(computer)

    computers_with_ram_between_4_and_16 = []
    for computer in computers:
        if computer.has_ram_between_4_and_16():
            computers_with_ram_between_4_and_16.append(computer)

    for computer in computers_with_ram_between_4_and_16:
        computer.print_computer_info()

if __name__ == "__main__":
    main()
