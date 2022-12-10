from scrapy import Spider
from scrapy import Request
from scrapy.selector import Selector
from pokemonscraping.items import PokemonscrapingItem
import re


class PokeSpider(Spider):
    name = "pokespider"
    allowed_domains = ["serebii.net"]
    current_link_index = 0
    start_urls = [
    "https://www.serebii.net//pokedex-sv/sprigatito/",
    "https://www.serebii.net//pokedex-sv/floragato/",
    "https://www.serebii.net//pokedex-sv/meowscarada/",
    "https://www.serebii.net//pokedex-sv/fuecoco/",
    "https://www.serebii.net//pokedex-sv/crocalor/",
    "https://www.serebii.net//pokedex-sv/skeledirge/",
    "https://www.serebii.net//pokedex-sv/quaxly/",
    "https://www.serebii.net//pokedex-sv/quaxwell/",
    "https://www.serebii.net//pokedex-sv/quaquaval/",
    "https://www.serebii.net//pokedex-sv/lechonk/",
    "https://www.serebii.net//pokedex-sv/oinkologne/",
    "https://www.serebii.net//pokedex-sv/tarountula/",
    "https://www.serebii.net//pokedex-sv/spidops/",
    "https://www.serebii.net//pokedex-sv/nymble/",
    "https://www.serebii.net//pokedex-sv/lokix/",
    "https://www.serebii.net//pokedex-sv/hoppip/",
    "https://www.serebii.net//pokedex-sv/skiploom/",
    "https://www.serebii.net//pokedex-sv/jumpluff/",
    "https://www.serebii.net//pokedex-sv/fletchling/",
    "https://www.serebii.net//pokedex-sv/fletchinder/",
    "https://www.serebii.net//pokedex-sv/talonflame/",
    "https://www.serebii.net//pokedex-sv/pawmi/",
    "https://www.serebii.net//pokedex-sv/pawmo/",
    "https://www.serebii.net//pokedex-sv/pawmot/",
    "https://www.serebii.net//pokedex-sv/houndour/",
    "https://www.serebii.net//pokedex-sv/houndoom/",
    "https://www.serebii.net//pokedex-sv/yungoos/",
    "https://www.serebii.net//pokedex-sv/gumshoos/",
    "https://www.serebii.net//pokedex-sv/skwovet/",
    "https://www.serebii.net//pokedex-sv/greedent/",
    "https://www.serebii.net//pokedex-sv/sunkern/",
    "https://www.serebii.net//pokedex-sv/sunflora/",
    "https://www.serebii.net//pokedex-sv/kricketot/",
    "https://www.serebii.net//pokedex-sv/kricketune/",
    "https://www.serebii.net//pokedex-sv/scatterbug/",
    "https://www.serebii.net//pokedex-sv/spewpa/",
    "https://www.serebii.net//pokedex-sv/vivillon/",
    "https://www.serebii.net//pokedex-sv/combee/",
    "https://www.serebii.net//pokedex-sv/vespiquen/",
    "https://www.serebii.net//pokedex-sv/rookidee/",
    "https://www.serebii.net//pokedex-sv/corvisquire/",
    "https://www.serebii.net//pokedex-sv/corviknight/",
    "https://www.serebii.net//pokedex-sv/happiny/",
    "https://www.serebii.net//pokedex-sv/chansey/",
    "https://www.serebii.net//pokedex-sv/blissey/",
    "https://www.serebii.net//pokedex-sv/azurill/",
    "https://www.serebii.net//pokedex-sv/marill/",
    "https://www.serebii.net//pokedex-sv/azumarill/",
    "https://www.serebii.net//pokedex-sv/surskit/",
    "https://www.serebii.net//pokedex-sv/masquerain/",
    "https://www.serebii.net//pokedex-sv/buizel/",
    "https://www.serebii.net//pokedex-sv/floatzel/",
    "https://www.serebii.net//pokedex-sv/wooper/",
    "https://www.serebii.net//pokedex-sv/clodsire/",
    "https://www.serebii.net//pokedex-sv/psyduck/",
    "https://www.serebii.net//pokedex-sv/golduck/",
    "https://www.serebii.net//pokedex-sv/chewtle/",
    "https://www.serebii.net//pokedex-sv/drednaw/",
    "https://www.serebii.net//pokedex-sv/igglybuff/",
    "https://www.serebii.net//pokedex-sv/jigglypuff/",
    "https://www.serebii.net//pokedex-sv/wigglytuff/",
    "https://www.serebii.net//pokedex-sv/ralts/",
    "https://www.serebii.net//pokedex-sv/kirlia/",
    "https://www.serebii.net//pokedex-sv/gardevoir/",
    "https://www.serebii.net//pokedex-sv/gallade/",
    "https://www.serebii.net//pokedex-sv/drowzee/",
    "https://www.serebii.net//pokedex-sv/hypno/",
    "https://www.serebii.net//pokedex-sv/gastly/",
    "https://www.serebii.net//pokedex-sv/haunter/",
    "https://www.serebii.net//pokedex-sv/gengar/",
    "https://www.serebii.net//pokedex-sv/tandemaus/",
    "https://www.serebii.net//pokedex-sv/maushold/",
    "https://www.serebii.net//pokedex-sv/pichu/",
    "https://www.serebii.net//pokedex-sv/pikachu/",
    "https://www.serebii.net//pokedex-sv/raichu/",
    "https://www.serebii.net//pokedex-sv/fidough/",
    "https://www.serebii.net//pokedex-sv/dachsbun/",
    "https://www.serebii.net//pokedex-sv/slakoth/",
    "https://www.serebii.net//pokedex-sv/vigoroth/",
    "https://www.serebii.net//pokedex-sv/slaking/",
    "https://www.serebii.net//pokedex-sv/bounsweet/",
    "https://www.serebii.net//pokedex-sv/steenee/",
    "https://www.serebii.net//pokedex-sv/tsareena/",
    "https://www.serebii.net//pokedex-sv/smoliv/",
    "https://www.serebii.net//pokedex-sv/dolliv/",
    "https://www.serebii.net//pokedex-sv/arboliva/",
    "https://www.serebii.net//pokedex-sv/bonsly/",
    "https://www.serebii.net//pokedex-sv/sudowoodo/",
    "https://www.serebii.net//pokedex-sv/rockruff/",
    "https://www.serebii.net//pokedex-sv/lycanroc/",
    "https://www.serebii.net//pokedex-sv/rolycoly/",
    "https://www.serebii.net//pokedex-sv/carkol/",
    "https://www.serebii.net//pokedex-sv/coalossal/",
    "https://www.serebii.net//pokedex-sv/shinx/",
    "https://www.serebii.net//pokedex-sv/luxio/",
    "https://www.serebii.net//pokedex-sv/luxray/",
    "https://www.serebii.net//pokedex-sv/starly/",
    "https://www.serebii.net//pokedex-sv/staravia/",
    "https://www.serebii.net//pokedex-sv/staraptor/",
    "https://www.serebii.net//pokedex-sv/oricorio/",
    "https://www.serebii.net//pokedex-sv/mareep/",
    "https://www.serebii.net//pokedex-sv/flaaffy/",
    "https://www.serebii.net//pokedex-sv/ampharos/",
    "https://www.serebii.net//pokedex-sv/petilil/",
    "https://www.serebii.net//pokedex-sv/lilligant/",
    "https://www.serebii.net//pokedex-sv/shroomish/",
    "https://www.serebii.net//pokedex-sv/breloom/",
    "https://www.serebii.net//pokedex-sv/applin/",
    "https://www.serebii.net//pokedex-sv/flapple/",
    "https://www.serebii.net//pokedex-sv/appletun/",
    "https://www.serebii.net//pokedex-sv/spoink/",
    "https://www.serebii.net//pokedex-sv/grumpig/",
    "https://www.serebii.net//pokedex-sv/squawkabilly/",
    "https://www.serebii.net//pokedex-sv/misdreavus/",
    "https://www.serebii.net//pokedex-sv/mismagius/",
    "https://www.serebii.net//pokedex-sv/makuhita/",
    "https://www.serebii.net//pokedex-sv/hariyama/",
    "https://www.serebii.net//pokedex-sv/crabrawler/",
    "https://www.serebii.net//pokedex-sv/crabominable/",
    "https://www.serebii.net//pokedex-sv/salandit/",
    "https://www.serebii.net//pokedex-sv/salazzle/",
    "https://www.serebii.net//pokedex-sv/phanpy/",
    "https://www.serebii.net//pokedex-sv/donphan/",
    "https://www.serebii.net//pokedex-sv/cufant/",
    "https://www.serebii.net//pokedex-sv/copperajah/",
    "https://www.serebii.net//pokedex-sv/gible/",
    "https://www.serebii.net//pokedex-sv/gabite/",
    "https://www.serebii.net//pokedex-sv/garchomp/",
    "https://www.serebii.net//pokedex-sv/nacli/",
    "https://www.serebii.net//pokedex-sv/naclstack/",
    "https://www.serebii.net//pokedex-sv/garganacl/",
    "https://www.serebii.net//pokedex-sv/wingull/",
    "https://www.serebii.net//pokedex-sv/pelipper/",
    "https://www.serebii.net//pokedex-sv/magikarp/",
    "https://www.serebii.net//pokedex-sv/gyarados/",
    "https://www.serebii.net//pokedex-sv/arrokuda/",
    "https://www.serebii.net//pokedex-sv/barraskewda/",
    "https://www.serebii.net//pokedex-sv/basculin/",
    "https://www.serebii.net//pokedex-sv/gulpin/",
    "https://www.serebii.net//pokedex-sv/swalot/",
    "https://www.serebii.net//pokedex-sv/meowth/",
    "https://www.serebii.net//pokedex-sv/persian/",
    "https://www.serebii.net//pokedex-sv/drifloon/",
    "https://www.serebii.net//pokedex-sv/drifblim/",
    "https://www.serebii.net//pokedex-sv/flabebe/",
    "https://www.serebii.net//pokedex-sv/floette/",
    "https://www.serebii.net//pokedex-sv/florges/",
    "https://www.serebii.net//pokedex-sv/diglett/",
    "https://www.serebii.net//pokedex-sv/dugtrio/",
    "https://www.serebii.net//pokedex-sv/torkoal/",
    "https://www.serebii.net//pokedex-sv/numel/",
    "https://www.serebii.net//pokedex-sv/camerupt/",
    "https://www.serebii.net//pokedex-sv/bronzor/",
    "https://www.serebii.net//pokedex-sv/bronzong/",
    "https://www.serebii.net//pokedex-sv/axew/",
    "https://www.serebii.net//pokedex-sv/fraxure/",
    "https://www.serebii.net//pokedex-sv/haxorus/",
    "https://www.serebii.net//pokedex-sv/mankey/",
    "https://www.serebii.net//pokedex-sv/primeape/",
    "https://www.serebii.net//pokedex-sv/annihilape/",
    "https://www.serebii.net//pokedex-sv/meditite/",
    "https://www.serebii.net//pokedex-sv/medicham/",
    "https://www.serebii.net//pokedex-sv/riolu/",
    "https://www.serebii.net//pokedex-sv/lucario/",
    "https://www.serebii.net//pokedex-sv/charcadet/",
    "https://www.serebii.net//pokedex-sv/armarouge/",
    "https://www.serebii.net//pokedex-sv/ceruledge/",
    "https://www.serebii.net//pokedex-sv/barboach/",
    "https://www.serebii.net//pokedex-sv/whiscash/",
    "https://www.serebii.net//pokedex-sv/tadbulb/",
    "https://www.serebii.net//pokedex-sv/bellibolt/",
    "https://www.serebii.net//pokedex-sv/goomy/",
    "https://www.serebii.net//pokedex-sv/sliggoo/",
    "https://www.serebii.net//pokedex-sv/goodra/",
    "https://www.serebii.net//pokedex-sv/croagunk/",
    "https://www.serebii.net//pokedex-sv/toxicroak/",
    "https://www.serebii.net//pokedex-sv/wattrel/",
    "https://www.serebii.net//pokedex-sv/kilowattrel/",
    "https://www.serebii.net//pokedex-sv/eevee/",
    "https://www.serebii.net//pokedex-sv/vaporeon/",
    "https://www.serebii.net//pokedex-sv/jolteon/",
    "https://www.serebii.net//pokedex-sv/flareon/",
    "https://www.serebii.net//pokedex-sv/espeon/",
    "https://www.serebii.net//pokedex-sv/umbreon/",
    "https://www.serebii.net//pokedex-sv/leafeon/",
    "https://www.serebii.net//pokedex-sv/glaceon/",
    "https://www.serebii.net//pokedex-sv/sylveon/",
    "https://www.serebii.net//pokedex-sv/dunsparce/",
    "https://www.serebii.net//pokedex-sv/dudunsparce/",
    "https://www.serebii.net//pokedex-sv/deerling/",
    "https://www.serebii.net//pokedex-sv/sawsbuck/",
    "https://www.serebii.net//pokedex-sv/girafarig/",
    "https://www.serebii.net//pokedex-sv/farigiraf/",
    "https://www.serebii.net//pokedex-sv/grimer/",
    "https://www.serebii.net//pokedex-sv/muk/",
    "https://www.serebii.net//pokedex-sv/maschiff/",
    "https://www.serebii.net//pokedex-sv/mabosstiff/",
    "https://www.serebii.net//pokedex-sv/toxel/",
    "https://www.serebii.net//pokedex-sv/toxtricity/",
    "https://www.serebii.net//pokedex-sv/dedenne/",
    "https://www.serebii.net//pokedex-sv/pachirisu/",
    "https://www.serebii.net//pokedex-sv/shroodle/",
    "https://www.serebii.net//pokedex-sv/grafaiai/",
    "https://www.serebii.net//pokedex-sv/stantler/",
    "https://www.serebii.net//pokedex-sv/foongus/",
    "https://www.serebii.net//pokedex-sv/amoonguss/",
    "https://www.serebii.net//pokedex-sv/voltorb/",
    "https://www.serebii.net//pokedex-sv/electrode/",
    "https://www.serebii.net//pokedex-sv/magnemite/",
    "https://www.serebii.net//pokedex-sv/magneton/",
    "https://www.serebii.net//pokedex-sv/magnezone/",
    "https://www.serebii.net//pokedex-sv/ditto/",
    "https://www.serebii.net//pokedex-sv/growlithe/",
    "https://www.serebii.net//pokedex-sv/arcanine/",
    "https://www.serebii.net//pokedex-sv/teddiursa/",
    "https://www.serebii.net//pokedex-sv/ursaring/",
    "https://www.serebii.net//pokedex-sv/zangoose/",
    "https://www.serebii.net//pokedex-sv/seviper/",
    "https://www.serebii.net//pokedex-sv/swablu/",
    "https://www.serebii.net//pokedex-sv/altaria/",
    "https://www.serebii.net//pokedex-sv/skiddo/",
    "https://www.serebii.net//pokedex-sv/gogoat/",
    "https://www.serebii.net//pokedex-sv/tauros/",
    "https://www.serebii.net//pokedex-sv/litleo/",
    "https://www.serebii.net//pokedex-sv/pyroar/",
    "https://www.serebii.net//pokedex-sv/stunky/",
    "https://www.serebii.net//pokedex-sv/skuntank/",
    "https://www.serebii.net//pokedex-sv/zorua/",
    "https://www.serebii.net//pokedex-sv/zoroark/",
    "https://www.serebii.net//pokedex-sv/sneasel/",
    "https://www.serebii.net//pokedex-sv/weavile/",
    "https://www.serebii.net//pokedex-sv/murkrow/",
    "https://www.serebii.net//pokedex-sv/honchkrow/",
    "https://www.serebii.net//pokedex-sv/gothita/",
    "https://www.serebii.net//pokedex-sv/gothorita/",
    "https://www.serebii.net//pokedex-sv/gothitelle/",
    "https://www.serebii.net//pokedex-sv/sinistea/",
    "https://www.serebii.net//pokedex-sv/polteageist/",
    "https://www.serebii.net//pokedex-sv/mimikyu/",
    "https://www.serebii.net//pokedex-sv/klefki/",
    "https://www.serebii.net//pokedex-sv/indeedee/",
    "https://www.serebii.net//pokedex-sv/bramblin/",
    "https://www.serebii.net//pokedex-sv/brambleghast/",
    "https://www.serebii.net//pokedex-sv/toedscool/",
    "https://www.serebii.net//pokedex-sv/toedscruel/",
    "https://www.serebii.net//pokedex-sv/tropius/",
    "https://www.serebii.net//pokedex-sv/fomantis/",
    "https://www.serebii.net//pokedex-sv/lurantis/",
    "https://www.serebii.net//pokedex-sv/klawf/",
    "https://www.serebii.net//pokedex-sv/capsakid/",
    "https://www.serebii.net//pokedex-sv/scovillain/",
    "https://www.serebii.net//pokedex-sv/cacnea/",
    "https://www.serebii.net//pokedex-sv/cacturne/",
    "https://www.serebii.net//pokedex-sv/rellor/",
    "https://www.serebii.net//pokedex-sv/rabsca/",
    "https://www.serebii.net//pokedex-sv/venonat/",
    "https://www.serebii.net//pokedex-sv/venomoth/",
    "https://www.serebii.net//pokedex-sv/pineco/",
    "https://www.serebii.net//pokedex-sv/forretress/",
    "https://www.serebii.net//pokedex-sv/scyther/",
    "https://www.serebii.net//pokedex-sv/scizor/",
    "https://www.serebii.net//pokedex-sv/heracross/",
    "https://www.serebii.net//pokedex-sv/flittle/",
    "https://www.serebii.net//pokedex-sv/espathra/",
    "https://www.serebii.net//pokedex-sv/hippopotas/",
    "https://www.serebii.net//pokedex-sv/hippowdon/",
    "https://www.serebii.net//pokedex-sv/sandile/",
    "https://www.serebii.net//pokedex-sv/krokorok/",
    "https://www.serebii.net//pokedex-sv/krookodile/",
    "https://www.serebii.net//pokedex-sv/silicobra/",
    "https://www.serebii.net//pokedex-sv/sandaconda/",
    "https://www.serebii.net//pokedex-sv/mudbray/",
    "https://www.serebii.net//pokedex-sv/mudsdale/",
    "https://www.serebii.net//pokedex-sv/larvesta/",
    "https://www.serebii.net//pokedex-sv/volcarona/",
    "https://www.serebii.net//pokedex-sv/bagon/",
    "https://www.serebii.net//pokedex-sv/shelgon/",
    "https://www.serebii.net//pokedex-sv/salamence/",
    "https://www.serebii.net//pokedex-sv/tinkatink/",
    "https://www.serebii.net//pokedex-sv/tinkatuff/",
    "https://www.serebii.net//pokedex-sv/tinkaton/",
    "https://www.serebii.net//pokedex-sv/hatenna/",
    "https://www.serebii.net//pokedex-sv/hattrem/",
    "https://www.serebii.net//pokedex-sv/hatterene/",
    "https://www.serebii.net//pokedex-sv/impidimp/",
    "https://www.serebii.net//pokedex-sv/morgrem/",
    "https://www.serebii.net//pokedex-sv/grimmsnarl/",
    "https://www.serebii.net//pokedex-sv/wiglett/",
    "https://www.serebii.net//pokedex-sv/wugtrio/",
    "https://www.serebii.net//pokedex-sv/bombirdier/",
    "https://www.serebii.net//pokedex-sv/finizen/",
    "https://www.serebii.net//pokedex-sv/palafin/",
    "https://www.serebii.net//pokedex-sv/varoom/",
    "https://www.serebii.net//pokedex-sv/revavroom/",
    "https://www.serebii.net//pokedex-sv/cyclizar/",
    "https://www.serebii.net//pokedex-sv/orthworm/",
    "https://www.serebii.net//pokedex-sv/sableye/",
    "https://www.serebii.net//pokedex-sv/shuppet/",
    "https://www.serebii.net//pokedex-sv/banette/",
    "https://www.serebii.net//pokedex-sv/falinks/",
    "https://www.serebii.net//pokedex-sv/hawlucha/",
    "https://www.serebii.net//pokedex-sv/spiritomb/",
    "https://www.serebii.net//pokedex-sv/noibat/",
    "https://www.serebii.net//pokedex-sv/noivern/",
    "https://www.serebii.net//pokedex-sv/dreepy/",
    "https://www.serebii.net//pokedex-sv/drakloak/",
    "https://www.serebii.net//pokedex-sv/dragapult/",
    "https://www.serebii.net//pokedex-sv/glimmet/",
    "https://www.serebii.net//pokedex-sv/glimmora/",
    "https://www.serebii.net//pokedex-sv/rotom/",
    "https://www.serebii.net//pokedex-sv/greavard/",
    "https://www.serebii.net//pokedex-sv/houndstone/",
    "https://www.serebii.net//pokedex-sv/oranguru/",
    "https://www.serebii.net//pokedex-sv/passimian/",
    "https://www.serebii.net//pokedex-sv/komala/",
    "https://www.serebii.net//pokedex-sv/larvitar/",
    "https://www.serebii.net//pokedex-sv/pupitar/",
    "https://www.serebii.net//pokedex-sv/tyranitar/",
    "https://www.serebii.net//pokedex-sv/stonjourner/",
    "https://www.serebii.net//pokedex-sv/eiscue/",
    "https://www.serebii.net//pokedex-sv/pincurchin/",
    "https://www.serebii.net//pokedex-sv/sandygast/",
    "https://www.serebii.net//pokedex-sv/palossand/",
    "https://www.serebii.net//pokedex-sv/slowpoke/",
    "https://www.serebii.net//pokedex-sv/slowbro/",
    "https://www.serebii.net//pokedex-sv/slowking/",
    "https://www.serebii.net//pokedex-sv/shellos/",
    "https://www.serebii.net//pokedex-sv/gastrodon/",
    "https://www.serebii.net//pokedex-sv/shellder/",
    "https://www.serebii.net//pokedex-sv/cloyster/",
    "https://www.serebii.net//pokedex-sv/qwilfish/",
    "https://www.serebii.net//pokedex-sv/luvdisc/",
    "https://www.serebii.net//pokedex-sv/finneon/",
    "https://www.serebii.net//pokedex-sv/lumineon/",
    "https://www.serebii.net//pokedex-sv/bruxish/",
    "https://www.serebii.net//pokedex-sv/alomomola/",
    "https://www.serebii.net//pokedex-sv/skrelp/",
    "https://www.serebii.net//pokedex-sv/dragalge/",
    "https://www.serebii.net//pokedex-sv/clauncher/",
    "https://www.serebii.net//pokedex-sv/clawitzer/",
    "https://www.serebii.net//pokedex-sv/tynamo/",
    "https://www.serebii.net//pokedex-sv/eelektrik/",
    "https://www.serebii.net//pokedex-sv/eelektross/",
    "https://www.serebii.net//pokedex-sv/mareanie/",
    "https://www.serebii.net//pokedex-sv/toxapex/",
    "https://www.serebii.net//pokedex-sv/flamigo/",
    "https://www.serebii.net//pokedex-sv/dratini/",
    "https://www.serebii.net//pokedex-sv/dragonair/",
    "https://www.serebii.net//pokedex-sv/dragonite/",
    "https://www.serebii.net//pokedex-sv/snom/",
    "https://www.serebii.net//pokedex-sv/frosmoth/",
    "https://www.serebii.net//pokedex-sv/snover/",
    "https://www.serebii.net//pokedex-sv/abomasnow/",
    "https://www.serebii.net//pokedex-sv/delibird/",
    "https://www.serebii.net//pokedex-sv/cubchoo/",
    "https://www.serebii.net//pokedex-sv/beartic/",
    "https://www.serebii.net//pokedex-sv/snorunt/",
    "https://www.serebii.net//pokedex-sv/glalie/",
    "https://www.serebii.net//pokedex-sv/froslass/",
    "https://www.serebii.net//pokedex-sv/cryogonal/",
    "https://www.serebii.net//pokedex-sv/cetoddle/",
    "https://www.serebii.net//pokedex-sv/cetitan/",
    "https://www.serebii.net//pokedex-sv/bergmite/",
    "https://www.serebii.net//pokedex-sv/avalugg/",
    "https://www.serebii.net//pokedex-sv/rufflet/",
    "https://www.serebii.net//pokedex-sv/braviary/",
    "https://www.serebii.net//pokedex-sv/pawniard/",
    "https://www.serebii.net//pokedex-sv/bisharp/",
    "https://www.serebii.net//pokedex-sv/kingambit/",
    "https://www.serebii.net//pokedex-sv/deino/",
    "https://www.serebii.net//pokedex-sv/zweilous/",
    "https://www.serebii.net//pokedex-sv/hydreigon/",
    "https://www.serebii.net//pokedex-sv/veluza/",
    "https://www.serebii.net//pokedex-sv/dondozo/",
    "https://www.serebii.net//pokedex-sv/tatsugiri/",
    "https://www.serebii.net//pokedex-sv/greattusk/",
    "https://www.serebii.net//pokedex-sv/screamtail/",
    "https://www.serebii.net//pokedex-sv/brutebonnet/",
    "https://www.serebii.net//pokedex-sv/fluttermane/",
    "https://www.serebii.net//pokedex-sv/slitherwing/",
    "https://www.serebii.net//pokedex-sv/sandyshocks/",
    "https://www.serebii.net//pokedex-sv/irontreads/",
    "https://www.serebii.net//pokedex-sv/ironbundle/",
    "https://www.serebii.net//pokedex-sv/ironhands/",
    "https://www.serebii.net//pokedex-sv/ironjugulis/",
    "https://www.serebii.net//pokedex-sv/ironmoth/",
    "https://www.serebii.net//pokedex-sv/ironthorns/",
    "https://www.serebii.net//pokedex-sv/frigibax/",
    "https://www.serebii.net//pokedex-sv/arctibax/",
    "https://www.serebii.net//pokedex-sv/baxcalibur/",
    "https://www.serebii.net//pokedex-sv/gimmighoul/",
    "https://www.serebii.net//pokedex-sv/gholdengo/",
    "https://www.serebii.net//pokedex-sv/wo-chien/",
    "https://www.serebii.net//pokedex-sv/chien-pao/",
    "https://www.serebii.net//pokedex-sv/ting-lu/",
    "https://www.serebii.net//pokedex-sv/chi-yu/",
    "https://www.serebii.net//pokedex-sv/roaringmoon/",
    "https://www.serebii.net//pokedex-sv/ironvaliant/",
    "https://www.serebii.net//pokedex-sv/koraidon/",
    "https://www.serebii.net//pokedex-sv/miraidon/"
]



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
        
        #def getCrawlableLink(number):
        #    return f"https://www.serebii.net/{paldean_links[number]}"
        
        #def getNextLink():
        #    if self.current_link_index + 1 == len(paldean_links):
        #        return None
        #    self.current_link_index += 1
        #    return getCrawlableLink(self.current_link_index)



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
