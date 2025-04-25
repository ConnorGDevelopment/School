names = ["Huey Duck", "Dewey Duck", "Louie Duck"]
addresses = ["1 McDuck Manor Apt 2", "1 McDuck Manor Apt 3", "1 McDuck Manor Apt 4"]
cities = ["Duckberg", "Thiswasapoorchoice", "Theylivetogether"]
states = ["UH", "OH", "ER"]
zipCodes = ["12345", "67890", "42420"]
ages = [10, 11, 12]
heights = [50.0, 50.1, 50.2]

for i in range(0, len(names)):
    print(names[i])
    print(addresses[i])
    print(f"{cities[i]}, {states[i]} {zipCodes[i]}")
    print(f"Age: {ages[i]}")
    print(f"Heights: {heights[i]}")
    print(" ")
 
print(f"Average Age: {sum(ages)/len(ages)}")
