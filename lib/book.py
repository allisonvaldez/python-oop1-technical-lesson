# Class for Book

class Book:
    # Constructor for Book class
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count
    
    # Setter for page_count with error handling
    @page_count.setter
    def page_count(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            # Print an error if not
            print("page_count must be an integer")  # ✅ removed period
        else:
            # Stores the value if it is an integer
            self._page_count = value

    # Method to turn the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")