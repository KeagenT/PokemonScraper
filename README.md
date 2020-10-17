# Pokemon Scraper
A simple scraper for serebii.net's galarian pokedex. Use it to build your own PokemonDB.
For fun Data analytics projects.
Comes with a pre-scraped JSON file with all new Galarian Pokemon. The scraper has been tested
for all Galar exclusive mons. It is possible to scrape mons inexclusive to galar, as the "types" field accounts for regional forms. 

# Using Scrapy
This project requires Scrapy and Python 3.X to run.
Refer to the [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html) tutorial for running a crawler
By default this project is configured to the "pokemonscraping" directory and a spider named pokecrawler.
Output is configured to give the following (sample) JSON for each page scraped.

```
  {
    "name": "Pokemon name",
    "number": "National pokedex number",
    "weight": "Weight" (in lbs)
    "types": {
        "Normal or Regional Form": ["Type"]

      },
    "locations_sword": ["locations"],
    "locations_shield": ["locations"],
    "abilities": ["Array of abilities"],
    "moves": ["Array of all moves"]
   }
```
# Future plans
No <3