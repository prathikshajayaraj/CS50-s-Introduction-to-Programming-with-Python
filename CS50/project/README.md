# Interactive Flashcard Learning System

## Video Demo: [Click here](https://youtu.be/3ojPlsfrceQ?si=0IehpSCvUTbH6EXf)

## Description:

This project is an Interactive Flashcard Learning System implemented in Python. It allows users to create, manage, and study flashcards while tracking their progress over time.

### Project Details:
* **Your Name:** Prathiksha S
* **GitHub Username:** prathikshajayaraj
* **edX Username:** prathikshas315

### Features:
1. **User Management:** The system allows multiple users to create accounts and tracks their individual progress.
2. **Flashcard Creation:** Users can add new flashcards with questions and answers.
3. **Study Mode:** The system presents random flashcards to users and checks their answers.
4. **Score Tracking:** Each user's score is updated based on their performance in study sessions.
5. **Persistent Storage:** Flashcards and user data are stored in CSV files for persistence between sessions.

### Files in the Project:
1. **project.py:** The main Python script containing all the code for the flashcard system.
   - `FlashCard` class: Handles flashcard operations (adding, displaying).
   - `FlashCardUser` class: Manages user interactions and score tracking.
   - `main()` function: Entry point of the program.

2. **flashcard.csv:** Stores all flashcards (questions and answers).

3. **userdetail.csv:** Keeps track of user information and scores.

4. **test_project.py:** Will contain pytest functions to test the main functionality.

### How It Works:
1. Users start by entering their username or creating a new account.
2. They can then choose to:
   - Add new flashcards to the system
   - Study existing flashcards
   - Exit the program
3. When studying, users are presented with random questions and have three chances to answer correctly.
4. Scores are updated based on correct answers and stored for each user.

### Design Choices:
1. **CSV for Data Storage:** Chose CSV files for simplicity and ease of human readability. For a larger-scale application, a database might be more appropriate.
2. **Class-Based Structure:** Used classes to encapsulate related functionality, making the code more organized and easier to extend.
3. **Random Question Selection:** Enhances learning by presenting questions in an unpredictable order.
4. **Multiple Chances:** Gives users opportunities to recall information, reinforcing learning.

### Possible Future Enhancements:
1. Implement categories for flashcards.
2. Add a graphical user interface.
3. Incorporate spaced repetition algorithms for more effective learning.
4. Implement data encryption for user information.

This project demonstrates proficiency in Python programming, including file I/O, data structures, object-oriented programming, and basic user interface design in a command-line environment.
