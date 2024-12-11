from datetime import date
import uuid

class Bus:
    def __init__(self, bus_id: str, capacity: int, route: str):
        self.bus_id = bus_id
        self.capacity = capacity
        self.route = route
        self.available_seats = list(range(1, capacity + 1))

    def get_available_seats(self) -> list:
        return self.available_seats

    def book_seat(self, seat_number: int) -> bool:
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            return True
        return False

    def cancel_seat(self, seat_number: int):
        if seat_number not in self.available_seats:
            self.available_seats.append(seat_number)
            self.available_seats.sort()

class Passenger:
    def __init__(self, passenger_id: str, name: str, contact: str):
        self.passenger_id = passenger_id
        self.name = name
        self.contact = contact

class Ticket:
    def __init__(self, ticket_id: str, passenger: Passenger, bus: Bus,
                 seat_number: int, journey_date: date, price: float):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.bus = bus
        self.seat_number = seat_number
        self.journey_date = journey_date
        self.price = price

    def print_ticket(self):
        print("+----------------------------------------+")
        print(f"| Ticket ID      : {self.ticket_id}")
        print(f"| Passenger Name : {self.passenger.name}")
        print(f"| Contact        : {self.passenger.contact}")
        print(f"| Bus ID         : {self.bus.bus_id}")
        print(f"| Route          : {self.bus.route}")
        print(f"| Seat Number    : {self.seat_number}")
        print(f"| Journey Date   : {self.journey_date}")
        print(f"| Price          : ${self.price}")
        print("+----------------------------------------+")

class BookingSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.tickets = []

    def add_bus(self, bus_id: str, capacity: int, route: str):
        bus = Bus(bus_id, capacity, route)
        self.buses.append(bus)
        print(f"Bus: {bus_id} registration successful.")

    def add_passenger(self, name: str, contact: str):
        passenger_id = f"P{len(self.passengers) + 1:03}"
        passenger = Passenger(passenger_id, name, contact)
        self.passengers.append(passenger)
        print(f"Passenger: {name} registration successful. Passenger ID: {passenger_id}")

    def list_passengers(self):
        if not self.passengers:
            print("No passengers registered.")
            return

        print("\nRegistered Passengers:")
        for passenger in self.passengers:
            print(f"ID: {passenger.passenger_id}, Name: {passenger.name}, Contact: {passenger.contact}")

    def book_ticket(self, passenger_id: str, bus_id: str, seat_number: int, journey_date: date):
        passenger = next((p for p in self.passengers if p.passenger_id == passenger_id), None)
        bus = next((b for b in self.buses if b.bus_id == bus_id), None)

        if not passenger:
            print("Error: Passenger not registered. Use '2' to register a passenger.")
            self.list_passengers()
            return

        if not bus:
            print("Error: Bus not registered.")
            self.list_buses()  # Show the list of registered buses
            return

        if not bus.book_seat(seat_number):
            print("Error: Seat not available.")
            return

        ticket_id = f"TKT{str(uuid.uuid4())[:8]}"
        price = 500.0  # Example price
        ticket = Ticket(ticket_id, passenger, bus, seat_number, journey_date, price)
        self.tickets.append(ticket)
        print("Ticket booking successful!")
        ticket.print_ticket()

    def list_buses(self):
        if not self.buses:
            print("No buses registered.")
            return

        print("\nRegistered Buses:")
        for bus in self.buses:
            print(f"ID: {bus.bus_id}, Route: {bus.route}, Capacity: {bus.capacity}, Available Seats: {len(bus.get_available_seats())}")


    def print_all_tickets(self):
        if not self.tickets:
            print("No tickets to print.")
            return

        for ticket in self.tickets:
            ticket.print_ticket()

    def close_system(self):
        print("Closing Booking System. Have a nice day!")

# Login System
OPERATORS = {
    "ragib": "4567",
    "yasin": "7568",
    "mou": "0912"
}

def authenticate_operator(mock_input=None):
    print("Welcome to the Bus Ticket Management System")
    for _ in range(3):
        username = mock_input["username"] if mock_input else input("Enter Operator Username: ")
        password = mock_input["password"] if mock_input else input("Enter Operator Password: ")

        if username in OPERATORS and OPERATORS[username] == password:
            print("Authentication Successful!\n")
            return True

        print("Invalid credentials. Please try again.")

    print("Too many failed attempts. Exiting system.")
    return False

def main(mock_inputs=None):
    if not authenticate_operator(mock_inputs):
        return

    system = BookingSystem()

    mock_index = 0
    while True:
        print("\n--- Main Menu ---")
        print("1. Register Bus")
        print("2. Register Passenger")
        print("3. Book Ticket")
        print("4. Print All Tickets")
        print("5. Exit")

        choice = mock_inputs[mock_index]["choice"] if mock_inputs else input("Enter your choice: ")
        mock_index += 1 if mock_inputs else 0

        if choice == "1":
            bus_id = mock_inputs[mock_index]["bus_id"] if mock_inputs else input("Enter Bus ID: ")
            capacity = int(mock_inputs[mock_index]["capacity"] if mock_inputs else input("Enter Bus Capacity: "))
            route = mock_inputs[mock_index]["route"] if mock_inputs else input("Enter Bus Route: ")
            system.add_bus(bus_id, capacity, route)
            mock_index += 1 if mock_inputs else 0

        elif choice == "2":
            name = mock_inputs[mock_index]["name"] if mock_inputs else input("Enter Passenger Name: ")
            contact = mock_inputs[mock_index]["contact"] if mock_inputs else input("Enter Passenger Contact: ")
            system.add_passenger(name, contact)
            mock_index += 1 if mock_inputs else 0

        elif choice == "3":
            passenger_id = mock_inputs[mock_index]["passenger_id"] if mock_inputs else input("Enter Passenger ID: ")
            bus_id = mock_inputs[mock_index]["bus_id"] if mock_inputs else input("Enter Bus ID: ")
            seat_number = int(mock_inputs[mock_index]["seat_number"] if mock_inputs else input("Enter Seat Number: "))
            journey_date = date.fromisoformat(mock_inputs[mock_index]["journey_date"] if mock_inputs else input("Enter Journey Date (YYYY-MM-DD): "))
            system.book_ticket(passenger_id, bus_id, seat_number, journey_date)
            mock_index += 1 if mock_inputs else 0

        elif choice == "4":
            system.print_all_tickets()

        elif choice == "5":
            system.close_system()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
