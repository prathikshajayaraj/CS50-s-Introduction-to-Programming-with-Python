import csv
import sys

def main():
    file1, file2 = get_filenames()
    data_list = read_file(file1)
    write_file(data_list, file2)

def get_filenames():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    file_1 = sys.argv[1]
    file_2 = sys.argv[2]

    if not file_1.endswith(".csv") or not file_2.endswith(".csv"):
        sys.exit("Both files must be CSV files")

    return file_1, file_2

def read_file(file1):
    data_list = []
    try:
        with open(file1, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_list.append({"name": row["name"], "house": row["house"]})
        return data_list
    except FileNotFoundError:
        sys.exit(f"Could not read file: {file1}")

def write_file(data_list, file2):
    with open(file2, mode='w', newline='') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  

        for item in data_list:
            try:
                lastname, firstname = item["name"].split(",", 1)
                writer.writerow({'first': firstname.strip(), 'last': lastname.strip(), 'house': item['house']})
            except ValueError:
                sys.exit(f"Error processing name: {item['name']}")

if __name__ == "__main__":
    main()

