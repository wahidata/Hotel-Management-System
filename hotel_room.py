# hotel_room.py

class HotelRoom:
    def __init__(self):
        self.room_details = {}      # key: Room:101, value: "Class: Deluxe, Description: ..., Type: ..."
        self.room_rates = {}        # key: Deluxe, value: 150
        self.total_rooms = {}       # key: Deluxe, value: 100

        # Initialise room data
        self.add_room("1-100", "Standard", "Budget friendly", "Twin or Double")
        self.add_room("101-200", "Deluxe", "Enhanced comfort", "Queen-sized bed")
        self.add_room("201-300", "Superior", "Premium Services", "King-sized bed")

        self.add_rate("Standard", 100)
        self.add_rate("Deluxe", 150)
        self.add_rate("Superior", 200)

        self.add_total_rooms("Standard", 100)
        self.add_total_rooms("Deluxe", 100)
        self.add_total_rooms("Superior", 100)

    def add_room(self, room_range, room_class, description, bed_type):
        start, end = map(int, room_range.split('-'))
        for num in range(start, end + 1):
            key = f"Room:{num}"
            value = f"Class: {room_class}, Description: {description}, Type: {bed_type}"
            self.room_details[key] = value

    def add_rate(self, room_class, rate):
        self.room_rates[room_class] = rate

    def add_total_rooms(self, room_class, total):
        self.total_rooms[room_class] = total

    def get_room_details(self, room_number):
        key = f"Room:{room_number}"
        return self.room_details.get(key, "Room not found")

    def get_room_rate(self, room_class):
        return self.room_rates.get(room_class, 0)

    def get_total_rooms(self, room_class):
        return self.total_rooms.get(room_class, 0)
