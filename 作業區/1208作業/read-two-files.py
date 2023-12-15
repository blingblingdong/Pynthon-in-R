# Writing sample data to world_population.txt
with open("world_population.txt", "w") as fw1:
    fw1.write("China=34567895678\nIndia=98765445673456789\nJapan=2453764724575")

# Writing sample data to world_area.txt
with open("world_area.txt", "w") as fw2:
    fw2.write("China=120\nIndia=100\nJapan=80")

# Reading data from world_population.txt
population_data = {}
with open("world_population.txt", "r") as p:
    for line in p:
        country, population = line.strip().split("=")
        population_data[country] = int(population)

# Reading data from world_area.txt
area_data = {}
with open("world_area.txt", "r") as a:
    for line in a:
        country, area = line.strip().split("=")
        area_data[country] = int(area)

# Calculating and writing density to world_density.txt
with open("world_density.txt", "w") as fw_density:
    for country in population_data:
        density = round(population_data[country] / area_data[country], 3)
        fw_density.write(f"{country} density: {density}\n")

