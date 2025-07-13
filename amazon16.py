#Compare 2 files and create a list of differences
import csv
filepath1 ="/Users/apple/Documents/PracticePython/file1.txt"
filepath2 = "/Users/apple/Documents/PracticePython/file2.txt"
output_csv = "/Users/apple/Documents/PracticePython/output.csv"
def compare_files(file1,file2):
    try:
        with open(file1,"r") as f1 , open(file2,"r") as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        differences = []

        for i, (line1,line2) in enumerate(zip(lines1,lines2)):
            if line1!=line2:
                differences.append((i+1 , line1.strip(),line2.strip()))

        if len(lines1)!= len(lines2):
                longer = lines1 if len(lines1)>len(lines2) else lines2
                for j in range(min(len(lines1),len(lines2)),max(len(lines1),len(lines2))):
                    if longer is lines1:
                        differences.append((j+1 ,longer[j].strip(),''))
                    else:
                        differences.append((j+1 ,longer[j].strip()))

        return differences
    except Exception as e:
        print("Error while comparing files:")
        return []

def save_to_csv(differences,outputfile):
    with open(outputfile,"w",newline = '',encoding = 'utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(["Line Number","File1","File2"])
        for diff in differences:
            writer.writerow(diff)
    print("CSV file saved successfully")





diff = compare_files (filepath1,filepath2)
for diff in diff:
    print(diff)

save_to_csv(diff, output_csv)
