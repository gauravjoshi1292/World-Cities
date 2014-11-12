class City:

    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.name, self.population, self.latitude, self.longitude)
