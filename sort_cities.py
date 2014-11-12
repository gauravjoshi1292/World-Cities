from city import City
from quicksort import *

def compare_alpha(a, b):
    # Converts names to lowercase, and then returns true if a_name is alphabetically before b_name.
    a_name = a.name.lower()
    b_name = b.name.lower()
    if(a_name <= b_name):
        return True
    return False

def compare_population(a, b):
    if(a.population <= b.population):
        return False
    return True

def compare_latitude(a, b):
    if(a.latitude <= b.latitude):
        return True
    return False

cities = []

def in_cities():
    # Read cities from input file, create city objects, and populate list.
    in_file = open("world_cities.txt", "r")
    for line in in_file:
        line = line.strip() # remove whitespace from ends of line
        city_info = line.split(",")
        city = City(city_info[0], city_info[1], city_info[2], int(city_info[3]),
                    float(city_info[4]), float(city_info[5])) # initialize each city
        cities.append(city) # add city to list
    in_file.close()

def get_cities_sorted_by_population():
    # Returns the list of cities sorted by population.
    if(len(cities) == 0):
        in_cities()
    sort(cities, compare_population)
    return cities

def out_cities(out_file_name):
    # Write cities to output file. File name taken as argument.
    out_file = open(out_file_name, "w")
    first_line = True
    for city in cities:
        if(first_line): # no newline character before first line
            out_file.write(city.__str__())
            first_line = False
        else:
            out_file.write("\n" + city.__str__())
    out_file.close()


if __name__ == "__main__":
    # Read cities from input file, create city objects, and populate list.
    in_cities()

    # Write cities to output file.
    out_cities("cities_out.txt")

    # Alphabetical sorting and writing to file.
    sort(cities, compare_alpha)
    out_cities("cities_alpha.txt")

    # Sorting by population and writing to file.
    sort(cities, compare_population)
    out_cities("cities_population.txt")

    # Sorting by latitude and writing to file.
    sort(cities, compare_latitude)
    out_cities("cities_latitude.txt")
