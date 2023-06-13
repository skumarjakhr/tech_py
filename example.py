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
