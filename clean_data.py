import csv
from datetime import datetime

# Function to calculate days from 12/26/2019
def calculate_days_from_reference(date_str):
    reference_date = datetime(2019, 12, 26)
    current_date = datetime.strptime(date_str, "%m/%d/%Y")
    return (current_date - reference_date).days

# File paths
input_csv = "data.csv"
output_csv = "data-final.csv"

# Read and process the CSV
with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Process each row
    for row in reader:
        updated_row = []
        for cell in row:
            try:
                # Try to parse the cell as a date
                days_from_ref = calculate_days_from_reference(cell)
                updated_row.append(days_from_ref)
            except ValueError:
                # If not a date, keep the original value
                updated_row.append(cell)
        writer.writerow(updated_row)

print(f"Processed CSV saved as {output_csv}")

