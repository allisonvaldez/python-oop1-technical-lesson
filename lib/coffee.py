# Class for Coffee
class Coffee:
    # Constructor for Coffee class
    def __init__(self, size, price):
        self.size = size      
        self.price = price    
    
    # Getter for size with decorator
    @property                 
    def size(self):
        # Getter it returns the size of the coffee
        return self._size     

    # Setter for size with error handling
    @size.setter              
    def size(self, value):
        # Check if value is one of the valid sizes
        if value not in ["Small", "Medium", "Large"]:
            # Print an error if not
            print("Size must be Small, Medium, or Large") 
        else:
            # Stores the value if it is valid
            self._size = value
    
    # Method to tip for the coffee
    def tip(self):
        # Print the message
        print("This coffee is great, here's a tip!")
        # Increase price
        self.price += 1.00