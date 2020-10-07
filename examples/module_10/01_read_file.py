import os


script_dir = os.path.dirname(__file__)
script_dir = os.path.abspath(script_dir)
abs_file_path = os.path.join(script_dir, 'example.txt')


with open(abs_file_path, 'r') as reader:
    for line in reader.readlines():
        print(line)

