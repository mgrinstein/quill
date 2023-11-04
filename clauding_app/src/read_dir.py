# File that prints the contents of all text files in a given directory
# including subdirectories.
# Usage: python read_dir.py <directory>
# Example: python read_dir.py /home/username/Documents

import os

def read_dir(directory, output_file=""):
    output = ""

    if output_file != "":
        f = open(output_file, 'w')
    else:
        f = None

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                output += process_file(os.path.join(root, file), f)

    if f is not None:
        f.close()

    return output


def process_file(file_path, f=None):
    output = file_path + '\n'
    output += "----------------------------------\n"
    
    with open(file_path, 'r') as g:
        output += g.read() + '\n'
        
    if f is not None:    
        f.write(output + '\n')
    
    return output
