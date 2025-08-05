# Secure-Login-and-Registration-System
A simple, secure user authentication system built in Python for terminal use. This project allows users to register with a strong password and securely log in with hashed credentials.

---
# 🚀 Features
- Register new users with strong password validation
- Login system with password hashing (SHA-256)
- Lock account after 3 failed login attempts
- Simulated user session after successful login
- Uses getpass for hidden password input
- In-memory storage (easy to extend to file/DB)
---
---
# 🛠️ Technologies Used
- Python 3
- hashlib for password hashing
- getpass for secure input
- re for password strength validation
---
---
# 📋 Password Strength Requirements
- Minimum 8 characters
- At least one uppercase, one lowercase, one digit, and one special character (@, $, !, %, *, ?, &)
---
---
# 🔧 How to Run
1- Make sure you have Python 3 installed
2- Run the script in terminal:
- python Securelogin.py
