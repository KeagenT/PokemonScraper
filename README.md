# Pokemon Scraper
  A dynamic scraper for serebii.net's galarian pokedex. 
  Use it to for whatever educational projects you'd like.
  Includes a pre-scraped GalarDex file with all new Galarian Pokemon. 
  The scraper has been tested for all Galar exclusive pokemon excluding
  expansion pokemon. It is possible to scrape mons inexclusive to galar, as the "types" field accounts for regional forms. 

# Using Scrapy
  This project requires Scrapy and Python 3.X to run.
  Refer to the [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html) 
  tutorial for more information.
  Navigate to this project's directory with the CLI and 
  run the following command:
```
scrapy crawl pokespider -o GalarDex.json -t json
```
  By default this project is configured to the "pokemonscraping" 
  directory and a spider named pokespider.
  Output is configured to give the 
  following (sample) JSON for each page scraped.


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
# Generated Data and Visualizations
  This folder contains python code to transform the generated GalarDex.json into json files
  organized by: Type, Location, and Moves.
  Run these scripts after scraping updated content (Looking at you crown tundra etc.)
  [Here's](https://keagent.github.io/PokemonScraper/) a sample visualization made with D3.js. 
  Feel free to use any of this project's scraped data with attribution. 

# Future plans
* Allow User input for the sample data visualization.
* Create a singular class to transform scraped data rather than current monolith.
* Test scraping for expansion added content
* Enable scraping for all gen 8 pokemon rather than Galar Exclusives

# Acknowledgements
  All Scraped content is © Copyright of Serebii.net 1999-2020.
  Pokémon and All Respective Names are Trademark & © of Nintendo 1996-2020.