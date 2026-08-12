import os
movies={
    1: {"name": "Avengers", "price":250, "seats":30},
    2: {"name": "Pushpa 2", "price":200, "seats":25},
    3: {"name": "KGF 2", "price":180, "seats":20},
    4: {"name": "Jawan", "price":220, "seats":15}
}
bookings={}
def save_booking():
    with open("booking.txt","w") as file:
        for user, data in bookings.items():
            file.write(f"{user},{data['movie']},{data['tickets']},{data['amount']}\n")

def load_booking():
    if os.path.exists("booking.txt"):
        with open("booking.txt","r") as file:
            for line in file:
                user,movie,tickets,amount=line.strip().split(",")
                bookings[user]={
                    "movie":movie,
                    "tickets":int(tickets),
                    "amount":int(amount)
                }
def show_movies():
    print("\n------MOVIES-----")
    for key, value in movies.items():
        print(f"{key}. {value['name']} | Price: ₹{value['price']} | Seats Left: {value['seats']}")

def book_ticket():
    name=input("enter your name :")

    show_movies()

    try:
        choice=int(input("select movie: "))

        if choice not in movies:
            print("Invalid choice")
            return
        ticket=int(input("enter number of tickets: "))

        if ticket>movies[choice]["seats"]:
            print("seats not available")
            return

        amount=ticket*movies[choice]["price"]

        movies[choice]["seats"] -= ticket

        bookings[name] = {
            "movie": movies[choice]["name"],
            "tickets": ticket,
            "amount": amount
        }
        save_booking()

        print("\nBooking Successful")
        print("------------------------")
        print("Customer :", name)
        print("Movie    :", movies[choice]["name"])
        print("Tickets  :", ticket)
        print("Amount   : ₹", amount)

    except ValueError:
        print("Enter Valid Number")
def cancel_ticket():
    name = input("Enter Your Name: ")

    if name in bookings:

        movie_name = bookings[name]["movie"]

        for movie in movies.values():
            if movie["name"] == movie_name:
                movie["seats"] += bookings[name]["tickets"]

        del bookings[name]
        save_booking()
        print("Booking Cancelled Successfully")

    else:
        print("No Booking Found")

def view_booking():
    name = input("Enter Your Name: ")

    if name in bookings:
        print("\n------ BOOKING ------")
        print("Movie :", bookings[name]["movie"])
        print("Tickets :", bookings[name]["tickets"])
        print("Amount : ₹", bookings[name]["amount"])
    else:
        print("No Booking Found")

load_booking()

while True:

    print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_booking()

    elif choice == "4":
        cancel_ticket()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")





