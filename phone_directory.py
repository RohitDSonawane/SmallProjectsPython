# Step 1: Initialize the Phone Directory
contacts = {}

# Step 6: Repeat the Menu until Exit
while True:
    # Step 4: Display the Menu
    print("Phone Directory Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            # Step 2: Add Contact
            name = input("Enter Name: ").strip()
            phone_number = input("Enter 10-digit Phone Number: ").strip()
            place = input("Enter Place: ").strip()

            # Step 5: Error handling for phone number
            if phone_number.isdigit() and len(phone_number) == 10:
                contacts[name] = {'Phone Number': phone_number, 'Place': place}
                print("Contact added successfully!\n")
            else:
                print("Error: Phone number must be exactly 10 digits and numeric.\n")

        elif choice == 2:
            # Step 3: Display Contacts
            if not contacts:
                print("No contacts available.\n")
            else:
                print("\nPhone Directory:")
                for name, details in contacts.items():
                    print(f"Name: {name}, Phone Number: {details['Phone Number']}, Place: {details['Place']}")
                print()

        elif choice == 3:
            print("Exiting Phone Directory. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

    except ValueError:
        print("Invalid input. Please enter a number (1-3).\n")
    except Exception as e:
        print("An unexpected error occurred:\n",e)