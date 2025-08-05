# This file handles shared classes and data used in main and truck.py
import csv
import datetime
from datetime import timedelta
from hashTable import HashTable

#creates a dictionary to store the addresses as keys to reference in get_distance
distance_table = {}

#reads the file into distance table
with open('WGUPS Distance Table.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for items in reader:
        distance_table[items[2]] = items[0]

with open('WGUPS Distance Table.csv') as file:
    csv_distances = list(csv.reader(file))

#function to get distance on distance matrix
def get_distance(i, j):
    j = int(j) +2 # +2 is to account for headers and columns
    i = int(i)+2
    if i == j:
        return 0.0
    elif i > j:
        distance = csv_distances[i][j]
    else:
        distance = csv_distances[j][i]
    return float(distance)


#create hashtable and creates function to load packages
hash_table = HashTable()
def load_packages(file_path):

    with open(file_path) as f:
        for line in f:
            parts = line.split(',')
            package_id = parts[0]
            address = parts[1]
            city = parts[2]
            state = parts[3]
            zipcode = parts[4]
            delivery_deadline = parts[5]
            weight = parts[6]
            instructions = parts[7]
            status_update = "At Hub"
            time_delivered = str(datetime.timedelta(minutes=0))
            departure_time = str(datetime.timedelta(minutes=0))
            next_stop = str(datetime.timedelta(minutes=0))
            data = [package_id, address, city, state, zipcode, delivery_deadline, weight, instructions, status_update, time_delivered, departure_time, next_stop]

            hash_table.add(package_id, data)
    return hash_table
#load hash table
load_packages('package.csv')


