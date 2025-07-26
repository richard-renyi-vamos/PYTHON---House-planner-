# house_planner.py

class Furniture:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    def __str__(self):
        return f"{self.name} ({self.width}x{self.length} m)"

class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length
        self.furniture = []

    def add_furniture(self, item):
        self.furniture.append(item)

    def show_furniture(self):
        if not self.furniture:
            return "No furniture added yet."
        return "\n".join([f"- {str(item)}" for item in self.furniture])

    def __str__(self):
        return f"{self.name} - {self.width}x{self.length} m"

class HousePlanner:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def list_rooms(self):
        if not self.rooms:
            print("No rooms added yet 🏚️")
        for idx, room in enumerate(self.rooms, 1):
            print(f"{idx}. {room}")

    def room_details(self, idx):
        try:
            room = self.rooms[idx - 1]
            print(f"\nRoom: {room}")
            print("Furniture:")
            print(room.show_furniture())
        except IndexError:
            print("Invalid room number ❌")

def main():
    planner = HousePlanner()

    while True:
        print("\n🏡 HOUSE PLANNER MENU")
        print("1. Add a room")
        print("2. Add furniture to a room")
        print("3. List all rooms")
        print("4. View room details")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Room name: ")
            width = float(input("Room width (m): "))
            length = float(input("Room length (m): "))
            planner.add_room(Room(name, width, length))
            print("Room added successfully ✅")

        elif choice == '2':
            planner.list_rooms()
            try:
                room_num = int(input("Select room number: "))
                furniture_name = input("Furniture name: ")
                f_width = float(input("Furniture width (m): "))
                f_length = float(input("Furniture length (m): "))
                planner.rooms[room_num - 1].add_furniture(Furniture(furniture_name, f_width, f_length))
                print("Furniture added successfully 🪑")
            except Exception as e:
                print("Error adding furniture ❗", e)

        elif choice == '3':
            planner.list_rooms()

        elif choice == '4':
            planner.list_rooms()
            try:
                room_num = int(input("Enter room number to view: "))
                planner.room_details(room_num)
            except Exception as e:
                print("Error viewing room ❗", e)

        elif choice == '5':
            print("Goodbye! 🖐️")
            break

        else:
            print("Invalid choice, try again 🙃")

if __name__ == "__main__":
    main()
