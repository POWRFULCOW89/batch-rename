from os import listdir, rename
from os.path import isfile, splitext, join, isdir
from argparse import ArgumentParser

parser = ArgumentParser(description="Batch rename files, stripping a given substring")

parser.add_argument("path", metavar="path", type=str, default="./", nargs="?", help="Path to directory with files to rename. Defaults to current working directory.")
parser.add_argument("substring", metavar="substring", type=str, help="Substring to strip or replace out of every file in path.")
parser.add_argument("new_string", metavar="new_string", type=str, default="", nargs="?", help="String to replace for every matching substring.")
parser.add_argument('-n', action='store_true', help="Rename all files to substring and number them accordingly.")

args = parser.parse_args()
path = args.path
substring = args.substring
numbers = args.n
new_string = args.new_string

def scanDir():
    if isdir(path):
        files = [f for f in listdir(path) if isfile(join(path, f))] # Filter out files only
        if len(files) > 0:
            return files # Return what was found
        else: 
            print("Directory is empty")
    else:
        print(path, "is not a directory or does not exist.")


def renameFiles(files):
    count = 0

    for file in files:

        name, ext = splitext(file)

        newName = name

        if numbers: 
            newName = substring + str(count + 1)

        elif name.find(substring) != -1:
            newName = name.replace(substring, new_string)
        
        if numbers or name.find(substring) != -1: # if the numbers flag is present or a file can be renamed, then
            count += 1
            rename("{0}/{1}".format(path, file), "{0}/{1}{2}".format(path, newName, ext))
        

    if count > 0: 
        print("Successfully renamed {0} files.".format(count))
    else: 
        print("No files renamed.")

if __name__ == '__main__':
    try:
        files = scanDir()
        if files:
            renameFiles(files)

    except Exception as e:
        print(e)
