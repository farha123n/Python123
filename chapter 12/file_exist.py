from logging import exception


def readfile(file_name):
    try:
        with open(file_name) as f:
            f.read()
    except FileNotFoundError as e:
        print(f" file {file_name} not found")

readfile("txt1.txt")
readfile("txt2.txt")
readfile("txt3.txt")