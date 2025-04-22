# main_app.py

from reserved_guests import ReservedGuests

def main():
    print("🛎️ Welcome to My Hotel Booking System 🛎️")
    reserved = ReservedGuests()

    while True:
        print("\nWhat would you like to do?")
        print("1. View Reserved Guests")
        print("2. Make a Booking Reservation")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            reserved.view_reserved_rooms()

        elif choice == "2":
            try:
                group_size = int(input("Enter number of guests in the group (max 3): "))
                if group_size < 1 or group_size > 3:
                    print("Invalid group size. Please enter between 1 and 3.")
                    continue

                for i in range(group_size):
                    print(f"\nGuest {i+1}:")
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    length_of_stay = int(input("Length of stay (nights): "))
                    room_class = input("Room Class (Standard, Deluxe, Superior): ").capitalize()

                    reserved.reserve_room(first_name, last_name, length_of_stay, room_class)

            except ValueError:
                print("Please enter valid numeric input where required.")

        elif choice == "3":
            print("Thank you for using My Hotel Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
