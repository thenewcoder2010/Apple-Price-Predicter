import csv

# File paths
input_csv = "data-final.csv"
output_csv = "data-final-final.csv"

# Read the input CSV, remove dollar signs, and write to the output CSV
with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # Remove dollar signs from each cell
        cleaned_row = [cell.replace('$', '') for cell in row]
        writer.writerow(cleaned_row)

print(f"Processed CSV saved as {output_csv}")

