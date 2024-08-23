import re
import sys


def main():
    result =parse(input("HTML: "))
    if result:
        print(result)


def parse(s):
    match = re.search(r'<iframe[^>]*\bsrc="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"', s)
    if match:
        #full_url = match.group(1)
        video_id = match.group(2)


        short_url = f"https://youtu.be/{video_id}"
        return short_url
    return None



if __name__ == "__main__":
    main()
