import pandas as pd

# Load the uploaded CSV file to analyze its structure and data
file_path = 'dataset/educational_attainment_personal_income_2008-2014.csv'
data = pd.read_csv(file_path)

# Display the first few rows and the column info for analysis
# data_info = data.info()
# data_preview = data.head()

#data_info, data_preview

# Clean the data for SQL compatibility

# Simplify Year to extract only the year value
data['Year'] = pd.to_datetime(data['Year'], errors='coerce').dt.year

# Clean Personal Income to remove dollar signs and ranges for easier analysis
data['Personal Income'] = data['Personal Income'].str.replace(r'[^0-9-]', '', regex=True).replace('', None)

# Rename columns for SQL schema consistency
data.columns = ['year', 'age_group', 'gender', 'education_level', 'income_bracket', 'population_count']

# Display cleaned data info and preview for verification
# cleaned_data_info = data.info()
# cleaned_data_preview = data.head()

#cleaned_data_info, cleaned_data_preview
data.to_csv('dataset/cleaned/educational_attainment_personal_income_2008-2014.csv', index=False) 