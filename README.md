# PokemonScraper
A simple scraper for serebii.net's galarian pokedex. Use it to build your own PokemonDB

# Using Scrapy
This project requires Scrapy and Python 3.X to run.
Refer to the Scrapy tutorial for running a crawler https://docs.scrapy.org/en/latest/intro/tutorial.html
By default this project is configured to the "pokemonscraping" and a spider named pokecrawler.
Output is configured to give the following JSON for each page scraped.

```
  {
    "name": "Pokemon name",
    "number": "National pokedex number",
    "abilities": ["Array of abilities"],
    "moves": ["Array of all moves"]
   }
```
