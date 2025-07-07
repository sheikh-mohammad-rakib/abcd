#write a python function to add two numbers
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

# Example usage:
if __name__ == "__main__":
    result = add(5, 10)
    print("The sum is:", result)
    