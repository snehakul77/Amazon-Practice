#Parse errors into a dictionary and with key as timestamp
import csv
import re
import json
filepath = "/Users/apple/Documents/PracticePython/sample.txt"
#output_file = "/Users/apple/Documents/PracticePython/output.txt"

def error_timezone(filepath):
    error_lines = {}
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

    try:
        with open(filepath) as file:
            for line in file:
                if "error" in line.lower():
                    match = re.search(pattern, line)
                    if match:
                        timestamp = match.group()
                        parts = line.split("ERROR",1)
                        if len(parts) > 1:
                            message = parts[1].strip()
                            error_lines[timestamp] = message
            return error_lines
    except FileNotFoundError:
        print("File not found")
        return {}

#def save_to_json(data,output_file):
#    try:
#        with open(output_file, "w") as file:
#            json.dump(data, file, indent=4)
#       print("Data saved to file")

#    except Exception as e:
#        print("File not found")

def save_to_csv(data,output_file):
    with open(output_file,"w",newline = '',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp','error_message'])
        for timestamp,message in data.items():
            writer.writerow([timestamp,message])
        print(f"Successfully saved to csv file {output_file}")



error_log = error_timezone(filepath)
#save_to_json(error_log,output_file)
save_to_csv(error_log,"parsed_error_log.csv")
print(error_log)



