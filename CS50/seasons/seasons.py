from datetime import date, datetime
import inflect
import sys

class Minutes:
    def __init__(self, user):
        self.user = user
        self.today = date.today()
        self.dateconversion = datetime.strptime(self.user, '%Y-%m-%d').date()
        self.calculate_difference()

    def __str__(self):
        return f"{self.words} minutes"

    def calculate_difference(self):
        delta = self.today - self.dateconversion
        self.minutes = delta.days * 24 * 60
        self.word_minutes(self.minutes)

    def word_minutes(self, number):
        p = inflect.engine()
        self.words = p.number_to_words(number, andword="")
        self.words = self.words[0].upper() + self.words[1:]
        return self.words

def main():
    user = input("Date of Birth (YYYY-MM-DD): ").strip()
    try:
        minutes_word = Minutes(user)
        print(minutes_word)
    except ValueError:
        sys.exit("Invalid date. Please enter the date in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
