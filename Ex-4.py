bikes = 10
Space_in_a_bike = 2
drivers = 5
passengers = 10
bikes_not_driven = bikes - drivers
bikes_driven = drivers
bike_pool_capacity = bikes_driven * Space_in_a_bike
average_passengers_per_bikes = passengers / bikes_driven
print("There are", bikes, "bikes available.")
print("There are only", drivers, "drivers available.")
print("There will be", bikes_not_driven, "empty bikes today.")
print("We can transport", bike_pool_capacity, "people today.")
print("We have", passengers, "to bike pool today.")
print("We need to put about", average_passengers_per_bikes, "in each car.")