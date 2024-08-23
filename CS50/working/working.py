import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
        pattern = r"^((?:[1-9]|1[0-2])(?::[0-5][0-9])?\s[AP]M)\s+to\s+((?:[1-9]|1[0-2])(?::[0-5][0-9])?\s[AP]M)$"
        #pattern = r"^((?:[1-9]|1[0-2])(?::[0-5][0-9])?\s[A]M)\s+to\s+((?:[1-9]|1[0-2])(?::[0-5][0-9])?\s[AP]M)$"
        match = re.match(pattern, s)

        if not match:
            raise ValueError("Invalid time format")
        start_time, end_time = match.groups()
        start_24h =hour_24_format(start_time)
        end_24h = hour_24_format(end_time)
        return f"{start_24h} to {end_24h}"


def hour_24_format(time):
    period = "AM" if "AM" in time else "PM"
    time = time.replace("AM", "").replace("PM", "").strip()
    if ':' in time:
            hour, minutes = time.split(":")
    else:
            hour, minutes =time, "00"
    hour = int(hour)
    if period == "PM" and hour != 12:
            hour += 12
    elif period == "AM" and hour == 12:
            hour = 0

    return f"{hour:02}:{minutes}"

if __name__ == "__main__":
    main()
