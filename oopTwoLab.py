from datetime import date, datetime
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

    def get_bus_details(self) -> dict:
        return {
            "bus_id": self.bus_id,
            "capacity": self.capacity,
            "route": self.route,
            "available_seats": len(self.available_seats)
        }


class Passenger:
    def __init__(self, passenger_id: str, name: str, contact: str, email: str):
        self.passenger_id = passenger_id
        self.name = name
        self.contact = contact
        self.email = email

    def get_passenger_details(self) -> dict:
        return {
            "passenger_id": self.passenger_id,
            "name": self.name,
            "contact": self.contact,
            "email": self.email
        }

    def update_contact(self, new_contact: str):
        self.contact = new_contact

    def update_email(self, new_email: str):
        self.email = new_email


class Ticket:
    def __init__(self, ticket_id: str, passenger: Passenger, bus: Bus,
                 seat_number: int, journey_date: date, price: float):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.bus = bus
        self.seat_number = seat_number
        self.journey_date = journey_date
        self.status = "CONFIRMED"
        self.price = price

    def cancel_ticket(self):
        if self.status != "CANCELLED":
            self.status = "CANCELLED"
            self.bus.cancel_seat(self.seat_number)
            return True
        return False

    def get_ticket_details(self) -> dict:
        return {
            "ticket_id": self.ticket_id,
            "passenger": self.passenger.get_passenger_details(),
            "bus": self.bus.get_bus_details(),
            "seat_number": self.seat_number,
            "journey_date": self.journey_date,
            "status": self.status,
            "price": self.price
        }


class BookingSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.tickets = []

    def add_bus(self, bus: Bus):
        self.buses.append(bus)

    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)

    def book_ticket(self, passenger: Passenger, bus: Bus,
                    seat_number: int, journey_date: date) -> Ticket:
        if bus.book_seat(seat_number):
            ticket_id = f"TKT{str(uuid.uuid4())[:8]}"
            price = 500.0  # Sample price, can be calculated based on route
            ticket = Ticket(ticket_id, passenger, bus, seat_number, journey_date, price)
            self.tickets.append(ticket)
            return ticket
        return None

    def cancel_ticket(self, ticket_id: str) -> bool:
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket.cancel_ticket()
        return False

    def get_available_buses(self, journey_date: date) -> list:
        return [bus for bus in self.buses if len(bus.get_available_seats()) > 0]

    def get_booking_history(self, passenger_id: str) -> list:
        return [ticket for ticket in self.tickets
                if ticket.passenger.passenger_id == passenger_id]


def main():
    print("=== Bus Ticket Management System ===")
    print("Initializing Booking System...")

    # Initialize the booking system
    booking_system = BookingSystem()

    # Create and add buses
    print("\n--- Adding Buses ---")
    bus1 = Bus("BUS001", 40, "New York - Boston")
    bus2 = Bus("BUS002", 35, "Boston - Washington DC")
    booking_system.add_bus(bus1)
    booking_system.add_bus(bus2)

    print(f"Added Bus 1: {bus1.get_bus_details()}")
    print(f"Added Bus 2: {bus2.get_bus_details()}")

    # Create and add passengers
    print("\n--- Registering Passengers ---")
    passenger1 = Passenger("P001", "John Doe", "1234567890", "john@example.com")
    passenger2 = Passenger("P002", "Jane Smith", "0987654321", "jane@example.com")
    booking_system.add_passenger(passenger1)
    booking_system.add_passenger(passenger2)

    print(f"Registered Passenger 1: {passenger1.get_passenger_details()}")
    print(f"Registered Passenger 2: {passenger2.get_passenger_details()}")

    # Book tickets
    print("\n--- Booking Tickets ---")
    journey_date = date(2024, 12, 25)
    ticket1 = booking_system.book_ticket(passenger1, bus1, 5, journey_date)

    if ticket1:
        print("✅ Ticket Booked Successfully!")
        print("\n--- Ticket Details ---")
        ticket_details = ticket1.get_ticket_details()
        for key, value in ticket_details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

    # Cancel ticket
    print("\n--- Ticket Cancellation ---")
    if booking_system.cancel_ticket(ticket1.ticket_id):
        print("✅ Ticket Cancelled Successfully!")
    else:
        print("❌ Ticket Cancellation Failed")

    # Get booking history
    print("\n--- Booking History ---")
    history = booking_system.get_booking_history(passenger1.passenger_id)
    print(f"Booking History for {passenger1.name}:")

    if history:
        for ticket in history:
            print("\n--- Ticket Details ---")
            ticket_details = ticket.get_ticket_details()
            for key, value in ticket_details.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("No booking history found.")

    print("\n=== End of Booking System Demonstration ===")


if __name__ == "__main__":
    main()