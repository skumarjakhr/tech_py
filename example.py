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



def draw_name(name, spaces_between_chars):
    ascii_art = {
        'A': ["  AA  ", " A  A ", "AAAAA", "A    A", "A    A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCCC ", "C     ", "C     ", "C     ", " CCCC "],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
        'G': [" GGGG ", "G     ", "G  GG ", "G   G ", " GGGG "],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
        'J': ["   J ", "   J ", "   J ", "J  J ", " JJ  "],
        'K': ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
        'L': ["L     ", "L     ", "L     ", "L     ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q   Q", "Q  Q ", " QQ Q"],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSSS ", "S     ", " SSSS ", "    S ", " SSSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
        'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
    }

    name = name.upper()

    lines = [""] * 5

    for char in name:
        if char.isalpha():
            if char in ascii_art:
                for i, line in enumerate(ascii_art[char]):
                    lines[i] += line + " " * spaces_between_chars
            else:
                for i in range(5):
                    lines[i] += " " * (7 + spaces_between_chars)
        else:
            for i in range(5):
                lines[i] += " " * (7 + spaces_between_chars)

    for line in lines:
        print(line)


# Example usage
name = input("Enter the name: ")
spaces = int(input("Enter the number of spaces between characters: "))
#print('')
#print('')
#print('')

draw_name(name, spaces)


def get_input_from_clipboard():
    print("Paste your input:")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        except EOFError:
            break
    return lines

# Example usage
input_lines = get_input_from_clipboard()

# Print the input lines
for line in input_lines:
    print(line)



    from pyhive import hive

# Establish a connection
conn = hive.Connection(
    host='your_hive_server_host',
    port=10000,  # Default Hive Server 2 port
    username='your_username',
    password='your_password',
    database='your_database',
)

# Create a cursor
cursor = conn.cursor()

# Execute a query
query = 'SELECT * FROM your_table'
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()









import sys

def get_input_from_clipboard():
    # Read the clipboard contents from sys.stdin
    clipboard_text = sys.stdin.read()
    
    # Split the clipboard text into lines
    lines = clipboard_text.splitlines()
    
    return lines

# Example usage
input_lines = get_input_from_clipboard()

# Print the input lines
for line in input_lines:
    print(line)





from impala.dbapi import connect
import pandas as pd

# Establish a connection to Hive Server 2
conn = connect(host='your_hive_server_host', port=your_hive_server_port, database='your_database')

# Execute Hive queries using pandas
query = 'SELECT * FROM your_table'
df = pd.read_sql(query, conn)

# Display the DataFrame
print(df)



import pyodbc
import pandas as pd

# Configure the ODBC connection string
conn_str = "DSN=your_hive_odbc_dsn;UID=your_username;PWD=your_password"

# Establish a connection
conn = pyodbc.connect(conn_str)

# Execute Hive queries using pandas
query = 'SELECT * FROM your_table'
df = pd.read_sql(query, conn)




from impala.dbapi import connect
import pandas as pd

# Establish a connection to Hive Server 2
conn = connect(host='your_hive_server_host', port=your_hive_server_port, database='your_database',
               auth_mechanism='PLAIN', user='your_username', password='your_password')

# Execute Hive queries using pandas
query = 'SELECT * FROM your_table'
df = pd.read_sql(query, conn)

# Export the DataFrame to an Excel file
excel_file = 'data.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data exported to {excel_file}")










import subprocess

# SFTP server details
sftp_host = 'your_sftp_server_host'
sftp_username = 'your_sftp_username'
sftp_password = 'your_sftp_password'
remote_file_path = '/path/to/cloak-hiveconnector'

# Hive query
hive_query = 'SELECT * FROM your_table'

# Command to execute the "cloak-hiveconnector" executable with the query
command = f'ssh -p "{sftp_password}" sftp -oStrictHostKeyChecking=no {sftp_username}@{sftp_host}:{remote_file_path} ./cloak-hiveconnector -e "{hive_query}"'

# Execute the command and capture the output
output = subprocess.check_output(command, shell=True)

# Decode the output as per the appropriate encoding (if needed)
output = output.decode('utf-8')

# Print the output
print(output)



import subprocess

# PuTTY session details
putty_host = 'your_putty_host'
putty_username = 'your_putty_username'
putty_password = 'your_putty_password'
putty_command = 'your_putty_command'

# Construct the plink command
command = f'plink -ssh {putty_username}@{putty_host} -pw {putty_password} {putty_command}'

# Execute the command and capture the output
output = subprocess.check_output(command, shell=True)

# Decode the output as per the appropriate encoding (if needed)
output = output.decode('utf-8')

# Print the output
print(output)




