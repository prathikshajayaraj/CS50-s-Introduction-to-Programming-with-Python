import csv
import random
import os
import sys

class FlashCard:
    def __init__(self, question_text="", answer_text=""):
        self.question_text = question_text
        self.answer_text = answer_text

    def flashcard_choice(self):
        while True:
            operation = input(
                "1. Enter a new flashcard:\n"
                "2. Display a question:\n"
                "3. Exit\n"
                "Choose an option: "
            )
            match operation:
                case '1':
                    self.question = input("Enter your question: ")
                    self.answer = input("Enter your answer: ")
                    self.add_input(self.question, self.answer)
                case '2':
                    flashcarduser = FlashCardUser()
                    name, score = flashcarduser.user_current_score()
                    name, new_score = self.display_questions(name, int(score))
                    flashcarduser.user_update_score(name, new_score)
                case '3':
                    print("Exiting the program. Goodbye!")
                    sys.exit()
                case _:
                    print("Invalid choice. Please try again.")

    def add_input(self, question, answer):
        file_exists = os.path.isfile("flashcard.csv")
        with open("flashcard.csv", "a", newline="") as flashcard_file:
            fieldnames = ["question", "answer"]
            csv_writer = csv.DictWriter(flashcard_file, fieldnames=fieldnames)
            if not file_exists:
                csv_writer.writeheader()
            csv_writer.writerow({"question": question, "answer": answer})
        print("Flashcard added successfully!")

    def display_questions(self, name, score):
        chance = 3
        try:
            with open("flashcard.csv") as flashcard_file:
                reader = csv.DictReader(flashcard_file)
                rows = list(reader)
                questions = [row["question"] for row in rows]
            if not questions:
                print("No flashcards available. Please add some flashcards first.")
                return name, score

            self.question = random.choice(questions)

            while chance > 0:
                self.user_output = input(f"{self.question}: ")
                for row in rows:
                    if self.question == row["question"]:
                        if self.user_output.lower() == row["answer"].lower():
                            score += 1
                            print(f"Correct! Good job!\n{self.question}: {self.user_output}\nYour score: {score}")
                            return name, score
                        else:
                            print(f"Wrong answer :( ")
                            chance -= 1
                            if chance > 0:
                                print(f"You have {chance} {'chances' if chance > 1 else 'chance'} left.")
                            break
            print(f"Out of chances. Your final score: {score}")
            return name, score

        except FileNotFoundError:
            print("Flashcard file does not exist. Please add some flashcards first.")
            return name, score

class FlashCardUser:
    def __init__(self, username="", score=0):
        self.username = username
        self.score = score

    def user_detail(self):
        file_exists = os.path.isfile("userdetail.csv")
        user_exists = False
        if file_exists:
            with open("userdetail.csv", "r", newline="") as user_file:
                csv_reader = csv.DictReader(user_file)
                for row in csv_reader:
                    if row["name"] == self.username:
                        user_exists = True
                        self.score = int(row["score"])
                        break

        if not user_exists:
            with open("userdetail.csv", "a", newline="") as user_file:
                fieldnames = ["name", "score"]
                csv_writer = csv.DictWriter(user_file, fieldnames=fieldnames)
                if not file_exists:
                    csv_writer.writeheader()
                csv_writer.writerow({"name": self.username, "score": self.score})
            print(f"New user '{self.username}' created with initial score of 0.")
        else:
            print(f"Welcome back, {self.username}! Your current score is {self.score}.")

    def call_flashcard(self):
         flashcard = FlashCard()
         flashcard.flashcard_choice()

    def user_current_score(self):
        chance = 3
        try:
            with open("userdetail.csv") as user_file:
                csv_reader = csv.DictReader(user_file)
                rows = list(csv_reader)
                while chance > 0:
                    self.username = input("What is your username? ").strip()
                    for row in rows:
                        if self.username == row["name"]:
                            self.score = int(row["score"])
                            print(f"Welcome, {self.username}! Your current score is {self.score}.")
                            return self.username, self.score
                    else:
                        print("Username not found.")
                        chance -= 1
                        if chance > 0:
                            print(f"You have {chance} {'attempts' if chance > 1 else 'attempt'} left.")
                print("You have exhausted your attempts to enter a username.")
                print("Would you like to create a new user?")
                if input("Enter 'yes' to create a new user, or any other key to exit: ").lower() == 'yes':
                    return self.get_new_user()
                else:
                    sys.exit("Exiting the program. Goodbye!")

        except FileNotFoundError:
            print("User file does not exist. Creating a new user file.")
            return self.get_new_user()

    def user_update_score(self, name, score):
        try:
            with open("userdetail.csv", "r") as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            user_found = False
            for row in rows:
                if row["name"] == name:
                    row["score"] = str(score)
                    user_found = True
                    break

            if user_found:
                with open('userdetail.csv', mode='w', newline='') as file:
                    fieldnames = ["name", "score"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                print(f"Score updated for {name}. New score: {score}")
            else:
                print(f"User {name} not found. Score not updated.")

        except FileNotFoundError:
            print("User file does not exist. Unable to update score.")

    @classmethod
    def get(cls):
        username = input("Enter your username: ").strip()
        user = cls(username)
        user.user_detail()
        return user

    @classmethod
    def get_new_user(cls):
        while True:
            username = input("Enter a new username (3-20 characters, alphanumeric only): ").strip()
            if username.isalnum() and 3 <= len(username) <= 20:
                user = cls(username, 0)
                user.user_detail()
                return username, 0
            else:
                print("Invalid username. Please try again.")

def main():
    print("Welcome to the Flashcard Program!")
    user = FlashCardUser.get()
    user.call_flashcard()

if __name__ == "__main__":
    main()
