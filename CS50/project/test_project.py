import pytest
import os
import csv
from project import FlashCard, FlashCardUser

# Test case 1: Testing the add_input function
def test_add_input():
    flashcard = FlashCard()
    question = "What is the capital of France?"
    answer = "Paris"

    if os.path.exists("flashcard.csv"):
        os.remove("flashcard.csv")

    # Call the add_input method
    flashcard.add_input(question, answer)

    with open("flashcard.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["question"] == question
        assert rows[0]["answer"] == answer

    os.remove("flashcard.csv")

# Test case 2: Testing the user_detail function
def test_user_detail():
    username = "testuser"

    if os.path.exists("userdetail.csv"):
        os.remove("userdetail.csv")

    # Create a new user
    user = FlashCardUser(username)
    user.user_detail()

    with open("userdetail.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["name"] == username
        assert rows[0]["score"] == "0"

    os.remove("userdetail.csv")

# Test case 3: Testing the user_update_score function
def test_user_update_score():
    username = "testuser"
    initial_score = 2
    updated_score = 5

    if os.path.exists("userdetail.csv"):
        os.remove("userdetail.csv")

    # Create initial user data
    with open("userdetail.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerow({"name": username, "score": initial_score})

    # Update the score
    user = FlashCardUser(username)
    user.user_update_score(username, updated_score)

    # Verify the updated content of the CSV file
    with open("userdetail.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["name"] == username
        assert rows[0]["score"] == str(updated_score)

    os.remove("userdetail.csv")




if __name__ == "__main__":
    pytest.main()
