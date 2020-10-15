# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class PokemonscrapingItem(scrapy.Item):
    name = Field()
    number = Field()
    weight = Field()
    locations_sword = Field()
    locations_shield = Field()
    types = Field()
    abilities = Field()
    moves = Field()
    pass
