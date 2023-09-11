#Created By Aniketh_Rai 2023
"""Description: 
                This program combines input words and adds comma's to each word and combines them to a paragraph.
                Helpfull when combining keywords and making it a section in a Resume.
"""

import sys

# Initialize an empty list to store the inputs
input_lines = []

# Loop to read input lines until an empty line is encountered
while True:
    # Read a line of input from the command line
    line = input("Enter a line of text (or press Enter to finish): ")
    
    # Check if the line is empty (user pressed Enter)
    if not line:
        break
    
    # Append the input line to the list
    input_lines.append(line)

# Writing to a File name = Output.txt
paragraph = ''
for line in input_lines:
    paragraph += ',' + line
final_para = paragraph[1::] + '.'

output_file_name = "output.txt" #output file name

with open(output_file_name, "w") as output_file: #Writing final_para to output file
    output_file.write(final_para)
    
print('Done')
