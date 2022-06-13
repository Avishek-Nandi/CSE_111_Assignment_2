# Solution to Task 6

class Country:
    name = 'Bangladesh'
    continent = 'Asia'
    capital = "Dhaka"
    fifa_ranking = 187


if __name__ == "__main__":

    country = Country()
    print('Name:', country.name)
    print('Continent:', country.continent)
    print('Capital:', country.capital)
    print('Fifa Ranking:', country.fifa_ranking)
    print('===================')
    country.name = 'Belgium'
    country.continent = 'Europe'
    country.capital = 'Brussels'
    country.fifa_ranking = 1
    print('Name:', country.name)
    print('Continent:', country.continent)
    print('Capital:', country.capital)
    print('Fifa Ranking:', country.fifa_ranking)
