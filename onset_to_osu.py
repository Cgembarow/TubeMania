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

        # Generate a random number from the set [64, 192, 320, 448] for the first value
        rand_index = random.randint(0, len(possible_numbers) - 1)
        first_value = possible_numbers[rand_index]

        # Create a new line with the modified first value while retaining the other values
        new_line = f'{first_value},{line[1]},{third_value},{",".join(line[3:])}'  # Retains all other values
        modified_lines.append(new_line)

    # Write the modified lines to the output file
    with open(output_file_path, 'w') as output_file:
        for line in modified_lines:
            output_file.write(line + '\n')

# Example usage:
process_and_create_output('input.txt', 'output.txt')
