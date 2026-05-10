# Class for Coffee

class Coffee:

    # Constructor for Coffee class
    def __init__(self, size, price):
        self.name = name
        self.caffeine_content = caffeine_content
    
    # Method to get the size of the coffee
    def size(self):
        # Getter it returns the size of the coffee
        return self.size

    # Method to get the price and size of the coffee
    def size(self, value):
        # Check if value is one of the valid sizes
        if value not in ["Small", "Medium", "Large"]:
            # Print an error if not
            print("Error: size must be 'Small', 'Medium', or 'Large'.")
        else:
            # Stores the value if it is valid
            self._size = value
    
    # Method to get the tip amount
    def tip(self):
        # Print the message
        print("This coffee is great, here's a tip!")
        # Increase the tip by $1.00
        self.price += 1.00