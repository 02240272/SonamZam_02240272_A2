import random
import math
import SonamZam_02240272_A2_PB as PC  

# Number Guessing Adventure
class NumberGuessGame:
    def __init__(self):
        self.target_value = random.randint(1, 100)
        self.attempt_count = 0
        self.score = 0

    def start(self):
        print("\nWelcome to the Number Guessing Adventure!")
        while True:
            try:
                user_input = int(input("Guess a number between 1 and 100: "))
                self.attempt_count += 1

                if user_input < self.target_value:
                    print("Too low! Try again.")
                elif user_input > self.target_value:
                    print("Too high! Try again.")
                else:
                    self.score = max(0, 10 - self.attempt_count)
                    print(f"Congratulations! You guessed it right. The number was {self.target_value}.")
                    print(f"Your final score: {self.score}")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Rock, Paper, Scissors Arena
class RockPaperScissorsGame:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.player_wins = 0
        self.cpu_wins = 0

    def start(self):
        print("\nWelcome to Rock Paper Scissors Arena!")
        while True:
            user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
            if user_choice == 'exit':
                print("Returning to the main menu...")
                break

            if user_choice not in self.options:
                print("Invalid selection. Try again!")
                continue

            computer_choice = random.choice(self.options)
            print(f"Computer chose {computer_choice}.")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                self.player_wins += 1
                print("You won this round!")
            else:
                self.cpu_wins += 1
                print("Computer won this round!")

            print(f"Your Wins: {self.player_wins}, Computer Wins: {self.cpu_wins}")

# Trivia Quest
class TriviaGame:
    def __init__(self):
        self.categories = {
            "Science": [
                {"question": "What is the chemical symbol for water?", "choices": ["H2O", "CO2", "O2", "H2"], "answer": "H2O"},
                {"question": "Which planet is known as the Red Planet?", "choices": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
            ],
            "History": [
                {"question": "Who was the first U.S. president?", "choices": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "answer": "George Washington"},
                {"question": "In which year did WWII end?", "choices": ["1945", "1939", "1918", "1965"], "answer": "1945"},
            ],
            "Geography": [
                {"question": "What is the capital of France?", "choices": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
                {"question": "Where is the Sahara Desert located?", "choices": ["Africa", "Asia", "Australia", "North America"], "answer": "Africa"},
            ]
        }
        self.score = 0

    def start(self):
        print("\nWelcome to Trivia Quest!")

        while True:
            print("\nChoose a category or type 'exit' to quit:")
            categories_list = list(self.categories.keys())
            for index, category in enumerate(categories_list, 1):
                print(f"{index}. {category}")

            user_input = input("Enter the category number or 'exit': ").lower()

            if user_input == "exit":
                print(f"Thanks for playing! Your total score: {self.score}")
                break

            try:
                selected_category = int(user_input)
                if 1 <= selected_category <= len(categories_list):
                    chosen_category = categories_list[selected_category - 1]
                    self.ask_questions(chosen_category)
                else:
                    print("Invalid selection! Please choose a valid category.")
            except ValueError:
                print("Invalid input! Please enter a number or 'exit'.")

    def ask_questions(self, category):
        questions_set = self.categories[category]
        random.shuffle(questions_set)

        for question in questions_set:
            print(f"\nQuestion: {question['question']}")
            for i, choice in enumerate(question['choices'], 1):
                print(f"{i}. {choice}")

            try:
                user_answer = int(input("Select your answer (1-4): "))
                if question['choices'][user_answer - 1] == question['answer']:
                    self.score += 1
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is \"{question['answer']}\".")
            except (ValueError, IndexError):
                print("Invalid response! Moving to the next question.")

        print(f"\nTrivia completed! Your current score: {self.score}")

# Pokemon Binder Manager

class PokemonBinderManager:
    def __init__(self):
        self.card_storage = {}

    def start(self):
        self.run_binder_manager()

    def run_binder_manager(self):
        while True:
            print("\nWelcome to Pokemon Card Binder Manager!")
            print("Main Menu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            try:
                user_choice = int(input("Select option (1-4): "))
                if user_choice == 1:
                    self.add_pokemon_card()
                elif user_choice == 2:
                    self.reset_binder_data()
                elif user_choice == 3:
                    self.view_binder_status()
                elif user_choice == 4:
                    print("Thank you for using Pokemon Card Binder Manager!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def add_pokemon_card(self):
        try:
            pokedex_number = int(input("Enter Pokedex number (1-1025): "))
            if pokedex_number < 1 or pokedex_number > 1025:
                print("Invalid number! Must be between 1 and 1025.")
                return

            if pokedex_number in self.card_storage:
                print(f"Status: Pokedex #{pokedex_number} already exists.")
                return

            position = len(self.card_storage) + 1
            page = math.ceil(position / 64)
            row = ((position - 1) % 8) + 1
            col = ((position - 1) % 64) // 8 + 1

            self.card_storage[pokedex_number] = (page, row, col)
            print(f"Page: {page}, Position: Row {row}, Column {col}")
            print(f"Status: Added Pokedex #{pokedex_number} to binder.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def reset_binder_data(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        confirmation = input("Type 'CONFIRM' to reset or 'EXIT' to return: ").strip().lower()
        if confirmation == "confirm":
            self.card_storage.clear()
            print("The binder reset was successful! All cards have been removed.")
        else:
            print("Reset canceled.")

    def view_binder_status(self):
        print("\nCurrent Binder Contents:")
        if not self.card_storage:
            print("The binder is empty.")
        else:
            for pokedex_number, (page, row, col) in sorted(self.card_storage.items()):
                print(f"Pokedex #{pokedex_number}: Page {page}, Position: Row {row}, Column {col}")

        completion_percentage = (len(self.card_storage) / 1025) * 100
        print(f"Total cards in binder: {len(self.card_storage)}")
        print(f"Completion: {completion_percentage:.2f}%")

# Main Game Menu
class GameMenu:
    def __init__(self):
        self.games = {
            "1": ("Number Guessing Adventure", NumberGuessGame),
            "2": ("Rock Paper Scissors Arena", RockPaperScissorsGame),
            "3": ("Trivia Quest", TriviaGame),
            "4": ("Pokemon Card Binder Manager", PokemonBinderManager)
        }

    def start(self):
        while True:
            print("\n======= Game Menu =======")
            for key, (name, _) in self.games.items():
                print(f"{key}. {name}")
            print("5. Check Current Overall Score")
            print("0. Exit program")

            choice = input("Select a function (0-5): ").strip()
            if choice == "0":
                print("Goodbye! Thanks for playing.")
                break
            elif choice == "5":
                self.check_overall_score()
            elif choice in self.games:
                game_name, game_class = self.games[choice]
                print(f"\nStarting {game_name}...")
                game_instance = game_class()
                game_instance.start()
            else:
                print("Invalid choice. Please try again.")

    def check_overall_score(self):
        print("Overall Score: 100")  

if __name__ == "__main__":
    menu = GameMenu()
    menu.start()
