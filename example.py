data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)


import os
import subprocess

def create_and_open_folder(folder_path):
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)

    # Open the folder in the file explorer/finder
    if os.name == 'nt':  # For Windows
        subprocess.Popen(f'explorer "{folder_path}"')
    elif os.name == 'posix':  # For macOS/Linux
        subprocess.Popen(['open', folder_path])

# Example usage
folder_path = 'C:/path/to/folder'  # Specify the desired folder path
create_and_open_folder(folder_path)



def draw_name(name):
    special_chars = {
        'A': '@',
        'B': '8',
        'C': '(',
        'D': '|)',
        'E': '3',
        'F': '|=',
        'G': '6',
        'H': '|-|',
        'I': '!',
        'J': '_|',
        'K': '|<',
        'L': '1',
        'M': '|\\/|',
        'N': '|\\|',
        'O': '0',
        'P': '|D',
        'Q': '(,)',
        'R': '|2',
        'S': '$',
        'T': '7',
        'U': '|_|',
        'V': '\\/',
        'W': '\\/\\/',
        'X': '><',
        'Y': '`/',
        'Z': '2',
    }

    name = name.upper()  # Convert the name to uppercase

    for char in name:
        if char.isalpha():
            if char in special_chars:
                print(special_chars[char], end='')
            else:
                print(char, end='')
        else:
            print(char, end='')

# Example usage
name = 'John'
draw_name(name)

