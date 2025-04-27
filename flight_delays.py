import csv
from collections import defaultdict

def read_csv_file(filename):
    """
    Reads a CSV file and returns a list of rows.
    Each row is a list of values.
    """
    data = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return data

def compute_delays(data):
    """
    Computes the number of delayed flights per destination airport.
    Returns a dictionary with airport codes as keys and delay counts as values.
    """
    delay_counts = defaultdict(int)
    for row in data:
        try:
            destination_airport = row[4]    # Destination Airport
            arrival_delay = int(row[8])     # Arrival Delay

            if arrival_delay > 0:           # Consider only positive delays
                delay_counts[destination_airport] += 1
        except (IndexError, ValueError):
            # Skip bad or incomplete rows
            continue
    return delay_counts

def save_results_to_csv(results, output_filename):
    """
    Saves the computed delay counts into a new CSV file.
    """
    try:
        with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Airport", "Delayed Flights"])
            for airport, count in results.items():
                writer.writerow([airport, count])
        print(f"Results have been saved successfully to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function to execute the flight delay analysis.
    """
    input_filename = 'flights_sample.csv'   # Input CSV file
    output_filename = 'delayed_flights_summary.csv'  # Output CSV file

    print("Reading flight data...")
    flight_data = read_csv_file(input_filename)

    if not flight_data:
        print("No data to process. Exiting...")
        return

    print("Computing delayed flights per airport...")
    delay_summary = compute_delays(flight_data)

    print("\nDelayed Flights Per Airport:")
    for airport, count in delay_summary.items():
        print(f"Airport: {airport}, Delayed Flights: {count}")

    print("\nSaving results to CSV...")
    save_results_to_csv(delay_summary, output_filename)

if __name__ == "__main__":
    main()

