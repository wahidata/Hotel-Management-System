# reserved_guests.py

from hotel_room import HotelRoom

class ReservedGuests:
    def __init__(self):
        self.guest_details = {}  # key: roomNumber, value: guest info dictionary
        self.hotel = HotelRoom()

    def add_guest(self, room_number, first_name, last_name, length_of_stay, room_class, bed_type, price):
        self.guest_details[room_number] = {
            "firstName": first_name,
            "lastName": last_name,
            "lengthOfStay": length_of_stay,
            "roomClass": room_class,
            "bedType": bed_type,
            "price": price
        }

    def assign_room_number(self, room_class):
        class_ranges = {
            "Standard": (1, 100),
            "Deluxe": (101, 200),
            "Superior": (201, 300)
        }
        if room_class not in class_ranges:
            print("Invalid room class.")
            return None

        start, end = class_ranges[room_class]
        for i in range(start, end + 1):
            room_num = str(i)
            if room_num not in self.guest_details:
                return room_num

        print(f"No rooms available for the selected class: {room_class}")
        return None

    def reserve_room(self, first_name, last_name, length_of_stay, room_class):
        bed_type = self.get_bed_type(room_class)
        room_number = self.assign_room_number(room_class)

        if room_number:
            price = self.hotel.get_room_rate(room_class)
            self.add_guest(room_number, first_name, last_name, length_of_stay, room_class, bed_type, price)
            print(f"Room reserved for {first_name} {last_name} in Room {room_number}. Price: £{price} per night.")
        else:
            print("Failed to reserve room. Please try again.")

    def get_bed_type(self, room_class):
        return {
            "Standard": "Twin or Double",
            "Deluxe": "Queen-sized bed",
            "Superior": "King-sized bed"
        }.get(room_class, "Unknown")

    def view_reserved_rooms(self):
        if not self.guest_details:
            print("No rooms have been reserved yet.")
            return

        print("\nReserved Rooms:\n")
        for room, guest in self.guest_details.items():
            print(f"Room Number: {room}")
            for k, v in guest.items():
                print(f"{k}: {v}")
            print()

    def get_guest_details(self):
        return self.guest_details
