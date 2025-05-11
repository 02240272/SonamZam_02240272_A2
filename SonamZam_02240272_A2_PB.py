import math

class PokemonCardBinder:
    def __init__(self):
        self.binder = {}  # Stores Pokedex number -> (page, row, col)
        self.total_pages = math.ceil(1025 / 64)  # Maximum required pages
        self.max_pokedex_number = 1025

    def show_menu(self):
        print("\nWelcome to Pokemon Card Binder Manager!")
        print("Main Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")

    def add_card(self):
        try:
            pokedex_number = int(input("Enter Pokedex number (1-1025): "))
            if pokedex_number < 1 or pokedex_number > self.max_pokedex_number:
                print("Invalid Pokedex number! Please enter a number between 1 and 1025.")
                return

            if pokedex_number in self.binder:
                page, row, col = self.binder[pokedex_number]
                print(f"Status: Pokedex #{pokedex_number} already exists.")
                print(f"Page: {page}, Position: Row {row}, Column {col}")
                return

            # Determine card placement (8x8 grid logic)
            position = len(self.binder) + 1
            page = math.ceil(position / 64)
            row = ((position - 1) % 64) // 8 + 1
            col = ((position - 1) % 8) + 1

            # Store card details
            self.binder[pokedex_number] = (page, row, col)
            print(f"Page: {page}, Position: Row {row}, Column {col}")
            print(f"Status: Added Pokedex #{pokedex_number} to binder.")

            # Completion check
            if len(self.binder) == self.max_pokedex_number:
                print("Congratulations! You have caught them all!!")
        except ValueError:
            print("Invalid input! Please enter a valid Pokedex number.")

    def reset_binder(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        confirmation = input("Type 'CONFIRM' to reset or 'EXIT' to return: ").strip().upper()

        if confirmation == "CONFIRM":
            self.binder.clear()
            print("The binder reset was successful! All cards have been removed.")
        elif confirmation == "EXIT":
            print("Returning to the main menu...")
        else:
            print("Invalid input! Please type 'CONFIRM' or 'EXIT'.")

    def view_placements(self):
        if not self.binder:
            print("The binder is empty.")
        else:
            print("\nCurrent Binder Contents:")
            for pokedex_number, (page, row, col) in sorted(self.binder.items()):
                print(f"Pokedex #{pokedex_number}: Page {page}, Position: Row {row}, Column {col}")
        
        total_cards = len(self.binder)
        completion_percentage = (total_cards / self.max_pokedex_number) * 100
        print(f"Total cards in binder: {total_cards}")
        print(f"Completion: {completion_percentage:.2f}%")

    def start(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Select option (1-4): "))
                if choice == 1:
                    self.add_card()
                elif choice == 2:
                    self.reset_binder()
                elif choice == 3:
                    self.view_placements()
                elif choice == 4:
                    print("Thank you for using Pokemon Card Binder Manager!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1-4.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    binder_manager = PokemonCardBinder()
    binder_manager.start()
