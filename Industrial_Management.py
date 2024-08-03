class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.current_volume = 0

    def add_item(self, name, quantity):
        if self.current_volume + quantity <= self.capacity :
            self.items.append((name, quantity))
            self.current_volume += quantity
            return True
        else:
            print("Not enough space in inventory.")
            return False
        
    def display_inventory(self):
        print('Current inventory: ')
        for name, quantity in self.items:
            print(f"{name}: {quantity} units")
        
        print(f"Total volume: {self.current_volume} / {self.capacity}")
        print(f"Remaining capacity: {self.capacity - self.current_volume} units")
def main():
    warehouse1_capacity = 450
    warehouse2_capacity = 200
    warehouse3_capacity = 160

    warehouse1 = Inventory(warehouse1_capacity)
    warehouse2 = Inventory(warehouse2_capacity)
    warehouse3 = Inventory(warehouse3_capacity)

    #حلقه
    while True :
        try:
            name = input("Enter the item name (or 'exit' to quit): ")
            if name.lower() == "exit":
                break
            
            quantity = int(input("Enter the quantity: "))

            if quantity <= 0:
                print("Quantity must be a positive integer. ")
                continue

            if warehouse1.add_item(name, quantity):
                print(f"{quantity} units of {name} added to Warehouse1. ")

            elif  warehouse2.add_item(name, quantity):
                print(f"{quantity} units of {name} added to Warehouse2. ")

            elif warehouse3.add_item(name, quantity):
                print(f"{quantity} units of {name} added to Warehouse3. ")

            else:
                print(f"Not enough space in any warehouse for {quantity} units of {name}. ")

        except ValueError:
            
            print("Invalid input. Please  enter a valid quantity.")

    print("\nFinal inventory status: ")

    warehouse1.display_inventory()
    warehouse2.display_inventory()
    warehouse3.display_inventory()

    total_volume = warehouse1.current_volume + warehouse2.current_volume + warehouse3.current_volume
    print(f"\nTotal occupied volume across all warhouses: {total_volume}")

if __name__ == "__main__":
    main()





