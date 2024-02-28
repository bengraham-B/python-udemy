# Add country name
country = input("Enter the country name: ")

# Number of visits
visits = int(input("Enter the number of visits: "))

# Create list from formatted string
list_of_cities = eval(input("Enter the list of cities as a formatted string: "))

# Print the list
print("List of cities:", list_of_cities)

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Function to add new country to the travel log
def add_new_country(country, visits, list_of_cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(new_country)

# Add new country to the travel log
add_new_country(country, visits, list_of_cities)

# Print the details of the newly added country
print(f"I've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
print(f"My favourite city was {travel_log[-1]['cities'][0]}.")
