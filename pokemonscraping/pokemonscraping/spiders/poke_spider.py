from scrapy import Spider
from scrapy import Request
from scrapy.selector import Selector
from pokemonscraping.items import PokemonscrapingItem


class PokeSpider(Spider):
    name = "pokespider"
    allowed_domains = ["serebii.net"]
    start_urls = ["https://serebii.net/pokedex-swsh/grookey/"]

    def weightParse(weightSelector):
        extractedLbs = weightSelector.extract()[0]
        if "/" in extractedLbs:
            extractedLbs = extractedLbs.split("/")[0].strip().replace("lbs", "")
            return extractedLbs
        else:
            extractedLbs = extractedLbs.strip().replace("lbs", "")
            return extractedLbs


    def parse(self, response):
        DexTables = Selector(response).xpath('//table[@class="dextable"]')
        AllMoves = Selector(response).xpath('//table[@class="dextable"]//td[@class="fooinfo"]//a[contains(@href,"attackdex")]//text()').extract()
        AbilitiesList = response.xpath('//table[@class="dextable"]//td[@class="fooinfo"]//a[contains(@href, "abilitydex")]//text()').extract()
       #AllTypes = response.xpath('//table[@class="dextable"]//td[@class="cen"]//a//img[contains(@alt, "type")]/@alt').extract()
       #CleanTypes = [type.replace("-type","") for type in AllTypes]
        item = PokemonscrapingItem()
        item['name'] = response.xpath('//table[@class="dextable"][2]//td[@class="fooinfo"]/text()').extract()[0]
        item['number'] = response.xpath('//table[@class="dextable"]//td[@class="fooinfo"]//td/text()').extract()[9]
        item['weight'] = weightParse(response.xpath('//table[@class="dextable"]//td[contains(text(), "lbs")]/text()'))
        item['types'] = []
        item['abilities'] = []
        item['moves'] = []
        for move in AllMoves:
            item['moves'].append(move)
        for ability in AbilitiesList:
            item['abilities'].append(ability)
        yield item
        followLink = response.xpath('//table[contains(@width,"100%")]//td[contains(@align,"center")]//a[contains(@href,"pokedex")]')[1].css('a::attr(href)').get()
        if followLink is not None:
            yield response.follow(followLink, callback=self.parse)
