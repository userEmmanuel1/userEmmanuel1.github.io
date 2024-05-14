def print_number_pyramid(rows):
    num = 1  # Initialize starting number
    
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        
        # Print numbers for the current row
        for j in range(1, 2 * i):
            print(num % 10, end="")
            num += 1  # Increment number
        
        # Move to the next line after printing the row
        print()

# Example usage:
print_number_pyramid(5)
