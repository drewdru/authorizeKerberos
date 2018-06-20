#! ./env/bin/python
import os
def add_string_to_file(text, file_name):
    with open(file_name, "r+") as file:
        for line in file:
            if text in line:
                break
        else:
            file.write('\n{}'.format(text))

def replace_file_line(filename, old_line, new_line):    
    tempname = filename + '.temp'
    with open(filename, 'r') as fin:
        with open(tempname, 'w') as fout:
            for line in fin:
                line = line.rstrip('\n')
                if line != old_line:
                    fout.write
                else:
                    fout.write('{}\n'.format(new_line))
    os.rename(tempname, filename)