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




import tkinter as tk
from tkinter import ttk
import sqlite3
import csv
import webbrowser
import os

# Create a connection to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Clear existing data in the result_treeview
        result_treeview.delete(*result_treeview.get_children())
        # Insert the column names as headings in the result_treeview
        column_names = [description[0] for description in cursor.description]
        result_treeview["columns"] = column_names
        result_treeview.heading("#0", text="Row")
        for column in column_names:
            result_treeview.heading(column, text=column)
        # Insert the data rows in the result_treeview
        for i, row in enumerate(rows):
            result_treeview.insert("", tk.END, text=i+1, values=row)
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Rest of the code...

# Create a Treeview widget to display the query results
result_treeview = ttk.Treeview(window)
result_treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the result_treeview
result_scrollbar = tk.Scrollbar(window, orient="vertical", command=result_treeview.yview)
result_treeview.configure(yscrollcommand=result_scrollbar.set)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Treeview columns and headings
result_treeview["columns"] = ("#0", "Column1", "Column2", ...)  # Replace with actual column names
result_treeview.heading("#0", text="Row")
result_treeview.column("#0", width=50, anchor="center")
result_treeview.column("Column1", width=100, anchor="center")
result_treeview.column("Column2", width=100, anchor="center")
...

# Rest of the code...

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()















import tkinter as tk
import sqlite3
import csv
import webbrowser
import os

# Create a connection to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Display the results in the result_text Text widget
        result_text.delete("1.0", tk.END)
        for row in rows:
            result_text.insert(tk.END, str(row) + "\n")
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Function to update the table list in the table_listbox
def update_table_list():
    table_listbox.delete(0, tk.END)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_listbox.insert(tk.END, table[0])

# Function to export the table data to a CSV file
def export_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    result_text.insert(tk.END, "Table data exported to " + filename + "\n")
    result_text.insert(tk.END, "File location: " + os.path.abspath(filename) + "\n")

# Function to export the entire table as a CSV file
def export_entire_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    webbrowser.open_new_tab(os.path.abspath(filename))

# Create the main window
window = tk.Tk()
window.title("SQLite Browser")

# Create a Text widget for entering SQL queries
query_text = tk.Text(window, height=10, width=50)
query_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the query_text Text widget
query_scrollbar = tk.Scrollbar(window)
query_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
query_text.config(yscrollcommand=query_scrollbar.set)
query_scrollbar.config(command=query_text.yview)

# Create a Button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack(side=tk.LEFT)

# Create a Text widget to display the query results
result_text = tk.Text(window, height=10, width=50)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the result_text Text widget
result_scrollbar = tk.Scrollbar(window)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=result_scrollbar.set)
result_scrollbar.config(command=result_text.yview)

# Create a Listbox to display the tables in the database
table_listbox = tk.Listbox(window, height=20)
table_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
table_listbox.bind("<Button-3>", lambda e: table_menu.post(e.x_root, e.y_root))

# Create a ContextMenu for the table_listbox
table_menu = tk.Menu(table_listbox, tearoff=False)
table_menu.add_command(label="Export Table", command=export_table)
table_menu.add_command(label="Export Entire Table", command=export_entire_table)

# Update the table list
update_table_list()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()




import tkinter as tk
import sqlite3
import csv
import webbrowser

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Display the results in the result_text Text widget
        result_text.delete("1.0", tk.END)
        for row in rows:
            result_text.insert(tk.END, str(row) + "\n")
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Function to update the table list in the table_listbox
def update_table_list():
    table_listbox.delete(0, tk.END)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_listbox.insert(tk.END, table[0])

# Function to export the table data to a CSV file
def export_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    result_text.insert(tk.END, "Table data exported to " + filename + "\n")
    result_text.insert(tk.END, "File location: " + os.path.abspath(filename) + "\n")

# Function to export the entire table as a CSV file
def export_entire_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    webbrowser.open_new_tab(os.path.abspath(filename))

# Create the main window
window = tk.Tk()
window.title("SQLite Browser")

# Create a Text widget for entering SQL queries
query_text = tk.Text(window, height=10, width=50)
query_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the query_text Text widget
query_scrollbar = tk.Scrollbar(window)
query_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
query_text.config(yscrollcommand=query_scrollbar.set)
query_scrollbar.config(command=query_text.yview)

# Create a Button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack(side=tk.LEFT)

# Create a Text widget to display the query results
result_text = tk.Text(window, height=10, width=50)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the result_text Text widget
result_scrollbar = tk.Scrollbar(window)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=result_scrollbar.set)
result_scrollbar.config(command=result_text.yview)

# Create a Listbox to display the tables
table_listbox = tk.Listbox(window, height=10, width=20)
table_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
table_listbox.bind("<Button-3>", lambda e: table_menu.post(e.x_root, e.y_root))

# Create a ContextMenu for the table_listbox
table_menu = tk.Menu(table_listbox, tearoff=False)
table_menu.add_command(label="Export Table", command=export_table)
table_menu.add_command(label="Export Entire Table", command=export_entire_table)

# Update the table list
update_table_list()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()




import tkinter as tk
import sqlite3
import csv
import webbrowser

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Display the results in the result_text Text widget
        result_text.delete("1.0", tk.END)
        for row in rows:
            result_text.insert(tk.END, str(row) + "\n")
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Function to update the table list in the table_listbox
def update_table_list():
    table_listbox.delete(0, tk.END)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_listbox.insert(tk.END, table[0])

# Function to export the table data to a CSV file
def export_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    result_text.insert(tk.END, "Table data exported to " + filename + "\n")
    result_text.insert(tk.END, "File location: " + os.path.abspath(filename) + "\n")

# Function to export the entire table as a CSV file
def export_entire_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    webbrowser.open_new_tab(os.path.abspath(filename))

# Create the main window
window = tk.Tk()
window.title("SQLite Browser")

# Create a Text widget for entering SQL queries
query_text = tk.Text(window, height=10, width=50)
query_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the query_text Text widget
query_scrollbar = tk.Scrollbar(window)
query_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
query_text.config(yscrollcommand=query_scrollbar.set)
query_scrollbar.config(command=query_text.yview)

# Create a Button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack(side=tk.LEFT)

# Create a Text widget to display the query results
result_text = tk.Text(window, height=10, width=50)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the result_text Text widget
result_scrollbar = tk.Scrollbar(window)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=result_scrollbar.set)
result_scrollbar.config(command=result_text.yview)

# Create a Listbox to display the tables
table_listbox = tk.Listbox(window, height=10, width=20)
table_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
table_listbox.bind("<Button-3>", lambda e: table_menu.post(e.x_root, e.y_root))

# Create a ContextMenu for the table_listbox
table_menu = tk.Menu(table_listbox, tearoff=False)
table_menu.add_command(label="Export Table", command=export_table)
table_menu.add_command(label="Export Entire Table", command=export_entire_table)

# Update the table list
update_table_list()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()


import tkinter as tk
import sqlite3
import csv

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Display the results in the result_text Text widget
        result_text.delete("1.0", tk.END)
        for row in rows:
            result_text.insert(tk.END, str(row) + "\n")
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Function to update the table list in the table_listbox
def update_table_list():
    table_listbox.delete(0, tk.END)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_listbox.insert(tk.END, table[0])

# Function to export the table data to a CSV file
def export_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + " LIMIT 100;")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    result_text.insert(tk.END, "Table data exported to " + filename + "\n")

# Create the main window
window = tk.Tk()
window.title("SQLite Browser")

# Create a Text widget for entering SQL queries
query_text = tk.Text(window, height=10, width=50)
query_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the query_text Text widget
query_scrollbar = tk.Scrollbar(window)
query_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
query_text.config(yscrollcommand=query_scrollbar.set)
query_scrollbar.config(command=query_text.yview)

# Create a Button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack(side=tk.LEFT)

# Create a Text widget to display the query results
result_text = tk.Text(window, height=10, width=50)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar for the result_text Text widget
result_scrollbar = tk.Scrollbar(window)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=result_scrollbar.set)
result_scrollbar.config(command=result_text.yview)

# Create a Listbox to display the tables
table_listbox = tk.Listbox(window, height=10, width=20)
table_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a Button to export table data to CSV
export_button = tk.Button(window, text="Export Table", command=export_table)
export_button.pack(side=tk.LEFT)

# Create a context menu for the table_listbox
table_menu = tk.Menu(window, tearoff=False)
table_menu.add_command(label="View Top 100 Lines", command=export_table)

# Function to handle right-click on table_listbox
def show_table_menu(event):
    table_menu.post(event.x_root, event.y_root)

# Bind right-click event to the table_listbox
table_listbox.bind("<Button-3>", show_table_menu)

# Connect to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

# Update the table list
update_table_list()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()




import tkinter as tk
import sqlite3
import csv

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Display the results in the result_text Text widget
        result_text.delete("1.0", tk.END)
        for row in rows:
            result_text.insert(tk.END, str(row) + "\n")
            
        # Update the table list in the table_listbox
        update_table_list()
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Function to update the table list in the table_listbox
def update_table_list():
    table_listbox.delete(0, tk.END)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_listbox.insert(tk.END, table[0])

# Function to export the table data to a CSV file
def export_table():
    table_name = table_listbox.get(tk.ACTIVE)
    if not table_name:
        return
    filename = table_name + ".csv"
    cursor.execute("SELECT * FROM " + table_name + ";")
    rows = cursor.fetchall()
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([description[0] for description in cursor.description])
        csv_writer.writerows(rows)
    result_text.insert(tk.END, "Table data exported to " + filename + "\n")

# Create the main window
window = tk.Tk()
window.title("SQLite Browser")

# Create a Text widget for entering SQL queries
query_text = tk.Text(window, height=10, width=50)
query_text.pack()

# Create a Button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack()

# Create a Text widget to display the query results
result_text = tk.Text(window, height=10, width=50)
result_text.pack()

# Create a Listbox to display the tables
table_listbox = tk.Listbox(window, height=10, width=50)
table_listbox.pack()

# Create a Button to export table data to CSV
export_button = tk.Button(window, text="Export Table", command=export_table)
export_button.pack()

# Connect to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

# Update the table list
update_table_list()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()


import tkinter as tk
import sqlite3

# Function to execute SQL query and fetch results
def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        # Display the results in the result_text Text widget
        result_text.delete("1.0", tk.END)
        for row in rows:
            result_text.insert(tk.END, str(row) + "\n")
    except sqlite3.Error as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("SQLite Browser")

# Create a Text widget for entering SQL queries
query_text = tk.Text(window, height=10, width=50)
query_text.pack()

# Create a Button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack()

# Create a Text widget to display the query results
result_text = tk.Text(window, height=10, width=50)
result_text.pack()

# Connect to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()



import tkinter as tk
import sqlite3
import csv

# Function to execute the SQL query
def execute_query():
    query = query_text.get("1.0", tk.END).strip()
    if query:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                result_text.delete("1.0", tk.END)
                for row in result:
                    result_text.insert(tk.END, str(row) + "\n")
        except sqlite3.Error as e:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "Error: " + str(e))

# Function to export query results to CSV
def export_to_csv():
    query = query_text.get("1.0", tk.END).strip()
    if query:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                with open("output.csv", "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(result)
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, "Query results exported to output.csv")
        except sqlite3.Error as e:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("SQLite Client")

# Create and connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Function to retrieve table names from the database
def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

# Create a dropdown menu for table selection
table_names = get_table_names()
table_var = tk.StringVar()
table_var.set(table_names[0])
table_dropdown = tk.OptionMenu(window, table_var, *table_names)
table_dropdown.pack()

# Function to retrieve column names for a given table
def get_column_names(table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    return [column[1] for column in columns]

# Create a table column listbox
column_listbox = tk.Listbox(window)
column_listbox.pack()

# Function to update the column listbox based on the selected table
def update_column_listbox(*args):
    table_name = table_var.get()
    column_names = get_column_names(table_name)
    column_listbox.delete(0, tk.END)
    for column in column_names:
        column_listbox.insert(tk.END, column)

# Bind the table dropdown to update the column listbox
table_var.trace("w", update_column_listbox)

# Create a text area for entering SQL queries
query_text = tk.Text(window, height=6)
query_text.pack()

# Create a button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack()

# Create a button to export query results to CSV
export_button = tk.Button(window, text="Export to CSV", command=export_to_csv)
export_button.pack()

# Create a text area to display the query results
result_text = tk.Text(window, height=10)
result_text.pack()

# Start the Tkinter event loop
window.mainloop()




import tkinter as tk
import sqlite3

# Function to execute the SQL query
def execute_query():
    query = query_text.get("1.0", tk.END).strip()
    if query:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                result_text.delete("1.0", tk.END)
                for row in result:
                    result_text.insert(tk.END, str(row) + "\n")
        except sqlite3.Error as e:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("SQLite Client")

# Create and connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create a text area for entering SQL queries
query_text = tk.Text(window, height=6)
query_text.pack()

# Create a button to execute the query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack()

# Create a text area to display the query results
result_text = tk.Text(window, height=10)
result_text.pack()

# Start the Tkinter event loop
window.mainloop()






import tkinter as tk
from tkinter import messagebox
import sqlite3
import csv
import pandas as pd
from pandastable import Table

conn = sqlite3.connect("mydatabase.db")
cursor=conn.cursor()

def connect_to_database():
    """Connect to the SQLite database."""
    try:
        db_path = db_path_entry.get()
        conn = sqlite3.connect(db_path)
        messagebox.showinfo("Success", "Connected to the database successfully.")
        return conn, conn.cursor()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to connect to the database:\n{str(e)}")
        return None, None

def execute_query():
    """Execute the SQL query and display the results."""
    query = query_text.get(1.0, tk.END).strip()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        if result:
            result_frame.destroy()
            result_frame = tk.Frame(root)
            result_frame.grid(row=2, column=1, sticky="nsew")

            table = Table(result_frame, dataframe=pd.DataFrame(result, columns=column_names))
            table.show()

            export_button = tk.Button(root, text="Export", command=lambda: export_to_csv(result, column_names))
            export_button.grid(row=3, column=1, pady=10)
        else:
            messagebox.showinfo("Result", "Query executed successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error executing query:\n{str(e)}")

def export_to_csv(data, column_names):
    """Export the query results to a CSV file."""
    try:
        filename = "output.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(column_names)
            writer.writerows(data)
        messagebox.showinfo("Success", f"Data exported to {filename} successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error exporting data:\n{str(e)}")

def get_table_list():
    """Retrieve the list of tables in the database."""
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        table_listbox.delete(0, tk.END)
        for table in tables:
            table_listbox.insert(tk.END, table[0])
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error retrieving table list:\n{str(e)}")

root = tk.Tk()
root.title("SQLite Query Tool")
root.geometry("800x600")

# Database Path
db_path_label = tk.Label(root, text="Database Path:")
db_path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

db_path_entry = tk.Entry(root, width=50)
db_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

connect_button = tk.Button(root, text="Connect", command=connect_to_database)
connect_button.grid(row=0, column=2, padx=10, pady=10)

# Query Entry and Execution
query_text = tk.Text(root, height=10, width=50)
query_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")

execute_button = tk.Button(root, text="Execute", command=execute_query)
execute_button.grid(row=1, column=1, padx=10, pady=10)

# Result Frame
result_frame = tk.Frame(root)
result_frame.grid(row=2, column=1, sticky="nsew")

# Table List
table_list_label = tk.Label(root, text="Tables:")
table_list_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

table_listbox = tk.Listbox(root)
table_listbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

get_table_list()

# Resize Controls
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)

# Status Bar
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.grid(row=4, column=0, columnspan=3, sticky="we")

# Set initial status
status_var.set("Ready")

root.mainloop()




import tkinter as tk
from tkinter import ttk
import sqlite3

# Create the main window
root = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(root)

# Connect to the SQLite database
conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM your_table")

# Fetch column names from the cursor description
column_names = [desc[0] for desc in cursor.description]

# Configure the Treeview columns based on the column names
tree["columns"] = column_names
for col in column_names:
    tree.heading(col, text=col)

# Fetch all rows from the query result
rows = cursor.fetchall()

# Iterate over the rows and insert them into the Treeview
for row in rows:
    tree.insert("", "end", values=row)

# Close the database connection
conn.close()

# Pack the Treeview widget
tree.pack()

# Start the main event loop
root.mainloop()











import tkinter as tk
from tkinter import ttk
import pandas as pd
import sqlite3
import tkinterdnd2 as tkdnd


class TableViewer:
    def __init__(self, root):
        self.root = root
        self.tree = None
        self.conn = None
        self.cursor = None
        self.column_names = []

    def create_table_viewer(self):
        # Create the Treeview widget
        self.tree = ttk.Treeview(self.root, show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Enable drag and drop functionality
        tkdnd.DragSource(self.tree, "text/uri-list")

        # Create a horizontal scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)
        scrollbar.grid(row=1, column=0, sticky="ew")
        self.tree.configure(xscrollcommand=scrollbar.set)

        # Bind the Treeview selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def connect_to_database(self, db_file):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        # Execute the query
        self.cursor.execute(query)

        # Fetch column names from the cursor description
        self.column_names = [desc[0] for desc in self.cursor.description]

        # Fetch all rows from the query result
        rows = self.cursor.fetchall()

        # Convert the rows to a Pandas DataFrame
        df = pd.DataFrame(rows, columns=self.column_names)

        # Clear the existing columns in the Treeview
        self.tree.delete(*self.tree.get_children())

        # Insert the column names as Treeview headings
        for col in self.column_names:
            self.tree.heading(col, text=col)

        # Insert the data rows into the Treeview
        for i, row in df.iterrows():
            self.tree.insert("", "end", values=row.tolist())

    def on_tree_select(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            selected_values = []
            for item in selected_items:
                values = self.tree.item(item, "values")
                selected_values.append(values)
            print(selected_values)  # Replace with your desired action


# Create the main window
root = tk.Tk()

# Configure the main window
root.title("SQLite Table Viewer")
root.geometry("800x600")

# Create an instance of TableViewer
table_viewer = TableViewer(root)
table_viewer.create_table_viewer()

# Connect to the SQLite database
table_viewer.connect_to_database("your_database.db")

# Execute a SELECT query
table_viewer.execute_query("SELECT * FROM your_table")

# Start the main event loop
root.mainloop()





import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

def create_treeview(root, data, headers=None):
    # Create Treeview widget
    tree = ttk.Treeview(root)
    tree.pack(fill="both", expand=True)

    # Add scrollbars to the Treeview
    tree_scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree_scrollbar_y.pack(side="right", fill="y")
    tree_scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    tree_scrollbar_x.pack(side="bottom", fill="x")
    tree.configure(yscrollcommand=tree_scrollbar_y.set, xscrollcommand=tree_scrollbar_x.set)

    # Insert headers if provided
    if headers:
        tree["columns"] = headers
        for header in headers:
            tree.heading(header, text=header)

    # Insert data rows into the Treeview
    for row in data:
        tree.insert("", "end", values=row)

    return tree

def copy_selected_data(event=None):
    selected_items = treeview.selection()
    if selected_items:
        selected_data = []
        if headers:
            if include_headers.get():
                selected_data.append(headers)
        for item in selected_items:
            values = treeview.item(item)["values"]
            if not values:
                continue
            selected_data.append(values)

        copied_text = ""
        if selected_data:
            copied_text = "\n".join(["\t".join(map(str, row)) for row in selected_data])

        root.clipboard_clear()
        root.clipboard_append(copied_text)

def select_all(event=None):
    treeview.selection_set(treeview.get_children())

def clear_selection(event=None):
    treeview.selection_remove(treeview.selection())

def show_context_menu(event):
    item = treeview.identify("item", event.x, event.y)
    if item:
        treeview.selection_set(item)

        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Copy with Headers", command=copy_selected_data)
        menu.add_command(label="Copy without Headers", command=lambda: copy_selected_data(include_headers=False))
        menu.tk_popup(event.x_root, event.y_root)

# Example usage
root = tk.Tk()
root.geometry("400x300")

data = [
    ("John Doe", 30, "john.doe@example.com"),
    ("Jane Smith", 25, "jane.smith@example.com"),
    ("Mike Johnson", 35, "mike.johnson@example.com")
]
headers = ["Name", "Age", "Email"]

treeview = create_treeview(root, data, headers)

# Enable multiple selection
treeview.configure(selectmode="extended")

# Bind Ctrl+A to select all items
root.bind("<Control-a>", select_all)

# Bind Ctrl+C to copy selected data
root.bind("<Control-c>", copy_selected_data)

# Bind Right-click to show context menu
treeview.bind("<Button-3>", show_context_menu)

include_headers = tk.BooleanVar()
include_headers.set(True)

# Checkbox to include headers when copying
checkbox = ttk.Checkbutton(root, text="Include Headers", variable=include_headers)
checkbox.pack()

root.mainloop()



import tkinter as tk
import subprocess

def execute_command():
    command = input_entry.get()
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    output_text.insert('end', output)

root = tk.Tk()

# Create a Text widget for output display
output_text = tk.Text(root)
output_text.pack(fill='both', expand=True)

# Create an Entry widget for command input
input_entry = tk.Entry(root)
input_entry.pack(fill='x')

# Create a button to execute the command
execute_button = tk.Button(root, text='Execute', command=execute_command)
execute_button.pack()

root.mainloop()



import tkinter as tk
import paramiko

def connect_ssh():
    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SSH server
        ssh.connect(host, username=username, password=password)
        output_text.insert('end', f"Connected to {host}\n")
        
        # Create an interactive shell
        shell = ssh.invoke_shell()
        shell.send("\n")

        def send_command(event):
            command = command_entry.get()
            shell.send(command + "\n")
            command_entry.delete(0, 'end')

        def receive_output():
            while shell.recv_ready():
                output = shell.recv(1024).decode('utf-8')
                output_text.insert('end', output)
                output_text.see('end')

            output_text.after(100, receive_output)

        # Bind the command sending function to the Enter key
        command_entry.bind("<Return>", send_command)

        # Start receiving output from the shell
        receive_output()

    except paramiko.AuthenticationException:
        output_text.insert('end', "Authentication failed\n")
    except paramiko.SSHException as e:
        output_text.insert('end', f"SSH error: {str(e)}\n")
    except paramiko.socket.error as e:
        output_text.insert('end', f"Socket error: {str(e)}\n")
    finally:
        # Close the SSH connection
        ssh.close()

root = tk.Tk()

# Hostname entry
host_label = tk.Label(root, text="Hostname:")
host_label.pack()
host_entry = tk.Entry(root)
host_entry.pack()

# Username entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

# Connect button
connect_button = tk.Button(root, text="Connect", command=connect_ssh)
connect_button.pack()

# Output text area
output_text = tk.Text(root)
output_text.pack(fill='both', expand=True)

# Command entry
command_entry = tk.Entry(root)
command_entry.pack()

root.mainloop()



import tkinter as tk
from tkinter import ttk
import threading
import time

threads = {}

def start_thread(tab, tab_name, label_var):
    stop_event = threading.Event()
    def run(stop_event):
        while not stop_event.is_set():
            current_time = time.strftime("%H:%M:%S")
            label_var.set(f"{tab_name}: Running... Time: {current_time}")
            time.sleep(2)
    thread = threading.Thread(target=run, args=(stop_event,))
    thread.start()
    threads[tab_name] = (thread, stop_event)

def stop_thread(tab_name, label_var):
    thread, stop_event = threads.get(tab_name, (None, None))
    if thread and stop_event:
        stop_event.set()
        thread.join()
        label_var.set(f"{tab_name}: Stopped.")

root = tk.Tk()
root.title("Multiple Threads Example")

tab_control = ttk.Notebook(root)

# Create tabs
tabs = ["Tab 1", "Tab 2", "Tab 3"]

for tab_name in tabs:
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=tab_name)

    label_var = tk.StringVar()
    label_var.set(f"{tab_name}: Not running")

    label = ttk.Label(tab, textvariable=label_var)
    label.pack(padx=20, pady=20)

    start_button = ttk.Button(tab, text="Start Thread", command=lambda tab=tab, name=tab_name, var=label_var: start_thread(tab, name, var))
    start_button.pack(padx=20, pady=5)

    stop_button = ttk.Button(tab, text="Stop Thread", command=lambda name=tab_name, var=label_var: stop_thread(name, var))
    stop_button.pack(padx=20, pady=5)

    threads[tab_name] = (None, None)  # Initialize thread and stop event

# Pack the tab control
tab_control.pack(expand=True, fill="both")

root.mainloop()



import tkinter as tk
from tkinter import ttk
global root
root = tk.Tk()
global controls
controls={}
global controlsframe
controlsframe={}

def add_scrollbar(widget, use_vertical=True, use_horizontal=True):
    if use_vertical:
        # Create a vertical scrollbar
        scrollbar_y = ttk.Scrollbar(widget, orient=tk.VERTICAL)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        widget.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_y.configure(command=widget.yview)

    if use_horizontal:
        # Create a horizontal scrollbar
        scrollbar_x = ttk.Scrollbar(widget, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        widget.configure(xscrollcommand=scrollbar_x.set)
        scrollbar_x.configure(command=widget.xview)

def mainGui(title,mainsize):
    root.title(title)
    root.geometry(mainsize)  # Set the default size of the window
    global notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)
    mstyle = ttk.Style()
    mstyle.configure("Custom.TNotebook.Tab", background="blue")
    
    #Add Frame
    tablist=['CSIA','Hive','Local','Settings','Admin']
    def add_frames(num,tablist):
        for n,name in enumerate(tablist):
            control=ttk.Frame(notebook,name=name.lower())
            notebook.add(control, text=name)
            notebook.tab(control)
            
            controls[name.lower()]=control
            
            framelist=['side','top','bottom']
            bgcolor=['blue','green','red']
            tabb=control#controls['hive']
            print(tabb)
            def add_frames_tab(framelist,tab,tabname):
                for n,(name,clr) in enumerate(zip(framelist,bgcolor)):
                    style = ttk.Style()
                    style.configure("Custom.TFrame", background=clr)
                    controlframe=tk.Text(tabb,name=tabname.lower()+name.lower(),borderwidth=3)
                    controlframe.grid(row=2, column=2, padx=5, pady=5, sticky="n")
                    
                    #controlframe2=tk.Listbox(tabb,name=tabname.lower()+name.lower(),borderwidth=3,height=30, width=40)
                    #controlframe2.grid(row=2, column=10, padx=5, pady=5, sticky="n")
                    
                    #root.grid_rowconfigure(0, weight=1)
                    #root.grid_columnconfigure(0, weight=1)
                    print(clr)
                    
                    controlsframe[tabname.lower()+name.lower()]=controlframe
                    print(controlframe)
    
            #add_frames_tab(framelist,tabb,name)
            
            def design_tab(tabb):
                frame1=tk.Frame(tabb,borderwidth=3,bg="red")
                frame2=tk.Frame(tabb,borderwidth=3,width=10,height=300)
                frame3=tk.Frame(tabb,borderwidth=3,height=30)
                frame4=tk.Frame(tabb,borderwidth=3)
                frame5=tk.Frame(tabb,borderwidth=3)
                #frame1.pack(side=tk.TOP,fill="both")
                frame3.pack(side=tk.BOTTOM,fill="x",expand=False)
                frame1.pack(side=tk.TOP,fill="x",expand=False)
                #frame3.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
                frame2.pack(side=tk.LEFT,fill=tk.BOTH,expand=False)
                #frame2.grid(row=0, column=1, sticky="nsew")
                
                frame5.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
                frame4.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
                
                
                
                labelf1=tk.Label(frame1,text="Controls")
                labelf2=tk.Label(frame2,text="TableList")
                labelf3=ttk.Label(frame3,text="Execution Logs")
                labelf4=tk.Label(frame4,text="Viewer")
                labelf5=tk.Label(frame5,text="Query Editor")
                
                labelf1.pack(side=tk.TOP,expand=False)
                labelf2.pack(side=tk.TOP,expand=False)
                #labelf3.pack(side=tk.TOP,expand=False)
                labelf4.pack(side=tk.TOP,expand=False)
                labelf5.pack(side=tk.TOP,expand=False)
                
                tablelist=tk.Listbox(frame2,width=30)
                
                tablelist.pack(side=tk.TOP,fill="both",expand=True)
                #add_scrollbar(frame2,True,True)
                tablelist.insert(tk.END, "Table List Below")
                
                querywin=tk.Text(frame5,borderwidth=3)
                add_scrollbar(querywin)
                querywin.pack(side=tk.BOTTOM,fill="both",expand=True)
                outputq=ttk.Treeview(frame4)
                add_scrollbar(outputq)
                outputq.pack(side=tk.TOP,fill="both",expand=True)
                logtxt=tk.Text(frame3,borderwidth=3,height=40)
                #logtxt=tk.Text(frame2,borderwidth=3,height=40)
                add_scrollbar(logtxt)
                
                logtxt.pack(side=tk.LEFT,fill="x",expand=True)
                buttonexe=tk.Button(frame1,text="Execute Query",borderwidth=3)
                buttonexe.pack(side=tk.LEFT)
                logtxt2=tk.Text(frame3,borderwidth=3,height=40)
                logtxt3=tk.Text(frame3,borderwidth=3,height=40)
                add_scrollbar(logtxt2)
                add_scrollbar(logtxt3)
                logtxt2.pack(side=tk.LEFT,fill="both",expand=True)
                logtxt3.pack(side=tk.LEFT,fill="both",expand=True)
                
                buttonexe2=tk.Button(frame1,text="Import Data",borderwidth=3)
                buttonexe2.pack(side=tk.LEFT)
                
                buttonexe3=tk.Button(frame1,text="Refresh Tables List",borderwidth=3)
                buttonexe3.pack(side=tk.LEFT)
                
                buttonexe4=tk.Button(frame1,text="Blank",borderwidth=3)
                buttonexe4.pack(side=tk.LEFT)
                
                buttonexe5=tk.Button(frame1,text="Blank",borderwidth=3)
                buttonexe5.pack(side=tk.LEFT)
            
            design_tab(control)
                


    
    data = ["Apple", "Banana", "Orange", "Grape", "Mango"]
    
    def frame_controls(slaveframe,data):
        
        # Create a listbox
        table=ttk.Treeview(tab1)
        table.pack(side=tk.BOTTOM)
        listbox = tk.Listbox(slaveframe)
        listbox.pack()

        # Insert data into the listbox
        for item in data:
            listbox.insert(tk.END, item)
    
    add_frames(4,tablist)   
    #add_frames_tab    
    #frame_controls(tab1,data)
    
    def test():
    
        print(controls['hive'])
        
   
    #test()    
    



mainGui("Kumar's","800x600")

root.mainloop()


from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Web Browser")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.showMaximized()

    def load_page(self, url):
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication([])
    window = BrowserWindow()
    window.load_page("https://www.google.com")
    app.exec_()




from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Web Browser")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.showMaximized()

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.url_entry = QLineEdit()
        self.go_button = QPushButton("Go")
        self.back_button = QPushButton("Back")

        toolbar.addWidget(self.url_entry)
        toolbar.addWidget(self.go_button)
        toolbar.addWidget(self.back_button)

        self.go_button.clicked.connect(self.go_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def go_button_clicked(self):
        url = self.url_entry.text()
        self.load_page(url)

    def back_button_clicked(self):
        self.browser.back()

    def load_page(self, url):
        request = QWebEngineHttpRequest(QUrl(url))
        self.browser.load(request)

if __name__ == "__main__":
    app = QApplication([])
    window = BrowserWindow()
    window.load_page("https://www.example.com")
    app.exec_()






<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>677</width>
    <height>410</height>
   </rect>
  </property>
  <widget class="QTabWidget" name="tabWidget">
   <property name="currentIndex">
    <number>0</number>
   </property>
   <widget class="QWidget" name="tab">
    <attribute name="title">
     <string/>
    </attribute>
    <widget class="QWebView" name="webView" native="true">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>10</y>
       <width>771</width>
       <height>541</height>
      </rect>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="tab_2">
    <attribute name="title">
     <string/>
    </attribute>
    <widget class="QWebView" name="webView_2" native="true">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>10</y>
       <width>771</width>
       <height>541</height>
      </rect>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="tab_3">
    <attribute name="title">
     <string/>
    </attribute>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>677</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QToolBar" name="toolBar">
   <property name="windowTitle">
    <string>toolBar</string>
   </property>
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <layoutdefault spacing="6" margin="11"/>
 <customwidgets>
  <customwidget>
   <class>QWebView</class>
   <extends>QWidget</extends>
   <header>qwebview.h</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
