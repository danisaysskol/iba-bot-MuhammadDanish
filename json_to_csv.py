import json
import csv

# Read JSON file
with open('json_dataset/courses_info.json', 'r') as json_file:
    data = json.load(json_file)

# Open CSV file for writing
with open('csv_dataset/courses_info.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(data[0].keys())

    # Write data rows
    for item in data:
        csv_writer.writerow(item.values())

print("JSON converted to CSV and saved as 'data.csv'")
