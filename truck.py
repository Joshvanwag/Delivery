from datetime import timedelta
from data import get_distance, distance_table, hash_table

#create truck class
class Truck:
    def __init__(self, packages=None, departure_time=timedelta(minutes=0)):
        if packages is None:
            packages = []
        self.packages = packages
        self.mileage = 0
        self.next_location = "4001 South 700 East"
        self.departure_time= departure_time
        self.time = timedelta(minutes=0)

    #main algorithm
    def deliver_packages(self):
        not_delivered = self.packages.copy() # create new list to remove delivered packages from
        while len(not_delivered) > 0:

            #initialize variables
            shortest_distance = float("inf")
            next_package_id = None
            next_package_data = None

            #compares every package to the current location and finds closest
            for package_id in not_delivered:
                package_data = hash_table.lookup(str(package_id))# returns all the data in package as string. i.e. 1: "address",...
                package_data[10] = str(self.departure_time)

                #handles change made to package 9 address by only editing the package if its after 10:20
                if package_id == 9 and (self.time + self.departure_time) > timedelta(hours = 10, minutes = 20):
                    package_data[1] = "410 S State St"


                i = distance_table[self.next_location]
                j = distance_table[package_data[1]]
                distance = get_distance(i,j) # references distance matrix
                if distance < shortest_distance:
                    shortest_distance = distance
                    next_package_id = package_id
                    next_package_data = package_data

            # updates distance traveled, time taken, current location, and removes package from not_delivered
            not_delivered.remove(next_package_id)
            self.next_location = next_package_data[1] # the next location to be compared is updated to what the closest location was
            self.mileage += shortest_distance
            next_package_data[11] = str(self.time + self.departure_time)
            self.time += timedelta(minutes = shortest_distance/ (18/60))
            next_package_data[9] = str(self.time+ self.departure_time)
            next_package_data[8] = "Delivered"

            #if packages have been delivered, calculates distance to hub and time taken to drive back
            if len(not_delivered) == 0:
                go_home = get_distance(distance_table[next_package_data[1]], distance_table["4001 South 700 East"])
                self.mileage += go_home
                self.time += timedelta(minutes = go_home/(18/60))


