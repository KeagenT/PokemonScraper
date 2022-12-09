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
    locations_scarlet = Field()
    locations_violet = Field()
    egg_moves = Field()
    egg_group = Field()
    types = Field()
    abilities = Field()
    moves = Field()
    pass
