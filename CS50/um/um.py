import re

def main():
    print(count(input("Text: ")))

def count(s):
    if matches := re.findall(r"\bum\b",s,re.IGNORECASE):
        return(len(matches))



if __name__ == "__main__":
    main()
