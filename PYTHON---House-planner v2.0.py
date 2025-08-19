# house_planner.py

import json

class Furniture:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    def __str__(self):
        return f"{self.name} ({self.width}x{self.length} m, {self.area:.2f} m²)"

class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length
        self.furniture = []

    @property
    def area(self):
        return self.width * self.length

    @property
    def used_space(self):
        return sum(item.area for item in self.furniture)

    @property
    def free_space(self):
        return self.area - self.used_space

    def add_furniture(self, item):
        if item.area > self.free_space:
            return f"⚠️ Not enough free space in {self.name}! ({self.free_space:.2f} m² left)"
        self.furniture.append(item)
        return f"{item.name} added successfully 🪑"

    def remove_furniture(self, name):
        for item in self.furniture:
            if item.name.lower() == name.lower():
                self.furniture.remove(item)
                return f"{name} removed 🗑️"
        return "Furniture not found ❌"

    def show_furniture(self):
        if not self.furniture:
            return "No furniture added yet."
        return "\n".join([f"- {str(item)}" for item in self.furniture])

    def __str__(self):
        return f"{self.name} - {self.width}x{self.length} m ({self.area:.2f} m², Free: {self.free_space:.2f} m²)"

class HousePlanner:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, idx):
        try:
            removed = self.rooms.pop(idx - 1)
            print(f"Room '{removed.name}' removed 🗑️")
        except IndexError:
            print("Invalid room number ❌")

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

    def save_plan(self, filename="house_plan.json"):
        data = [
            {
                "name": room.name,
                "width": room.width,
                "length": room.length,
                "furniture": [
                    {"name": f.name, "width": f.width, "length": f.length}
                    for f in room.furniture
                ],
            }
            for room in self.rooms
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Plan saved 💾")

    def load_plan(self, filename="house_plan.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.rooms = [
                Room(r["name"], r["width"], r["length"])
                for r in data
            ]
            for room, rdata in zip(self.rooms, data):
                for f in rdata["furniture"]:
                    room.add_furniture(Furniture(f["name"], f["width"], f["length"]))
            print("Plan loaded 📂")
        except FileNotFoundError:
            print("No saved plan found ❌")

def main():
    planner = HousePlanner()

    while True:
        print("\n🏡 HOUSE PLANNER MENU")
        print("1. Add a room")
        print("2. Add furniture to a room")
        print("3. List all rooms")
        print("4. View room details")
        print("5. Remove a room")
        print("6. Remove furniture from a room")
        print("7. Save plan")
        print("8. Load plan")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

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
                message = planner.rooms[room_num - 1].add_furniture(
                    Furniture(furniture_name, f_width, f_length)
                )
                print(message)
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
            planner.list_rooms()
            num = int(input("Enter room number to remove: "))
            planner.remove_room(num)

        elif choice == '6':
            planner.list_rooms()
            num = int(input("Select room number: "))
            furniture_name = input("Enter furniture name to remove: ")
            print(planner.rooms[num - 1].remove_furniture(furniture_name))

        elif choice == '7':
            planner.save_plan()

        elif choice == '8':
            planner.load_plan()

        elif choice == '9':
            print("Goodbye! 🖐️")
            break

        else:
            print("Invalid choice, try again 🙃")

if __name__ == "__main__":
    main()
