# Set up the testing file for coffee class

# Import the Coffee class from the lib directory
from lib.coffee import Coffee

# Create a function to test if the coffee has a size
def test_coffee_has_size():
    # Create instance of Coffee class with size small and price of 3.00
    coffee = Coffee("Small", 3.00)
    # Assert the coffee size is small
    assert coffee.size == "Small"

# Create a function to test if the coffee has a price
def test_coffee_has_price():
    # Create instance of Coffee class with size small and price of 3.00
    coffee = Coffee("Small", 3.00)
    # Assert the coffee price is 3.00
    assert coffee.price == 3.00

# Create a function to test if the coffee size is valid. capsys is used to capture the output of the print statement in the test_coffee_size_is_valid method.
def test_coffee_size_is_valid(capsys):
    # Create instance of Coffee class with size tiny and price of 3.00
    coffee = Coffee("Tiny", 3.00)
    # Capture the output of the print statement
    captured = capsys.readouterr()
    # Assert coffee size is valid
    assert "Size must be Small, Medium, or Large" in captured.out

# Create a function to test if the tip is added to the coffee price. capsys is used to capture the output of the print statement in the test_tip method.
def test_tip(capsys):
    # Create instance of Coffee class with size small and price of 3.00
    coffee = Coffee("Small", 3.00)
    # Get the tip for the coffee 
    coffee.tip()
    # Capture the output of the print statement
    captured = capsys.readouterr()
    # Assert a message is printed and the price is updated
    assert "This coffee is great, here's a tip!" in captured.out
    # Assert the price is updated to 4.00   
    assert coffee.price == 4.00
