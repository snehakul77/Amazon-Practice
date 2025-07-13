import re

file_path = "/Users/apple/Documents/PracticePython/sample.txt"

def count_errors(file_path):
    error_count = 0
    try:
        with open(file_path) as file:
            for line in file:
                if "error" in line.lower():
                    error_count += 1
            return error_count
    except FileNotFoundError:
        print("File not found")
        return -1

print(count_errors(file_path))

def find_error_timezone(file_path):
    error_count = 0
    error_lines = []
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    try:
        with open(file_path) as file:
            for line in file:
                if "error" in line.lower():
                    match = re.search(pattern, line)
                    if match:
                        error_lines.append(match.group())
            return error_lines
    except FileNotFoundError:
        print("File not found")
        return -1

print(find_error_timezone(file_path))


