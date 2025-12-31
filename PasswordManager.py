import secrets
import string
import json
import os

"""
A class that manages a collection of password entries with generation and JSON persistence.
"""
class PasswordManager:
    """
    Constructs a password manager, loading from file if it exists.
    @param filename the JSON file to save/load from
    """
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.entries = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [PasswordEntry(**e) for e in data]
        return []

    def save(self):
        with open(self.filename, 'w') as f:
            data = [{"site": e.site, "username": e.username, "password": e.password} for e in self.entries]
            json.dump(data, f, indent=2)
        print("Passwords saved.")

    def generate_password(self, length=16):
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def add_entry(self, site, username, password=None):
        if site and username:
            if password is None:
                password = self.generate_password()
                print(f"Generated password: {password}")
            entry = PasswordEntry(site, username, password)
            self.entries.append(entry)
            print(f"Added: {entry}")
            self.save()
        else:
            print("Site and username are required.")

    def view_entries(self):
        if not self.entries:
            print("No passwords yet.")
            return
        for i, e in enumerate(self.entries, 1):
            print(f"{i}. {e}")

    def search(self, term):
        found = [e for e in self.entries if term.lower() in e.site.lower() or term.lower() in e.username.lower()]
        if found:
            for e in found:
                print(e)
        else:
            print("No matches.")
