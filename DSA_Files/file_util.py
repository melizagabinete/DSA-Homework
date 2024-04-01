import os
class FileUtil:
    def create_file(filename, data):
        try:
            with open(filename, 'w') as f:
                f.write(f'{data} \n')
            print("File "+ filename + "created successfully.")
        except IOError:
            print("Error: could not create file "+filename)

    def read_file(filename):
        try:
            with open(filename, 'r') as f:
                contents = f.read()
                print(contents)
        except IOError:
            print("Enter: could not read file " + filename)

    def append_file(filename, text):
        try:
            with open(filename, 'a') as f:
                f.write(text)
            print("Text appended to file" + filename + "succesfully")
        except IOError:
            print("Error: could not append to file " + filename)

    def rename_file(filename, new_filename):
        try:
            os.rename(filename, new_filename)
            print("File " + filename + "renamed to" + new_filename + "succesfully.")
        except IOError:
            print("Error: could not rename file " + filename)

    def delete_file(filename):
        try:
            os.remove(filename)
            print("File " + filename + "delete successfully.")
        except IOError:
            print("error: could not delte file " + filename)
