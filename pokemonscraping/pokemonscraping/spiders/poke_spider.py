from scrapy import Spider
from scrapy import Request
from scrapy.selector import Selector
from pokemonscraping.items import PokemonscrapingItem
import re


class PokeSpider(Spider):
    name = "pokespider"
    allowed_domains = ["serebii.net"]
    start_urls = ["https://www.serebii.net/pokedex-sv/sprigatito/"]


    def parse(self, response):

        def weightParse(weightSelector):
            extractedLbs = weightSelector.extract()[0]
            if "/" in extractedLbs:
                extractedLbs = extractedLbs.split("/")[0].strip().replace("lbs", "")
                return extractedLbs
            else:
                extractedLbs = extractedLbs.strip().replace("lbs", "")
                return extractedLbs

        #takes the attribute list of a pokemon's type images and removes the -type for every item in the list
        def getCleanTypes(inputTypesList):
            return [types.replace("-type","") for types in inputTypesList]

        #checks if the pokemon's type category has multiple forms, and gets a cleaned list of those forms
        def getAlternateFormsList():
            #Filters out junk \t \r \anything tags and empty spaces in the list
            junkText = re.compile(r"((\\.)+|\s)")
            dirtyAlternateFormsList = response.xpath('//table[@class="dextable"]//td[@class="cen"]//tr[*]//text()').extract()
            cleanedForms = [form for form in dirtyAlternateFormsList if not junkText.match(form)]
            return cleanedForms

        #gets the xpath object for a given alternate form. Used when a pokemon has multiple forms with different types.
        def getFormXPathObject(form):
            formXpath = response.xpath('//table[@class="dextable"]//td[@class="cen"]//tr[*[contains(text(), {})]]'.format("\""+form+"\""))
            return formXpath

        #gets a list of a pokemon's type from the above function's xpath object. 
        #Darmanitan is the only pokemon that has two different forms with the same name and thus returns 2 xpath objects
        def getTypesFromXpath(inputXpath, index = 0):
            return getCleanTypes(inputXpath[index].xpath('.//a//img[contains(@alt, "type")]/@alt').extract())

        #builds a dictionary for the types field with multiple keys if there's multiple forms or just "normal" if there are no alternate forms for that pokemon
        def buildTypesDict():
            typesDict = {}
            formsList = getAlternateFormsList()
            #if the alternate forms list is empty
            if not formsList:
                NormalFormTypes = response.xpath('//table[@class="dextable"]//td[@class="cen"]')[0].xpath('.//a//img[contains(@alt, "type")]/@alt').extract()
                CleanTypes = getCleanTypes(NormalFormTypes)
                typesDict['Normal'] = CleanTypes
                return typesDict
            else:
                for alternateForm in formsList:
                    #Literally just a check for Darmanitan
                    currentFormXpath = getFormXPathObject(alternateForm)
                    if alternateForm not in typesDict.keys():
                        typesDict[alternateForm] = getTypesFromXpath(currentFormXpath)
                    else:
                        alternateForm = "Galarian "+ alternateForm
                        typesDict[alternateForm] = getTypesFromXpath(currentFormXpath, 1)
                return typesDict
        
        #scaVio should be either foox for sword locations or fooy for shield locations
        def getLocations(scaVio):
            locations = []
            ScarletVioletXpath = response.xpath('//table[@class="dextable"]//tr[td[@class="fooevo"][h2[contains(text(),"Location")]]]/following-sibling::tr[td[@class="{}"]][1]//td[@class = "fooinfo"]'.format(scaVio))
            linkedLocations = ScarletVioletXpath.xpath('.//a/text()').extract()
            unlinkedLocations = ScarletVioletXpath.xpath('./text()').extract()
            #If there's no links inside the xpath
            if not linkedLocations:   
                   locations = locations + unlinkedLocations
                   return locations
            else:
                locations = locations + linkedLocations
                locations = list(set(locations))
                return locations



        scarletLocations = getLocations("scarlet")
        violetLocations = getLocations("violet")
        typesDict = buildTypesDict()
        DexTables = Selector(response).xpath('//table[@class="dextable"]')
        AllMoves = Selector(response).xpath('//table[@class="dextable"]//td[@class="fooinfo"]//a[contains(@href,"attackdex")]//text()').extract()
        EggGroups = Selector(response).xpath('//td[@align="center"]//table[@class="dexitem"]//a/text()').extract()
        EggMoves = Selector(response).xpath('//tr[*//a[@name="eggmoves"]]/following-sibling::tr//td[@class="fooinfo"]//a/text()').extract()
        AbilitiesList = response.xpath('//table[@class="dextable"]//td[@class="fooinfo"]//a[contains(@href, "abilitydex")]//text()').extract()
        item = PokemonscrapingItem()
        item['name'] = response.xpath('//table[@class="dextable"][2]//td[@class="fooinfo"]/text()').extract()[0]
        item['number'] = response.xpath('//tr[td[*[contains(text(), "National")]]]//td/text()').extract()[1].replace("#","")
        item['weight'] = weightParse(response.xpath('//table[@class="dextable"]//td[contains(text(), "lbs")]/text()'))
        item['types'] = typesDict
        item['egg_group'] = EggGroups
        item['egg_moves'] = EggMoves
        item['locations_scarlet'] = scarletLocations
        item['locations_violet'] = violetLocations
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

