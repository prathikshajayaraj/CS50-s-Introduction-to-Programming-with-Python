import sys
def main():
    filename = file()
    read_file(filename)

def file() :
    if len(sys.argv)!=2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if file_name.endswith(".py"):
            return file_name
        else:
            sys.exit("Not a Python file")

def read_file(filename):
   no_lines = 0
   try:
        with open(filename) as file:
            lines = file.readlines()

        for line in lines:
            line =line.strip()
            if not line or line.startswith("#"):
                continue
            no_lines = no_lines + 1
        print(no_lines)

   except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main() 
