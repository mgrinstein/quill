# File that prints the contents of all text files in a given directory
# including subdirectories.
# Usage: python printdir.py <directory>
# Example: python printdir.py /home/username/Documents

import os
import sys

def printdir(directory, output_file=""):
    if output_file != "":
        f = open(output_file, 'w')
    else:
        f = None

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                printfile(os.path.join(root, file), f)

    if f is not None:
        f.close()

def printfile(file_path, f=None):
    if f is None:
        print(file_path)
    else:
        f.write(file_path + '\n')

    with open(file_path, 'r') as g:
        if f is None:
            print(g.read())
        else:
            f.write(g.read() + '\n')


if __name__ == '__main__':
    output_file = "test.txt"
    printdir(sys.argv[1], output_file)
