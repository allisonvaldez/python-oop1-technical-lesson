# Set up the testing file for the Book class

# Import the Book class from the lib directory
from lib.book import Book

# Create a function to test if the book has a title
def test_book_has_title():
    # Create instance of Book class with title Harry Potter and list its 300 pages
    book = Book("Harry Potter", 300)
    # Assert the book title is Harry Potter
    assert book.title == "Harry Potter"

# Create a function to test if the book has page count
def test_book_has_page_count():
    # Create instance of Book class with title and assigns 300 pages
    book =  Book("Harry Potter", 300)
    # Assert the book page count is 300
    assert book.page_count == 300

# Create a function to test if the page count is an integer. capsys is used to capture the output of the print statement in the test_page_count_is_integer method.
def test_page_count_is_integer(capsys):
    # Create instance of Book class with the page number is a string
    book = Book("Harry Potter", "three hundred")
    # Capture the output of the print statement
    captured = capsys.readouterr()
    # Assert page count is an integer
    assert "page_count must be an integer" in captured.out  # ✅ no period

# Create a function to test if the book turned a page. capsys is used to capture the output of the print statement in the turn_page method.
def test_turn_page(capsys):
    # Create instance of Book class with title Harry Potter and list a string of page number
    book = Book("Harry Potter", 300)
    # Call the turn_page method to simulate turning a page in the book
    book.turn_page()
    # Capture the output of the print statement
    captured = capsys.readouterr()
    # Assert the message is printed when the function is called
    assert "Flipping the page...wow, you read fast!" in captured.out