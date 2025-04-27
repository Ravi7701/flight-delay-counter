import csv
from collections import defaultdict

# Initialize a dictionary to store delay counts per airport
delay_counts = defaultdict(int)

# Open and read the CSV file
with open('flights_sample.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Skip the header
    next(reader)
    
    # Process each row
    for row in reader:
        try:
            airport = row[4]        # Destination Airport
            delay = int(row[8])     # Arrival Delay
            
            if delay > 0:           # Only delayed flights
                delay_counts[airport] += 1
        except (IndexError, ValueError):
            # Skip bad rows
            continue

# Print the delay counts per airport
for airport, count in delay_counts.items():
    print(f'Airport: {airport}, Delayed Flights: {count}')
