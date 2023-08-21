import random

def process_and_create_output(input_file_path, output_file_path):
    # List of possible numbers
    possible_numbers = [64, 192, 320, 448]

    # Read the lines from the input file
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Create a list to store the modified lines
    modified_lines = []

    for i in range(len(lines)):
        line = lines[i].strip().split(',')

        # Retain the third value from the original line
        third_value = line[2]

        # Shuffle the possible_numbers list
        random.shuffle(possible_numbers)

        # Take the first two values from the shuffled list
        first_value_1 = possible_numbers[0]
        first_value_2 = possible_numbers[1]

        # Create two new lines with the modified first values while retaining the other values
        new_line_1 = f'{first_value_1},{line[1]},{third_value},{",".join(line[3:])}'  # Retains all other values
        new_line_2 = f'{first_value_2},{line[1]},{third_value},{",".join(line[3:])}'  # Retains all other values

        # Add new_line_1 to the modified lines
        modified_lines.append(new_line_1)

        # Check if it's every 4th input line and add new_line_2 if so
        if (i + 1) % 4 == 0:
            modified_lines.append(new_line_2)

    # Write the modified lines to the output file
    with open(output_file_path, 'w') as output_file:
        for line in modified_lines:
            output_file.write(line + '\n')

# Example usage:
process_and_create_output('input.txt', 'output.txt')
