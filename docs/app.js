const GalarTypes = './GalarTypes.json';
//const GalarTypes = 'https://gist.githubusercontent.com/KeagenT/bb1ff135bbb08b16407cddb4f1b9b189/raw/1bac6c628bb715861c3aab3c227c4ab2959b1ed2/Types.json';
const GalarLocations = './GalarLocations.json';
//const GalarLocations = 'https://gist.githubusercontent.com/KeagenT/bb1ff135bbb08b16407cddb4f1b9b189/raw/1bac6c628bb715861c3aab3c227c4ab2959b1ed2/Locations.json';
var typesArray = ["Water","Steel", "Bug", "Grass", "Electric", "Fire", "Fighting", "Ghost", "Psychic"];

async function getD3Data(typesArray) {
    let locations = await fetch(GalarLocations);
    let locationsJSON = await locations.json();
    let types = await fetch(GalarTypes);
    let typesJSON = await types.json()

            
    function getIsPokemonType(pokemon, typesObject, type){
        for(let mon of typesObject[type]["pokemon"]){
            if(mon === pokemon) {
                return 1;
            }

        }
        return 0; 
    };


    function getTotalTypeAtLocation(type, locationObject, game){
        let totalOfType = 0;
        if(game ==="sword"){
            let swordArray = locationObject["sword_pokemon"];
            for(let pokemon of swordArray){
                totalOfType += getIsPokemonType(pokemon, typesJSON, type);
            }
            return totalOfType;
        }
        if(game ==="shield"){
            for(let pokemon of locationObject["shield_pokemon"]){
                totalOfType += getIsPokemonType(pokemon, typesJSON, type);
            }
            return totalOfType;
        }
    };
    let game = "sword"
    function getTotalTypesAllLocations(type, locationsObject, game){
        let typesObject = {};
        for(let [key, location] of Object.entries(locationsObject)){
            let locString = location["location"];
            let typesAt = getTotalTypeAtLocation(type, location, game);
            typesObject[locString] = typesAt;
            typesObject["type"] = type;
        }
        return typesObject;
    };

    function getPlottableStandard(type){
        let plottable = [];
        let totalTypesObject = getTotalTypesAllLocations(type, locationsJSON, game);
        for(let [location, totalType] of Object.entries(totalTypesObject)){
            let currentLocation = {};
            let pokemonTypeKey = totalTypesObject.type;
            if(location !== "type"){
                currentLocation["location"] = location;
                currentLocation["type"] = pokemonTypeKey;
                currentLocation[pokemonTypeKey] = totalType;
                plottable.push(currentLocation);
            }
        }
        return plottable;
    }
    //An incredibly slow join reduce for two arrays of objects
    function joinPlottable(plottableA, plottableB){
        for(let locationA of plottableA){
            delete locationA.type;
            locationA.location = locationA.location;
            for(let locationB of plottableB){
                let BtypeKey = locationB.type;
                let BCount = locationB[BtypeKey];
                if(locationB.location === locationA.location){
                    locationA[BtypeKey] = BCount;
                }
            }
        }
        return plottableA;
    }

    function getPlottableStacked(typesArray){
        plottableArray = []
        for(let type of typesArray){
            let typePlottable = getPlottableStandard(type);
            plottableArray.push(typePlottable);
        }
        plottableArray = plottableArray.reduce(joinPlottable);
        for(let location of plottableArray){
            let total = 0;
            for(let [key, value] of Object.entries(location)){
                if(key!== "location"){
                    total+= value;
                };
            };
        location["total"] = total;
        }
        plottableArray.columns = [];
        for(key of Object.keys(plottableArray[0])){
            if(key!=="total"){
                plottableArray.columns.push(key)
            }
        }
        return plottableArray;
    }

    return getPlottableStacked(typesArray);
};


//Doesn't actually get used except to see which type is most common for plotting a sample graph
function getTotalForEachTypes(typesObject){
    let typesObjectOutput = {};
    for(let[key, type] of Object.entries(typesObject)){
        let typeString = type["type"];
        //One line reduce total of a certain type using earlier function. It's totally wasteful.
        typesObjectOutput[typeString] = Object.values(getTotalTypesAllLocations(key,locationsJSON, game)).reduce((total, val) =>  total + parseInt(val));
    }
    return typesObjectOutput;
}
//Shows the pokemon ranked by sum of catcheable type at each location
function rankedTypes(typesObject){
    const sorted = Object.entries(getTotalForEachTypes(typesObject))
    .sort(([,a],[,b]) => a-b);
    return sorted.reverse();
}