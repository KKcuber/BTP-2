import pandas as pd

# Read the CSV file
df = pd.read_csv('./data/Bhadra Haralahalli.csv')

# Convert 'mm-dd-yyyy' format to 'dd/mm/yyyy'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert existing dates
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

# Save the cleaned DataFrame back to a CSV file if needed
df.to_csv('./data/cleaned_data.csv', index=False)
