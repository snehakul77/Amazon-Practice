#Script to read contents of file and print its contents
from curses.ascii import isdigit


#filepath = "/Users/apple/Documents/PracticePython/application.log"
#try:
#    with open(filepath) as f:
#       lines = f.readlines()
#        for line in lines:
#            print(line)
#except FileNotFoundError:
#    print("File not found")

#Create a function square_numbers(n) that returns a list of the first n perfect squares.

#def square_num(n):
#    l = []
#    for i in range(n+1):
#        l.append(i*i)
#    return l

#squared_numbers = square_num(5)
#print(squared_numbers)

#Using Exception Handling, prompt the user to enter an integer and handle cases where the input isn’t a number.

#def check_numbers():
#    try:
#        n = int(input("Enter a number: "))
#        print("Given number is valid")
#        return True
#    except ValueError:
#        print("Invalid Input: Please enter a valid integer")
#        return False

#check_numbers()

#function to return list of odd number

#def odd_numbs(l):
#    return [i for i in l if i % 2 != 0]

#print(odd_numbs([1,2,3,4,5,6,7,]))
#-----------------------------------------
#print string without any white spaces

#text = "   Hello, Amazon!   "
#text = text.strip()
#print(text)
#---------------------------------------
#split usage

#sentence = "This is an Amazon interview"
#words = sentence.split()
#print(words)
#---------------------------------------
#enumerate usage"

##word = "QA"
#for idx,val in enumerate(word):
#    print(idx,val)

#--------------------------------------
#zip usage

#nums = [1, 2, 3]
#chars = ['a', 'b', 'c']

#for k,v in zip(nums, chars):
 #   print(k, v)
#--------------------------------------
#join() usage

#letters = ['A', 'B', 'C']
#letters = '-'.join(letters)
#print(letters)
#----------------------------------------
#map() usage

#str_nums = ['1', '2', '3']

#def convert_int(x):
#    return int(x)

#print(list(map(convert_int, str_nums )))
#------------------------------------------
#filter usage

#numbers = [1, 2, 3, 4, 5, 6]

#def is_even(num):
#    return num % 2 == 0

#print(list(filter(is_even, numbers)))
#--------------------------------------
#range function

#for i in range(5,11):
#    print(i)
#----------------------------------
#Handle IndexError when accessing an index that’s out of range

#def handle_errors(lst):
#    try:
#        if lst[3] == 5:
#            print("Number present")
#    except IndexError:
#        print("Index not present")

#handle_errors([1, 2, 3])
#-----------------------------------
#valueerror

def handle_errors(s):
    try:
        age = int(s)
        print("Converted successfully")
    except ValueError:
        print("Invalid input")

handle_errors("twenty")


