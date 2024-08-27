import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6],
    'Column3': [7, 8, 9]
}

df = pd.DataFrame(data)

# Initialize an empty string to store the result
result = ''

# Loop through the range of the number of columns in the DataFrame
for i in range(len(df.columns)):
    # Append the current index to the result string
    result += str(i)
    # Add a comma if it's not the last element
    if i < len(df.columns) - 1:
        result += ','

print(result)
