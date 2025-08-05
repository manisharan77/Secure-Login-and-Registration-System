import getpass
import hashlib
import re
import time

users = {}

login_attempts = {}

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@$!%*?&]", password):
        return False
    return True

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    print("\n=== User Registration ===")
    username = input("Choose a username: ").strip()
    
    if username in users:
        print("Username already exists. Try another.")
        return
    
    password = getpass.getpass("Choose a strong password: ")
    confirm = getpass.getpass("Confirm password: ")
    
    if password != confirm:
        print("Passwords do not match.")
        return
    
    if not is_strong_password(password):
        print("Password is not strong enough.")
        print("Password must have: min 8 chars, upper, lower, digit, and special char.")
        return
    
    users[username] = hash_password(password)
    print("Registration successful!")

def login():
    print("\n=== User Login ===")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if username not in users:
        print("User not found.")
        return

    if login_attempts.get(username, 0) >= 3:
        print("Account locked due to multiple failed attempts. Try again later.")
        return

    hashed_input = hash_password(password)
    if users[username] == hashed_input:
        print(f"Welcome, {username}! Login successful.")
        login_attempts[username] = 0  
        simulate_session(username)
    else:
        login_attempts[username] = login_attempts.get(username, 0) + 1
        print("Invalid credentials.")

def simulate_session(username):
    while True:
        print(f"\n-- Logged in as {username} --")
        print("1. View Profile")
        print("2. Logout")
        choice = input("Choose: ")
        if choice == "1":
            print(f"\nUsername: {username} \nPassword Hash: {users[username]}")
        elif choice == "2":
            print("Logged out.")
            break
        else:
            print("Invalid option.")

def main():
    print("Secure Login & User System")
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
