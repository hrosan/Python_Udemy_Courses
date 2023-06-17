def greet(name, message="Hello"):
    """
    Display a greeting message with an optional custom message.
    
    Parameters:
    - name: The name of the person to greet (string).
    - message: The custom greeting message (string). Default is "Hello".

    Returns:
    None
    """
    print(message + ", " + name + "!")

# Example usage
greet("Alice")  # Uses the default message "Hello"
greet("Bob", "Hi")  # Uses the custom message "Hi"