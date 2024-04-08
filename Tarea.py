class Beverage:
    def __init__(self, name, sizes):
        self.name = name
        self.sizes = sizes

class BeverageManager:
    def __init__(self):
        self.beverages = []

    def add_beverage(self, input_string):
        # Remove white spaces and split input into name and sizes
        input_string = input_string.replace(" ", "")
        parts = input_string.split(",")
        
        # Validate input format
        if len(parts) < 2:
            print("Error: Incorrect input format.")
            return
        
        name = parts[0]
        sizes = parts[1:]
        
        # Validate beverage name
        if not name.isalpha() or len(name) < 2 or len(name) > 15:
            print("Error: Beverage name should contain only alphabetic characters and have a length of 2 to 15 characters.")
            return
        
        # Validate sizes
        if len(sizes) > 5:
            print("Error: Up to five sizes per item are allowed.")
            return
        
        sizes = sorted([int(size) for size in sizes])
        for size in sizes:
            if size < 1 or size > 48:
                print("Error: Beverage size should be an integer value within the range of 1 to 48.")
                return
        
        # Create new beverage and add it to the list of beverages
        new_beverage = Beverage(name, sizes)
        self.beverages.append(new_beverage)
        print(f"Beverage '{name}' added successfully.")

    def list_beverages(self):
        print("List of beverages:")
        for beverage in self.beverages:
            sizes_str = ", ".join(map(str, beverage.sizes))
            print(f"- {beverage.name}: Sizes: {sizes_str}")
