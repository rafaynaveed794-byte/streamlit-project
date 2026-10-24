
print("==========================================")
print("BUS TICKET BOOKING SYSTEM")
print("=============================")
cities = (
    "Karachi",
    "Hyderabad",
    "Sukkur",
    "Mirpur Khas",
    "Lahore"
)
routes = [
    {
        "route_id": "R101",
        "departure_city": "Karachi",
        "destination_city": "Hyderabad",
        "departure_time": "08:00 AM",
        "ticket_price": 1200,
        "total_seats": 40,
        "available_seats": 40
    },
    {
        "route_id": "R102",
        "departure_city": "Karachi",
        "destination_city": "Sukkur",
        "departure_time": "09:30 AM",
        "ticket_price": 2000,
        "total_seats": 36,
        "available_seats": 36
    },
    {
        "route_id": "R103",
        "departure_city": "Hyderabad",
        "destination_city": "Mirpur Khas",
        "departure_time": "11:00 AM",
        "ticket_price": 800,
        "total_seats": 32,
        "available_seats": 32
    },
    {
        "route_id": "R104",
        "departure_city": "Karachi",
        "destination_city": "Lahore",
        "departure_time": "07:00 PM",
        "ticket_price": 5000,
        "total_seats": 45,
        "available_seats": 45
    },
    {
        "route_id": "R105",
        "departure_city": "Sukkur",
        "destination_city": "Hyderabad",
        "departure_time": "02:00 PM",
        "ticket_price": 1500,
        "total_seats": 30,
        "available_seats": 30
    }
]
# STEP 3: BOOKING DATA
bookings = []
next_booking_number = 1001
def find_route(route_id):
    for route in routes:
        if route["route_id"] == route_id.upper():
            return route
    return None
def view_routes():
    print("\n========== AVAILABLE ROUTES ==========")
    for route in routes:
        if route["available_seats"] == 0:
            status = "Fully Booked"
        else:
            status = "Seats Available"

        print("\nRoute ID:", route["route_id"])
        print(
            "Journey:",
            route["departure_city"],
            "->",
            route["destination_city"]
        )
        print("Departure:", route["departure_time"])
        print("Price: Rs.", route["ticket_price"])
        print(
            "Seats:",
            route["available_seats"],
            "/",
            route["total_seats"]
        )
        print("Status:", status)
def search_route():
    search = input(
        "Enter route ID or city name: "
    ).strip().lower()
    if not search:
        print("Search cannot be empty.")
        return
    found = False
    for route in routes:
        if (
            search == route["route_id"].lower()
            or search == route["departure_city"].lower()
            or search == route["destination_city"].lower()
        ):
            print("\nRoute ID:", route["route_id"])
            print(
                "Journey:",
                route["departure_city"],
                "->",
                route["destination_city"]
            )
            print("Departure:", route["departure_time"])
            print("Price: Rs.", route["ticket_price"])
            print("Available seats:", route["available_seats"])
            found = True
    if not found:
        print("No matching route found.")
def book_ticket():
    global next_booking_number
    print("\n========== BOOK YOUR TICKET ==========")
    name = input("Enter passenger name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        age = int(input("Enter passenger age: "))
        if age <= 0:
            print("Age must be greater than zero.")
            return
        route_id = input(
            "Enter route ID (e.g. R101): "
        ).strip().upper()
        route = find_route(route_id)
        if route is None:
            print("Invalid route ID.")
            return
        seats = int(input("Enter number of seats: "))
        if seats <= 0:
            print("Seats must be greater than zero.")
            return
        if seats > route["available_seats"]:
            print("Not enough seats available.")
            return
    except ValueError:
        print("Please enter valid numbers for age and seats.")
        return
    booking_id = f"B{next_booking_number}"
    next_booking_number += 1
    total_fare = route["ticket_price"] * seats
    booking = {
        "booking_id": booking_id,
        "passenger_name": name,
        "passenger_age": age,
        "route_id": route["route_id"],
        "seats": seats,
        "total_fare": total_fare,
        "status": "Confirmed"
    }
    bookings.append(booking)
    route["available_seats"] -= seats
    print("\n========== BOOKING CONFIRMED ==========")
    print("Booking ID:", booking_id)
    print("Passenger:", name)
    print("Age:", age)
    print(
        "Journey:",
        route["departure_city"],
        "->",
        route["destination_city"]
    )
    print("Departure:", route["departure_time"])
    print("Seats booked:", seats)
    print("Fare per seat: Rs.", route["ticket_price"])
    print("Total fare: Rs.", total_fare)
    print("Status: Confirmed")
def view_bookings():
    print("\n========== BOOKING HISTORY ==========")
    if not bookings:
        print("No bookings found.")
        return
    for booking in bookings:
        print("\nBooking ID:", booking["booking_id"])
        print("Passenger:", booking["passenger_name"])
        print("Age:", booking["passenger_age"])
        print("Route ID:", booking["route_id"])
        print("Seats:", booking["seats"])
        print("Total fare: Rs.", booking["total_fare"])
        print("Status:", booking["status"])
def cancel_booking():
    booking_id = input(
        "Enter booking ID to cancel: "
    ).strip().upper()
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            if booking["status"] == "Cancelled":
                print("This booking is already cancelled.")
                return
            route = find_route(booking["route_id"])
            if route is not None:
                route["available_seats"] += booking["seats"]
            booking["status"] = "Cancelled"
            print("Booking cancelled successfully.")
            print("Booking ID:", booking_id)
            print("Seats restored:", booking["seats"])
            return
    print("Booking ID not found.")
def seat_availability():
    print("\n========== SEAT AVAILABILITY ==========")
    for route in routes:
        available = route["available_seats"]
        total = route["total_seats"]
        if available == 0:
            status = "Fully Booked"
        elif available == total:
            status = "Available"
        else:
            status = "Partially Booked"
        print(
            route["route_id"],
            "|",
            route["departure_city"],
            "->",
            route["destination_city"],
            "| Seats:",
            f"{available}/{total}",
            "|",
            status
        )
# STEP 11: BOOKING REPORT
def booking_report():
    total_bookings = len(bookings)
    confirmed = 0
    cancelled = 0
    reserved_seats = 0
    revenue = 0
    for booking in bookings:
        if booking["status"] == "Confirmed":
            confirmed += 1
            reserved_seats += booking["seats"]
            revenue += booking["total_fare"]
        elif booking["status"] == "Cancelled":
            cancelled += 1

    print("\n========== BOOKING REPORT ==========")
    print("Total bookings:", total_bookings)
    print("Confirmed bookings:", confirmed)
    print("Cancelled bookings:", cancelled)
    print("Reserved seats:", reserved_seats)
    print("Confirmed revenue: Rs.", revenue)
    print("\n========== ROUTE-WISE REPORT ==========")
    for route in routes:
        route_seats = 0
        route_revenue = 0
        for booking in bookings:
            if (
                booking["route_id"] == route["route_id"]
                and booking["status"] == "Confirmed"
            ):
                route_seats += booking["seats"]
                route_revenue += booking["total_fare"]
        print(
            route["route_id"],
            "| Seats booked:", route_seats,
            "| Revenue: Rs.", route_revenue
        )
# STEP 12: ROUTE SCHEDULE
def route_schedule():
    print("\n========== ROUTE SCHEDULE ==========")
    for city in cities:
        print("\nCity:", city)
        found = False
        for route in routes:
            if route["departure_city"] == city:
                print(
                    route["route_id"],
                    "->",
                    route["destination_city"],
                    "| Departure:",
                    route["departure_time"]
                )
                found = True
        if not found:
            print("No scheduled departures.")
while True:
    print("\n===================================")
    print("   SMART BUS RESERVATION SYSTEM")
    print("===================================")
    print("1. View Available Routes")
    print("2. Search for a Route")
    print("3. Book a Ticket")
    print("4. View Booking History")
    print("5. Cancel a Booking")
    print("6. View Seat Availability")
    print("7. Generate Booking Report")
    print("8. View Route Schedule")
    print("9. Exit")
    print("===================================")
    choice = input("Enter your choice (1-9): ").strip()
    if choice == "1":
        view_routes()
    elif choice == "2":
        search_route()
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        view_bookings()
    elif choice == "5":
        cancel_booking()
    elif choice == "6":
        seat_availability()
    elif choice == "7":
        booking_report()
    elif choice == "8":
        route_schedule()
    elif choice == "9":
        print("Thank you for using Smart Bus Reservation System!")
        break
    else:
        print("Invalid choice. Enter a number from 1 to 9.")