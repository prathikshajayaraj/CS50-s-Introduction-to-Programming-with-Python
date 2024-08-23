import sys
import csv
from tabulate import tabulate
def main():
    filename = file()
    read_table(filename)


def file() :
    if len(sys.argv)!=2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if file_name.endswith(".csv"):
            return file_name
        else:
            sys.exit("Not a CSV file")

def read_table(filename):
    pizzas =[]
    try:
       with open(filename) as csvfile:
           reader = csv.reader(csvfile)
           for row in reader:
            pizzas.append(row)
       print(tabulate(pizzas, tablefmt="grid",headers="firstrow"))


    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main() 
