import pandas as pd
import re

# Sample DataFrame
data = {
    'Column1': ['   hello ', '\tworld   ', '   pandas  \n', '  data '],
    'Column2': ['  foo  ', ' bar ', '  \tbaz  ', '\n qux   ']
}

df = pd.DataFrame(data)

# Function to remove all types of leading, trailing, and extra whitespace characters
def clean_whitespace(x):
    if isinstance(x, str):  # Check if the value is a string
        return re.sub(r'\s+', ' ', x).strip()
    return x  # If not a string, return the value as is

# Apply the function to the entire DataFrame
df_cleaned = df.applymap(clean_whitespace)

print("Original DataFrame:")
print(df)
print("\nCleaned DataFrame:")
print(df_cleaned)
