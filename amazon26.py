#File I/O operations

file_path= "/Users/apple/Documents/PracticePython/file3.txt"
def file_handle(file_path):
    try:
        with open(file_path,"a") as f:
            f.write("Mango")
            lines = f.readlines()
            print(lines)
    except FileNotFoundError:
        print("File not found")

file_handle(file_path)

