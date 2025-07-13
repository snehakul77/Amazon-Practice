import re
import csv

filepath = "/Users/apple/Documents/PracticePython/server.log"
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(.*?)\] (\w+) (.+)"

#def log_parser(filepath):
#    error_entries= {}
#    try:
#        with open(filepath) as file:
#            for line in file:
#                if "error" in line.lower():
#                    match = re.search(pattern,line)
#                    if match:
#                        timestamp = match.group(1)
#                    parts = line.split("ERROR",3)
#                    #print(parts)
#                    if len(parts) > 1:
#                        component = parts[0].split(" ")
#                        comp = component[2]
#                        level = "ERROR"
 #                       message = parts[1].strip()
#                        error_entries[timestamp] = comp, level, message
#            return error_entries
#    except FileNotFoundError:
#        print("File not found")
#        return ()

#def save_to_csv(error_entries, output_file):
#    with open(output_file,"w",newline="",encoding="utf-8") as file:
#        writer =csv.writer(file)
#        writer.writerow(["timestamp","message info"])
##        for timestamp,message in error_entries.items():
#            writer.writerow([timestamp,message])
#        print(f"Successfully saved to csv file {output_file}")

def log_parser(filepath):
    error_log = []
    try:
        with open(filepath) as file:
            for line in file:
                if "error" in line.lower():
                    match = re.search(pattern,line)
                    if match:
                        timestamp,component, level, message = match.groups()
                        error_log.append({"timestamp":timestamp,"component":component,"level":level,"message":message})
                        print(error_log)
            return error_log
    except FileNotFoundError:
        print("File not found")
        return {}


def save_to_csv(error_log,output_file):
    with open(output_file,"w" ,newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = ["timestamp","component","level","message"])
        writer.writeheader()
        writer.writerows(error_log)
    print(f"Successfully saved to csv file {output_file}")

if __name__ == "__main__":

    error_log = log_parser(filepath)
    save_to_csv(error_log,"error_log.csv")




#parsed_file = log_parser(filepath)
#save_to_csv(parsed_file,"server_log_parsed.csv")
#print(parsed_file)


