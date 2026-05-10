# Class for Book
class Book:
    # Constructor for Book class
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    # Getter and setter for page_count
    def page_count(self):
        return self.page_count
    
    # Setter for page_count with error handling
    def page_count(self, value):
        # Check is the value is an integer
        if not isinstance(value, int):
            # Print an error if not
            print("Error: page_count must be an integer.")
        else:
            # Stores the value if it is an integer
            self._page_count = value
            
    # Method to turn the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



    