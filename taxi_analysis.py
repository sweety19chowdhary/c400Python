import requests
import csv

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
response = requests.get(url)

csv_file_path = 'taxi_zone_lookup.csv'
with open(csv_file_path, 'wb') as f:
    f.write(response.content)

total_records = 0
unique_boroughs = set()
brooklyn_records = 0

with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        total_records += 1
        borough = row['borough']
        unique_boroughs.add(borough)
        
        if borough == 'Brooklyn':
            brooklyn_records += 1

sorted_boroughs = sorted(unique_boroughs)

output_file_path = '/root/taxi_zone_output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(f'Total Number of Records: {total_records}\n')
    output_file.write(f'Unique Boroughs: {", ".join(sorted_boroughs)}\n')
    output_file.write(f'Number of Records for Brooklyn Borough: {brooklyn_records}\n')

print(f"Facts saved to {output_file_path}")
