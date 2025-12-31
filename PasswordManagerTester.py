from PasswordManager import PasswordManager

"""
This program tests the PasswordManager class with an interactive menu.
"""
class PasswordManagerTester:
    @staticmethod
    def main():
        manager = PasswordManager()

        while True:
            print("\nPassword Manager Menu")
            print("1. Add entry (with generated or custom password)")
            print("2. View all entries")
            print("3. Search entry")
            print("4. Exit")
            choice = input("Choose: ").strip()

            if choice == '1':
                site = input("Site/App: ").strip()
                username = input("Username: ").strip()
                custom = input("Generate password? (y/n): ").lower().strip()
                password = None if custom == 'y' else input("Password: ").strip()
                manager.add_entry(site, username, password)
            elif choice == '2':
                manager.view_entries()
            elif choice == '3':
                term = input("Search term (site or username): ").strip()
                manager.search(term)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    PasswordManagerTester.main()
