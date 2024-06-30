# Function to print the truth table
def print_truth_table():
    # Print the header
    print(f"{'A':<5} {'B':<5} {'A AND B':<10} {'A OR B':<10} {'NOT A':<10} {'NOT B':<10}")
    
    # Generate and print the truth table
    for A in [True, False]:
        for B in [True, False]:
            and_result = A and B
            or_result = A or B
            not_a = not A
            not_b = not B
            print(f"{A:<5} {B:<5} {and_result:<10} {or_result:<10} {not_a:<10} {not_b:<10}")

# Call the function to print the truth table
print_truth_table()
