# Student ID 009931743
from datetime import timedelta, datetime
from truck import Truck
from data import load_packages, hash_table

#create list of packages to load into trucks
truck_packages1 = [1, 13, 14, 15, 16,19, 20, 29, 30, 31, 34, 37, 40]
truck_packages2 = [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
truck_packages3 = [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33]

#Loads trucks with lists and departure time
Truck1 = Truck(truck_packages1, timedelta(hours=8))
Truck2 = Truck(truck_packages2, timedelta(hours=9, minutes = 5))



#Delivers the packages in trucks 1 and 2
Truck1.deliver_packages()
Truck2.deliver_packages()

#calculates which truck gets back first and then delivers truck 3
truckTime = min(Truck1.time, Truck2.time) + timedelta(hours=8)
Truck3 = Truck(truck_packages3, truckTime)
Truck3.deliver_packages()

# Function to get status of a package
def check_package_status(package_data, query_time):
    delivery_time = datetime.strptime(package_data[9], '%H:%M:%S')
    departure_time = datetime.strptime(package_data[10], '%H:%M:%S')
    next_stop = datetime.strptime(package_data[11], '%H:%M:%S')
    if query_time <= departure_time:
        return "At Hub"
    elif departure_time < query_time < next_stop:
        return "En Route"
    elif next_stop <= query_time < delivery_time:
        return "Next Stop"
    else:
        return f"Delivered at {delivery_time.time()}"

# Function to print all packages with status and truck number included
def print_package_statuses_at_time(query_time):
    print(f"\nPackage status at {query_time.time()}:\n")
    for package_id in range(1, 41):  # assuming 40 packages
        package = hash_table.lookup(str(package_id))
        status = check_package_status(package, query_time)
        address = package[1]

        #Logic to print out address of package 9 before and after correction
            #In the algorithm it handles the change, but this just prints it out
        compare_query = query_time.time()
        time_as_delta = timedelta(hours=compare_query.hour, minutes=compare_query.minute)
        if package_id in [6, 25, 28, 32] and time_as_delta < timedelta(hours=9, minutes=5):
            status = "Delayed on Flight---will not arrive to depot until 9:05 am."
        if package_id == 9 and time_as_delta < timedelta(hours=10, minutes=20):
            address = "300 State St"

        if package_id in truck_packages1:
            truck_id = 1
        elif package_id in truck_packages2:
            truck_id = 2
        else:
            truck_id = 3
        print(f"Package {package_id}: {status}  Delivery Address: - {address} - Truck number: {truck_id}")

# prints a single packages status with truck number
def print_single_package_status(package_id, query_time):
    package = hash_table.lookup(str(package_id))
    status = check_package_status(package, query_time)


    address = package[1]

    # Logic to print out address of package 9 before and after correction
    # In the algorithm it handles the change, but this just prints it out
    compare_query = query_time.time()
    time_as_delta = timedelta(hours=compare_query.hour, minutes=compare_query.minute)
    if package_id in [6, 25, 28, 32] and time_as_delta < timedelta(hours=9, minutes=5):
        status = "Delayed on Flight---will not arrive to depot until 9:05 am."
    if package_id == 9 and time_as_delta < timedelta(hours=10, minutes=20):
        address = "300 State St"

    if package_id in truck_packages1:
        truck_id = 1
    elif package_id in truck_packages2:
        truck_id = 2
    else:
        truck_id = 3
    print(f"\nPackage {package_id} status at {query_time.time()}: {status}  Delivery Address: - {address} - Truck number: {truck_id}\n")

#Interface for viewing status. Allows user to choose options to view statuses or to exit.
def delivery_status_interface():
    while True:
        print("=== WGUPS Package Status Checker ===")
        print("1. View ALL package statuses at a specific time")
        print("2. View SINGLE package status at a specific time")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            time_input = input("Enter time (HH:MM): ")
            try:
                query_time = datetime.strptime(time_input, "%H:%M")
                print_package_statuses_at_time(query_time)
            except ValueError:
                print("Invalid time format. Please use HH:MM.\n")

        elif choice == "2":
            package_id = input("Enter package ID (1–40): ")
            time_input = input("Enter time (HH:MM): ")
            try:
                query_time = datetime.strptime(time_input, "%H:%M")
                print_single_package_status(int(package_id), query_time)
            except ValueError:
                print("Invalid input. Make sure time is HH:MM and package ID is a number.\n")

        elif choice == "3":
            print("Exiting WGUPS Status Checker.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

#call user interface
delivery_status_interface()

#print total mileage of all trucks
total_mileage = Truck1.mileage + Truck2.mileage + Truck3.mileage
print(f"\nTotal mileage of all trucks: {total_mileage:.2f}")

