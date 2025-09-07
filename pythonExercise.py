"""
Python Learning Exercises
=========================

Complete the exercises below to practice Python fundamentals.
Each section focuses on different Python concepts.
"""

# =============================================================================
# SECTION 1: VARIABLES AND DATA TYPES
# =============================================================================

def exercise_1_variables():
    """
    Exercise 1: Create variables of different types
    TODO: Create the following variables:
    - name (string): your name
    - age (integer): your age
    - height (float): your height in meters
    - is_student (boolean): whether you're a student
    - hobbies (list): list of your hobbies
    """
    # Your code here
    name="Akash Chauhan"
    age=25
    height=1.75
    is_student=True
    hobbies=["coding","reading","writing"]
    print(f'Name: {name} ,age: {age}, height: {height}, is_student: {is_student}, hobbies: {hobbies}')
    pass

def exercise_2_type_conversion():
    """
    Exercise 2: Convert between data types
    TODO: Convert the given values and return results
    """
    number_str = "42"
    float_num = 3.14159
    
    # Convert string to integer
    # Convert float to integer
    # Convert integer to string
    # Round float to 2 decimal places
    
    # Your code here
    number_int=int(number_str)
    floatToInt=int(float_num)
    intToString=str(number_int)
    floatToDefinedecimal=round(float_num,2)
    print(f'number_str: {number_str}, float_num: {float_num}, number_int: {number_int}, floatToInt: {floatToInt}, intToString: {intToString}, floatToDefinedecimal: {floatToDefinedecimal}')
    pass

# =============================================================================
# SECTION 2: STRINGS
# =============================================================================

def exercise_3_string_operations():
    """
    Exercise 3: String manipulation
    TODO: Complete the string operations
    """
    text = "  Python Programming is Fun!  "
    
    # Remove whitespace and convert to lowercase
    # Count occurrences of 'n'
    # Replace 'Fun' with 'Awesome'
    # Split into words
    
    # Your code here
    pass

def exercise_4_string_formatting():
    """
    Exercise 4: String formatting
    TODO: Create formatted strings using different methods
    """
    name = "Alice"
    score = 95.5
    
    # Use f-strings to create: "Alice scored 95.5 points"
    # Use .format() method
    # Use % formatting
    
    # Your code here
    pass

# =============================================================================
# SECTION 3: LISTS AND TUPLES
# =============================================================================

def exercise_5_list_operations():
    """
    Exercise 5: List manipulation
    TODO: Perform various list operations
    """
    numbers = [1, 2, 3, 4, 5]
    
    # Add 6 to the end
    # Insert 0 at the beginning
    # Remove the number 3
    # Find the index of 4
    # Create a new list with numbers doubled
    
    # Your code here
    pass

def exercise_6_list_comprehensions():
    """
    Exercise 6: List comprehensions
    TODO: Create lists using comprehensions
    """
    # Create list of squares from 1 to 10
    # Create list of even numbers from 1 to 20
    # Create list of words with length > 3 from ["cat", "dog", "elephant", "ant"]
    
    # Your code here
    pass

# =============================================================================
# SECTION 4: DICTIONARIES
# =============================================================================

def exercise_7_dictionaries():
    """
    Exercise 7: Dictionary operations
    TODO: Work with dictionaries
    """
    student = {"name": "John", "age": 20, "grade": "A"}
    
    # Add a new key "city" with value "New York"
    # Update the grade to "A+"
    # Get all keys
    # Get all values
    # Check if "age" key exists
    
    # Your code here
    pass

def exercise_8_nested_data():
    """
    Exercise 8: Nested data structures
    TODO: Work with nested dictionaries and lists
    """
    data = {
        "students": [
            {"name": "Alice", "scores": [85, 90, 78]},
            {"name": "Bob", "scores": [92, 88, 84]}
        ]
    }
    
    # Get Alice's second score
    # Add a new student "Charlie" with scores [80, 85, 90]
    # Calculate average score for Bob
    
    # Your code here
    pass

# =============================================================================
# SECTION 5: CONTROL STRUCTURES
# =============================================================================

def exercise_9_conditionals():
    """
    Exercise 9: If statements
    TODO: Write conditional logic
    """
    def check_grade(score):
        # Return grade based on score:
        # 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F
        pass
    
    def is_leap_year(year):
        # Return True if year is a leap year, False otherwise
        # Leap year: divisible by 4, but not by 100, unless also divisible by 400
        pass

def exercise_10_loops():
    """
    Exercise 10: Loops
    TODO: Practice different types of loops
    """
    def print_multiplication_table(n):
        # Print multiplication table for n (1 to 10)
        pass
    
    def count_vowels(text):
        # Count and return number of vowels in text
        pass
    
    def fibonacci_sequence(n):
        # Generate first n numbers in Fibonacci sequence
        pass

# =============================================================================
# SECTION 6: FUNCTIONS
# =============================================================================

def exercise_11_functions():
    """
    Exercise 11: Function basics
    TODO: Create various functions
    """
    def calculate_area(length, width):
        # Calculate and return area of rectangle
        pass
    
    def greet(name, greeting="Hello"):
        # Return greeting message with default parameter
        pass
    
    def sum_all(*args):
        # Return sum of all arguments (variable number of arguments)
        pass

def exercise_12_lambda_functions():
    """
    Exercise 12: Lambda functions
    TODO: Create lambda functions
    """
    # Create lambda to square a number
    # Create lambda to check if number is even
    # Use lambda with map() to convert list of strings to uppercase
    
    # Your code here
    pass

# =============================================================================
# SECTION 7: ERROR HANDLING
# =============================================================================

def exercise_13_exceptions():
    """
    Exercise 13: Exception handling
    TODO: Handle different types of exceptions
    """
    def safe_divide(a, b):
        # Safely divide a by b, handle division by zero
        pass
    
    def safe_list_access(lst, index):
        # Safely access list element, handle index errors
        pass

# =============================================================================
# SECTION 8: FILE OPERATIONS
# =============================================================================

def exercise_14_file_operations():
    """
    Exercise 14: File handling
    TODO: Read and write files
    """
    def write_to_file(filename, content):
        # Write content to file
        pass
    
    def read_from_file(filename):
        # Read and return file content, handle file not found
        pass
    
    def count_lines(filename):
        # Count number of lines in file
        pass

# =============================================================================
# SECTION 9: CLASSES AND OBJECTS
# =============================================================================

def exercise_15_classes():
    """
    Exercise 15: Object-oriented programming
    TODO: Create classes with methods and attributes
    """
    class BankAccount:
        def __init__(self, account_number, initial_balance=0):
            # Initialize account
            pass
        
        def deposit(self, amount):
            # Add amount to balance
            pass
        
        def withdraw(self, amount):
            # Subtract amount from balance if sufficient funds
            pass
        
        def get_balance(self):
            # Return current balance
            pass

# =============================================================================
# SECTION 10: ADVANCED EXERCISES
# =============================================================================

def exercise_16_algorithms():
    """
    Exercise 16: Basic algorithms
    TODO: Implement common algorithms
    """
    def bubble_sort(arr):
        # Sort array using bubble sort algorithm
        pass
    
    def binary_search(arr, target):
        # Find target in sorted array using binary search
        pass
    
    def is_palindrome(text):
        # Check if text is a palindrome (ignoring spaces and case)
        pass

def exercise_17_data_processing():
    """
    Exercise 17: Data processing
    TODO: Process and analyze data
    """
    sales_data = [
        {"product": "laptop", "price": 1000, "quantity": 5},
        {"product": "mouse", "price": 25, "quantity": 10},
        {"product": "keyboard", "price": 75, "quantity": 8}
    ]
    
    def calculate_total_revenue(data):
        # Calculate total revenue from all products
        pass
    
    def find_most_expensive(data):
        # Find the most expensive product
        pass
    
    def average_price(data):
        # Calculate average price of all products
        pass

# =============================================================================
# TEST SECTION
# =============================================================================

def run_tests():
    """
    Test your implementations here
    """
    print("=== Python Exercise Tests ===\n")
    
    # Test your functions here
    print("Complete the exercises above and test them here!")
    
    # Example test:
    print("Testing exercise_1_variables:")
    exercise_1_variables()

    print("Testing exercise_2_type_conversion:")
    exercise_2_type_conversion()

if __name__ == "__main__":
    run_tests()

"""
LEARNING TIPS:
==============

1. Start with Section 1 and work through each section sequentially
2. Test each function as you complete it
3. Use Python's built-in help() function to learn about methods
4. Practice with the Python interactive shell (REPL)
5. Don't hesitate to look up documentation for unfamiliar concepts

CONCEPTS COVERED:
================

- Variables and data types
- String manipulation and formatting
- Lists, tuples, and dictionaries
- Control structures (if/else, loops)
- Functions and lambda expressions
- Error handling with try/except
- File input/output operations
- Object-oriented programming basics
- Basic algorithms and data processing

NEXT STEPS:
===========

After completing these exercises, consider exploring:
- Advanced OOP concepts (inheritance, polymorphism)
- Modules and packages
- Regular expressions
- Web scraping with requests/BeautifulSoup
- Data analysis with pandas
- GUI development with tkinter
- Web development with Flask/Django
"""