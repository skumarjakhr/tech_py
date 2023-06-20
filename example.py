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
j



import clr
clr.AddReference("Microsoft.VisualBasic")

from Microsoft.VisualBasic import Interaction

# Prompt the user to enter their name
name = Interaction.InputBox("Please enter your name:", "Name Input")

# Display a message with the entered name
message = f"Hello, {name}!"
Interaction.MsgBox(message)


import clr
clr.AddReference("System.IO")

from System.IO import File

# Get the list of attributes and methods of the File class
file_dir = dir(File)

# Print the list
for item in file_dir:
    print(item)


import tkinter as tk
import tkinter.messagebox as msgbox
import time

def show_timeout_message(message, timeout_seconds):
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Display the message box with the specified message
    msgbox.showinfo("Timeout Message", message)

    # Wait for the specified timeout duration
    time.sleep(timeout_seconds)

    # Close the root window
    root.destroy()

# Usage example
message = "This is a timeout message."
timeout_seconds = 5

show_timeout_message(message, timeout_seconds)




import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon

def show_timeout_message(message, timeout_seconds):
    # Create a MessageBox instance
    msg_box = MessageBox()

    # Set the properties of the message box
    msg_box.Text = "Timeout Message"
    msg_box.Icon = MessageBoxIcon.Warning
    msg_box.Buttons = MessageBoxButtons.OK
    msg_box.DefaultButton = MessageBoxDefaultButton.Button1

    # Display the message box with the specified message
    msg_box.Show(message)

    # Wait for the specified timeout duration
    import time
    time.sleep(timeout_seconds)

    # Close the message box
    msg_box.Close()

# Usage example
message = "This is a timeout message."
timeout_seconds = 5

show_timeout_message(message, timeout_seconds)


import paramiko
import pandas as pd

# SSH connection details
hostname = 'your_hostname'
username = 'your_username'
password = 'your_password'
command = 'your_hive_command'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Execute Hive command
stdin, stdout, stderr = ssh.exec_command(command)

# Read output into a Pandas DataFrame
data = []
for line in stdout:
    # Assuming each line of output is a comma-separated row
    row = line.strip().split(',')
    data.append(row)

# Close SSH connection
ssh.close()

# Convert data to DataFrame
df = pd.DataFrame(data)

# If data is too large, save it in batches to CSV files
if len(df) > 10000:
    batch_size = 1000
    num_batches = len(df) // batch_size + 1

    for i in range(num_batches):
        start = i * batch_size
        end = (i + 1) * batch_size
        batch_df = df[start:end]

        # Save batch DataFrame to a CSV file
        filename = f'output_batch_{i}.csv'
        batch_df.to_csv(filename, index=False)

# Alternatively, if data is small, you can process it directly
else:
    # Process the DataFrame as needed
    # ...



import paramiko

# SSH connection details
hostname = 'your_hostname'
username = 'your_username'
password = 'your_password'
command = 'your_command'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Open a shell session
shell = ssh.invoke_shell()

# Execute the command
shell.send(command + '\n')

# Read and print the output while the command is executing
while not shell.exit_status_ready():
    if shell.recv_ready():
        output = shell.recv(4096).decode('utf-8')
        print(output, end='')

# Close the shell session and SSH connection
shell.close()
ssh.close()


import paramiko

# SSH connection details
hostname = 'your_hostname'
username = 'your_username'
password = 'your_password'
command = 'your_command'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Open a shell session
shell = ssh.invoke_shell()

# Execute the command
shell.send(command + '\n')

# Read and print the output while the command is executing
while not shell.exit_status_ready():
    if shell.recv_ready():
        output = shell.recv(4096).decode('utf-8')
        print(output, end='')

# Check the exit status of the shell session
exit_status = shell.recv_exit_status()

# Print the exit status
print('Exit Status:', exit_status)

# Close the shell session and SSH connection
shell.close()
ssh.close()




import paramiko

# SSH connection details
hostname = 'your_hostname'
username = 'your_username'
password = 'your_password'
command = 'your_command'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Execute the command
stdin, stdout, stderr = ssh.exec_command(command)

# Read and print the output
for line in stdout:
    print(line.strip())

# Check if there were any errors
error = stderr.read().decode('utf-8')
if error:
    print('Error:', error)

# Close the SSH connection
ssh.close()


CREATE EXTERNAL TABLE csv_table
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar" = "\"",
  "escapeChar" = "\\"
)
STORED AS TEXTFILE
LOCATION '/path/to/csv/file'
TBLPROPERTIES (
  "skip.header.line.count" = "1"
);

SELECT * FROM csv_table;




