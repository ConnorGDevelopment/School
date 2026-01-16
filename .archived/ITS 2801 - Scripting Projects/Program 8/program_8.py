import operator
import sys
import os

# ------------------------------------------
# Open File, Prefer cmd args, prompt if fail
# ------------------------------------------


# This took a bit of time because the assignment said to use cmd args and handle FileNotFoundError(s)
FILE_PATH = ""

# Found how to do cmd args from searching and stumbling onto: https://docs.python.org/3/library/sys.html#sys.argv
if len(sys.argv) >= 2:
    FILE_PATH = sys.argv[1]

#  Found how to check if a path is valid from: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
filepath_is_valid = os.path.isfile(FILE_PATH)

while filepath_is_valid is False:
    print("File not found")

    print("Please enter the relative path to the file you would like to evaluate:")
    user_input = input()

    # It took a good deal of debugging to figure out why this wasn't working
    # Eventually I realized I was trying to read a path of 'batch.txt' instead of 'C://foo/bar/batch.txt
    FILE_PATH = os.path.join(os.getcwd(), user_input)

    filepath_is_valid = os.path.isfile(FILE_PATH)

# ---------------------
# The Actual Assignment
# ---------------------


def eval_arithmetic(_raw_line):
    lines = _raw_line.strip()
    lines = lines.split(" ")
    for line in lines:
        line = line.strip()

    match lines[0]:
        case "#":
            return None
        case "!":
            return _raw_line

    # This is fully outside what we've covered in the course
    # I wanted to learn how to actually pass dynamic operators
    # Originally I did a match block
    # Found the module here: https://docs.python.org/3/library/operator.html
    operator_map = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul
    }

    return operator_map[lines[1]](float(lines[0]), float(lines[2]))


# My linter recommended using with instead of a normal assign to make sure it lets go of the file in every scenario
with open(FILE_PATH, encoding="utf-8-sig") as file:
    file_choice = file.readlines()

for raw_line in file_choice:
    try:
        result = eval_arithmetic(raw_line)
        if result is not None:
            print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except (IndexError, KeyError):
        print("Line could not be parsed a three part arithmetic equation")
    except Exception as e:
        # Had to dig around to find where the error type was buried
        # Found it in this post: https://stackoverflow.com/questions/9823936/how-do-i-determine-what-type-of-exception-occurred
        print(f"{e.__class__.__name__}: {raw_line}")
