import os
# --------------------
# Selecting the Madlib
# --------------------
original_madlib = []


def select_madlib():
    print("Please type the relative path to your Madlibs file:")
    madlibs_path = input()

    # Because I forget
    if madlibs_path.find(".txt") == -1:
        madlibs_path = madlibs_path + ".txt"

    try:
        # I learned this in Program 8 and went back through because I had issues with this program not writing and stuff
        with open(madlibs_path, encoding="utf-8") as madlib_file:
            madlib_lines = madlib_file.readlines()
            for i, line in enumerate(madlib_lines):
                madlib_lines[i] = line.strip()
            return madlib_lines
    except:
        print("Your selection was invalid")
        return


while len(original_madlib) == 0:
    user_input = select_madlib()
    if user_input is not None:
        original_madlib = user_input

# ------------------------------
# Extracting the replace markers
# ------------------------------


def extract_markers(madlib):
    lines = list(madlib)
    markers = []

    for i, line in enumerate(lines):

        _line = str(line)
        while _line.find(">") != -1:
            marker_start = _line.find('<')
            marker_end = _line.find('>') + 1
            marker = _line[marker_start:marker_end]

            markers.append(marker)
            _line = _line.replace(marker, '')
            lines[i] = _line

    return markers


madlib_markers = extract_markers(original_madlib)

# ---------------------------------------------
# Asking user to write an input for each marker
# -----------------s----------------------------


madlib_answers = []

for madlib_marker in madlib_markers:
    print(f'Write a {madlib_marker}:')
    answer = input()
    madlib_answers.append(answer)

print(len(madlib_answers))
# ---------------------------------------------------
# Replacing each marker with the corresponding answer
# ---------------------------------------------------


def replace_markers(madlib, markers, answers):
    lines = list(madlib)

    for line_index, line in enumerate(lines):
        _line = str(line)
        for marker_index, marker in enumerate(markers):
            _line = _line.replace(marker, answers[marker_index])
        lines[line_index] = _line

    return lines


final_madlib = replace_markers(original_madlib, madlib_markers, madlib_answers)

# -----------------------------------
# Print final version and prompt save
# -----------------------------------

for madlib_line in final_madlib:
    print(madlib_line)

print()
print("Would you like to save your story? Y/N")

save_choice = input()

if save_choice.lower() == "y" or save_choice.lower() == "yes":
    WRITE_PATH = "my_madlib.txt"

    with open(os.path.join(os.getcwd(), WRITE_PATH), 'w', encoding="utf-8") as file:
        for madlib_line in final_madlib:
            file.write(str(madlib_line) + '\n')
