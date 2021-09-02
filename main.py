from os import listdir, rename
from os.path import isfile, splitext, join, isdir
from argparse import ArgumentParser
from sys import stderr

# Initializing the CLI tool with four parameters
parser = ArgumentParser(description="Batch rename files, stripping a given substring")
parser.add_argument("path", metavar="path", type=str, default="./", nargs="?", help="Path to directory with files to rename. Defaults to current working directory.")
parser.add_argument("substring", metavar="substring", type=str, help="Substring to strip or replace out of every file in path.")
parser.add_argument("new_string", metavar="new_string", type=str, default="", nargs="?", help="String to replace for every matching substring.")
parser.add_argument('-n', action='store_true', help="Rename all files to substring and number them accordingly.")

def scanDir(path):
    """Takes a path and returns a list of all existing files.

    Args:
        path (str): A resolvable path to search for files in a non-recursive manner.

    Returns:
        list: Valid files in directory.
    """
    if isdir(path): # Making sure it's a valid directory
        files = [f for f in listdir(path) if isfile(join(path, f))] # Filter out files only
        if len(files) > 0:
            return files # Return what was found
        else: 
            print("Directory is empty", file=stderr) # Outputting errors to the standard error stream.
    else:
        print(path, "is not a directory or does not exist.", file=stderr)


def renameFiles(path, files, substring, new_string, numbers):
    """Main renaming function. All ocurrences of substring will be replaced with new_string in a given path 
    that has at least one file. If numbers is set to true, all files will be renamed to substring and will be appended a 
    number in ascending order.

    Args:
        path (str): A resolvable path to look for files in.
        files (list(str)): A list containing valid files in the form of strings.
        substring (str): Substring that will be replaced.
        new_string (str): String to replace substring with.
        numbers (bool): If set to true, all files will be renamed to substring and appended a number in ascending order.

    Returns:
        int: Count of files renamed.
    """
    count = 0 # Final count to return of successful renames

    if files: 
        for file in files:
            name, ext = splitext(file) # Destructuring the name and extension of each file
            newName = name

            if numbers: 
                newName = substring + str(count + 1) # Appending a number if numbers is true

            elif name.find(substring) != -1:
                newName = name.replace(substring, new_string) # Renaming
            
            if numbers or name.find(substring) != -1: # if the numbers flag is present or a file can be renamed, then
                count += 1
                rename("{0}/{1}".format(path, file), "{0}/{1}{2}".format(path, newName, ext))
        

    if count > 0: 
        print("Successfully renamed {0} files.".format(count))
        return count
    else: 
        print("No files renamed.", file=stderr)

if __name__ == '__main__':
    try:
        # Making sure the CLI tool only works when run independently, allowing for modularization and testing
        args = parser.parse_args()
        path = args.path
        substring = args.substring
        numbers = args.n
        new_string = args.new_string

        files = scanDir(path)
        if files:
            renameFiles(path, files, substring, new_string, numbers)

    except Exception as e:
        print(e)
