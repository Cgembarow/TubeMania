import random


def onset_to_beatmap(input_file_path, output_file_path):
    # List of possible numbers
    possible_numbers = [64, 192, 320, 448]

    # Read the lines from the input file
    with open(input_file_path, "r") as input_file:
        lines = input_file.readlines()

    # Create a list to store the modified lines
    modified_lines = []

    for line in lines:
        # Parse the time value from the line (assuming there's only one value per line)
        time_value = int(line.strip())

        # Generate a random number from the set [64, 192, 320, 448] for the first value
        rand_index = random.randint(0, len(possible_numbers) - 1)
        first_value = possible_numbers[rand_index]

        # Create a new line with the modified values in the specified format
        new_line = f"{first_value},192,{time_value},1,0,0:0:0:0:\n"
        modified_lines.append(new_line)

    # Write the modified lines to the output file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(modified_lines)
