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






