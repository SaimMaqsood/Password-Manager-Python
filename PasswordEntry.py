"""
A class representing a single password entry.
"""
class PasswordEntry:
    """
    Constructs a password entry with site, username, and password.
    @param site the website/app name
    @param username the username/email
    @param password the password
    """
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.site} | Username: {self.username} | Password: {self.password}"
