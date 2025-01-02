import pandas as pd

# Process Stock Data (local file)
def process_stock_data(data):
    #data = data.rename(columns={'Close': 'Price'})  # Rename 'Close' to 'Price'
    data['Price'] = data['Close']  # Duplicate 'Close' column as 'Price'
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Convert Date to datetime
    data = data.dropna(subset=['Date'])  # Drop rows with invalid dates
    data['Price'] = data['Price'].replace({',': ''}, regex=True).astype(float)  # Remove commas and convert to float
    return data

# Process Global Development Data (local file)
def process_global_development_data(data):
    # Print column names
    #Column names: ['Code', 'Region', 'Year', 'Series', 'Value', 'Footnotes', 'Source']
    #print("Column names:", data.columns.tolist())
    
    # Assume we want columns 'Country', 'Year', 'GDP'
    columns_to_keep = ['Region', 'Year', 'Value']
    data = data[columns_to_keep]
    
    # Filter out rows where the 'Year' column contains "Total" or "All"
    data = data[~data['Region'].str.contains('Total|All', case=False, na=False)]
    
    # Convert 'Year' to integer if it contains only numeric values
    try:
        data['Year'] = data['Year'].astype(int)
        data['Value'] = data['Value'].replace({',': ''}, regex=True).astype(float)  # Remove commas and convert to float

    except ValueError:
        print("Warning: Some non-numeric values remain in 'Year'.")
    
    return data

# Process NASA API Data
def process_nasa_data(data):
    # Extract key fields for simplicity
    data = data[['date', 'title','explanation','url']]
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    print(data)
    return data

# Process Alpha Vantage Data (API)
def process_alpha_vantage_data(data):
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])
    data[['Open', 'High', 'Low', 'Close', 'Volume']] = data[['Open', 'High', 'Low', 'Close', 'Volume']].astype(float)
    return data
