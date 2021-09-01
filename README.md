# batch-rename

A CLI tool to help batch renaming of files.

## Installation

1. Get the [ZIP](https://github.com/POWRFULCOW89/batch-rename/archive/refs/tags/0.1.0.zip) or clone the repo:

    ```sh
    gh repo clone POWRFULCOW89/batch-rename
    ```

2. Initialize a virtual environment:

    ```sh
    python -m venv env
    ```

    And activate it:

    ```sh
    .\env\Scripts\activate
    ```

3. Install the dependencies:

    ```sh
    (env) pip install -r requirements.txt
    ```

4. Build from source:

    ```sh
    (env) pyinstaller --onefile main.py
    ```

    Or grab the latest [release](https://github.com/POWRFULCOW89/batch-rename/releases).

5. (Optional) [Add compiled .exe to PATH](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/).

## Usage

1. Help flag:

    ```sh
    batch-rename -h
    ```

    Outputs:

    ```txt
    usage: batch-renamepy.exe [-h] [-n] [path] substring [new_string]
    
    Batch rename files, stripping a given substring
    
    positional arguments:
      path        Path to directory with files to rename. Defaults to current working directory.
      substring   Substring to strip or replace out of every file in path.
      new_string  String to replace for every matching substring. Defaults to an empty string.
    
    optional arguments:
      -h, --help  show this help message and exit
      -n          Rename all files to substring and number them accordingly.
    ```

2. Strip all ocurrences of "log" in the current directory:

    ```sh
    batch-rename log
    ```

3. Strip all ocurrences of "python" in an absolute path:

    ```sh
    batch-rename "C:/Users/<you>/Documents/PDF" python
    ```

4. Rename all files in the "Songs" subdirectory numerically with a starting string:

    ```sh
    batch-rename Music/Songs "Track - " -n
    ```

5. Replace all ocurrences of "log" with "report" in the current directory:

    ```sh
    batch-rename ./ log report
    ```

## TO-DO

- [ ] RegEx support
- [ ] Tests