passwords = []

def add_password():
    print("\n--- Add Password ---")

    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    account = {
        "website": website,
        "username": username,
        "password": password
    }

    passwords.append(account)

    print("Password saved successfully!")


def view_passwords():
    print("\n--- Saved Passwords ---")

    if len(passwords) == 0:
        print("No passwords saved.")
        return

    for i, account in enumerate(passwords, 1):
        print("\nAccount", i)
        print("Website :", account["website"])
        print("Username:", account["username"])
        print("Password:", account["password"])


def search_password():
    print("\n--- Search Password ---")

    website = input("Enter website to search: ")

    found = False

    for account in passwords:
        if account["website"].lower() == website.lower():
            print("\nAccount found!")
            print("Website :", account["website"])
            print("Username:", account["username"])
            print("Password:", account["password"])
            found = True

    if not found:
        print("No account found.")


def delete_password():
    print("\n--- Delete Password ---")

    website = input("Enter website to delete: ")

    for account in passwords:
        if account["website"].lower() == website.lower():
            passwords.remove(account)
            print("Account deleted successfully!")
            return

    print("Account not found.")


def count_passwords():
    print("\n--- Password Count ---")
    print("Total saved accounts:", len(passwords))


def main():
    while True:
        print("\n==============================")
        print("       PASSWORD MANAGER")
        print("==============================")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Count Passwords")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            search_password()

        elif choice == "4":
            delete_password()

        elif choice == "5":
            count_passwords()

        elif choice == "6":
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid choice. Try again.")


main()
