# title: Reading Files  
# Working with files

from sys import argv

script, filename = argv

txt = open(filename) 

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type filename again : ")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read()) 
