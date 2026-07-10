print("Welcome! You will enjoy")
print("following the program.")
choice = input("Do you want to start? (yes/no): ").lower()

if choice == "no":
    print("So go away.")

elif choice == "yes":
    code = input("Type 11 to see the menu: ")

    if code == "11":
        print("Here is our menu:")
        print("1. Training")
        print("2. Match")
        print("3. Show my factors")
        print("4. I want to talk with coach")

        menu = input("Choose a number (1-4): ")

        if menu == "1":
            print("Today's training:")
            print("- Warm up")
            print("- Passing")
            print("- Shooting")
            print("- Stretching")
traning = input('choose:' \
'')
        elif menu == "2":
            print("No matches this week.")

        elif menu == "3":
            print("Your factors:")
            print("Speed: 80")
            print("Passing: 75")
            print("Shooting: 85")

        elif menu == "4":
            message = input("Write your message to the coach: ")
            print("Coach received your message:")
            print(message)

        else:
            print("Invalid menu choice.")

    else:
        print("Wrong code!")

else:
    print("Please type only 'yes' or 'no'.")