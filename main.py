from models.user import User

def main():
    database_host = 'localhost'  # Change as needed
    database_user = 'root'   # Change as needed
    database_password = ''  # Change as needed
    database_name = 'SecureAuthDB'  # Change as needed

    auth_system = User(database_host, database_user, database_password, database_name)

    # Example registration
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    auth_system.register_user(username, password)
    print("User registered successfully.")

    # Example verification
    username = input("Enter your username to log in: ")
    password = input("Enter your password: ")
    if auth_system.verify_user(username, password):
        print("Login successful.")
    else:
        print("Invalid credentials.")

    auth_system.close_connection()

if __name__ == "__main__":
    main()
