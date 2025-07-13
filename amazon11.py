import re
import json

filepath = "/Users/apple/Documents/PracticePython/application.log"
time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
error_lines = {}

def log_parser(filepath):
    error_lines = {}
    try:
        with open(filepath , "r") as file:
            for line in file:
                if "error" in line.lower():
                    match = re.search(time_pattern,line)
                    if match:
                        timestamp = match.group()
                        parts = line.split("ERROR",1)
                        print(parts)
                        if len(parts) > 1:
                            error_lines[timestamp] = parts[1].strip()
                elif "warning" in line.lower():
                    match = re.search(time_pattern,line)
                    if match:
                        timestamp = match.group()
                        parts = line.split("WARNING",1)
                        if len(parts) > 1:
                            error_lines[timestamp] = parts[1].strip()
                elif "info" in line.lower():
                    match = re.search(time_pattern,line)
                    if match:
                        timestamp = match.group()
                        parts = line.split("INFO",1)
                        if len(parts) > 1:
                            error_lines[timestamp] = parts[1].strip()
                elif "debug" in line.lower():
                    match = re.search(time_pattern,line)
                    if match:
                        timestamp = match.group()
                        parts = line.split("DEBUG",1)
                        if len(parts) > 1:
                            error_lines[timestamp] = parts[1].strip()
            return error_lines

    except Exception as e:
        print("File not found")
        return {}

print(log_parser(filepath))




