# Password-Manager-Python
A simple object-oriented console program for managing passwords.

### What it does
- Add entries with site, username, and password (custom or auto-generated)
- View all entries
- Search by site or username
- Saves/loads to JSON file automatically
- Basic validation for required fields

### How to run
1. Make sure you have Python installed
2. Run the tester program:
3. python PasswordManagerTester.py
### Example usage
Password Manager Menu
1. Add entry
2. View all entries
3. Search entry
4. Exit
Choose: 1
Site/App: Gmail
Username: alex@example.com
Generate password? (y/n): y
Generated password: aB3!cD4eF5gH6iJ7
Added: Gmail | Username: alex@example.com | Password: aB3!cD4eF5gH6iJ7

### Files
- **PasswordEntry.py**  
Represents a single password entry with site, username, password, and __str__ for printing.

- **PasswordManager.py**  
Manages the list of entries with add, view, search, generation, and JSON save/load.

- **PasswordManagerTester.py**  
Interactive console menu program to test the PasswordManager.

Learning project in Python – December 2025
