"""

Basically holds information for every item it will trade lmao

Its 100% easier than puting it in a json or in a database (real)

"""

# Pets according to: https://growagarden.fandom.com/wiki/Pets#Mythical

pets={
    "common":[
        "starfish",
        "crab",
        "seagull",
        "bunny",
        "dog",
        "golden lab"
    ],
    "uncommon":[
        "bee",
        "black bunny",
        "cat",
        "chicken",
        "deer"
    ],
    "rare":[
        "monkey",
        "orange tabby",
        "pig",
        "rooster",
        "spotted deer",
        "flamingo",
        "toucan",
        "sea turtle",
        "orangutan",
        "seal",
        "honey bee",
        "wasp",
        "hedgehog",
        "kiwi"
    ],
    "legendary":[
        "tarantula hawk",
        "turtle",
        "petal bee",
        "moth",
        "moon cat",
        "frog",
        "mole",
        "scarlet macaw",
        "ostrich",
        "peacock",
        "capybara",
        "sand snake",
        "meerkat",
        "cow",
        "polar bear",
        "sea otter",
        "silver monkey",
        "panda",
        "blood hedgehog"
    ],
    "mythical":[
        "brown mouse",
        "caterpillar",
        "giant ant",
        "grey mouse",
        "praying mantis",
        "red fox",
        "red giant ant",
        "snail",
        "squirrel",
        "bear bee",
        "butterfly",
        "echo frog",
        "pack bee",
        "mimic octopus",
        "hyacinth macaw",
        "axolotl",
        "hamster",
        "blood kiwi",
        "chicken zombie",
        "firefly",
        "owl",
        "golden bee",
        "cooked owl"
    ],
    "divine":[
        "dragonfly",
        "night owl",
        "queen bee",
        "raccoon",
        "disco bee",
        "fennec fox",
        "blood owl"
    ],
    "unknown":[
        "red dragon"
    ]
}

# Gears according to: https://growagarden.fandom.com/wiki/Gears#Common

gears={
    "common":[
        "watering can" # idk if anyone would care lmao
    ],
    "uncommon":[
        "trowel",
        "recall wrench" # idk if you could even trade these lol
    ],
    "rare":[
        "basic sprinkler"
    ],
    "legendary":[
        "advanced sprinkler",
        "star caller",
        "night staff"
    ],
    "mythical":[
        "godly sprinkler",
        "chocolate sprinkler",
        "magnifying glass",
        "nectar staff",
        "pollen radar"
    ],
    "divine":[
        "master sprinkler",
        "cleaning spray",
        "favorite tool",
        "harvest tool", # should i even add this trash?
        "frienship pot",
        "honey sprinkler"
    ],
    "craftables":[
        "lightning rod",
        "berry bush sprinkler",
        "flower froster sprinkler",
        "spice spritzer sprinkler",
        "stalk sprout sprinkler",
        "sweet soaker sprinkler",
        "tropical mist sprinkler",
        "reclaimer"
    ]
}

# Fruits according to: https://growagarden.fandom.com/wiki/Crops
# Im calling it fruits because i aint no trading no seeds
# i got data by webscraping the wiki. can be found in _itemscraper

fruits={
    "common": {
        "carrot": {
            "weight": 0.28,
            "price": 20.0
        },
        "strawberry": {
            "weight": 0.3,
            "price": 20.0
        },
        "chocolate carrot": {
            "weight": 0.28,
            "price": 11000.0
        },
        "pink tulip": {
            "weight": 0.05,
            "price": 850.0
        }
    },
    "uncommon": {
        "blueberry": {
            "weight": 0.2,
            "price": 20.0
        },
        "wild carrot": {
            "weight": 0.3,
            "price": 25000.0
        },
        "rose": {
            "weight": 1.0,
            "price": 5000.0
        },
        "orange tulip": {
            "weight": 0.05,
            "price": 850.0
        },
        "red lollipop": {
            "weight": 4.0,
            "price": 50000.0
        },
        "nightshade": {
            "weight": 0.5,
            "price": 3500.0
        },
        "manuka flower": {
            "weight": 0.3,
            "price": 25000.0
        },
        "lavender": {
            "weight": 0.28,
            "price": 25000.0
        },
        "crocus": {
            "weight": 0.28,
            "price": 30000.0
        }
    },
    "rare": {
        "tomato": {
            "weight": 0.5,
            "price": 30.0
        },
        "cauliflower": {
            "weight": 5.0,
            "price": 40.0
        },
        "delphinium": {
            "weight": 0.36,
            "price": 24000.0
        },
        "peace lily": {
            "weight": 0.6,
            "price": 24000.0
        },
        "pear": {
            "weight": 3.0,
            "price": 20000.0
        },
        "raspberry": {
            "weight": 0.75,
            "price": 100.0
        },
        "corn": {
            "weight": 2.0,
            "price": 40.0
        },
        "daffodil": {
            "weight": 0.2,
            "price": 1000.0
        },
        "candy sunflower": {
            "weight": 1.5,
            "price": 80000.0
        },
        "mint": {
            "weight": 1.0,
            "price": 5250.0
        },
        "glowshroom": {
            "weight": 0.75,
            "price": 300.0
        },
        "dandelion": {
            "weight": 4.0,
            "price": 50000.0
        },
        "nectarshade": {
            "weight": 0.8,
            "price": 50000.0
        },
        "foxglove": {
            "weight": 2.0,
            "price": 20000.0
        },
        "succulent": {
            "weight": 5.0,
            "price": 25000.0
        },
        "bee balm": {
            "weight": 1.0,
            "price": 18000.0
        }
    },
    "legendary": {
        "watermelon": {
            "weight": 7.0,
            "price": 3000.0
        },
        "pumpkin": {
            "weight": 8.0,
            "price": 3400.0
        },
        "banana": {
            "weight": 1.5,
            "price": 1750.0
        },
        "aloe vera": {
            "weight": 5.5,
            "price": 69000.0
        },
        "avocado": {
            "weight": 6.5,
            "price": 350.0
        },
        "cantaloupe": {
            "weight": 5.5,
            "price": 34000.0
        },
        "rafflesia": {
            "weight": 10.0,
            "price": 5500.0
        },
        "green apple": {
            "weight": 3.0,
            "price": 300.0
        },
        "bamboo": {
            "weight": 4.0,
            "price": 4000.0
        },
        "cranberry": {
            "weight": 1.0,
            "price": 3500.0
        },
        "durian": {
            "weight": 8.0,
            "price": 7500.0
        },
        "moonflower": {
            "weight": 2.0,
            "price": 9500.0
        },
        "starfruit": {
            "weight": 3.0,
            "price": 15000.0
        },
        "papaya": {
            "weight": 3.0,
            "price": 1000.0
        },
        "lilac": {
            "weight": 3.0,
            "price": 35000.0
        },
        "lumira": {
            "weight": 6.0,
            "price": 85000.0
        },
        "violet corn": {
            "weight": 3.0,
            "price": 50000.0
        },
        "nectar thorn": {
            "weight": 7.0,
            "price": 40111.0
        }
    },
    "mythical": {
        "peach": {
            "weight": 2.0,
            "price": 300.0
        },
        "pineapple": {
            "weight": 3.0,
            "price": 2000.0
        },
        "moon melon": {
            "weight": 8.0,
            "price": 18000.0
        },
        "celestiberry": {
            "weight": 2.0,
            "price": 10000.0
        },
        "kiwi": {
            "weight": 5.0,
            "price": 2750.0
        },
        "guanabana": {
            "weight": 4.0,
            "price": 72440.0
        },
        "bell pepper": {
            "weight": 8.0,
            "price": 5500.0
        },
        "prickly pear": {
            "weight": 7.0,
            "price": 7000.0
        },
        "parasol flower": {
            "weight": 6.0,
            "price": 200000.0
        },
        "cactus": {
            "weight": 7.0,
            "price": 3400.0
        },
        "lily of the valley": {
            "weight": 6.0,
            "price": 49120.0
        },
        "dragon fruit": {
            "weight": 12.0,
            "price": 4750.0
        },
        "easter egg": {
            "weight": 3.0,
            "price": 2500.0
        },
        "moon mango": {
            "weight": 15.0,
            "price": 50.0
        },
        "mango": {
            "weight": 15.0,
            "price": 6500.0
        },
        "coconut": {
            "weight": 14.0,
            "price": 400.0
        },
        "blood banana": {
            "weight": 1.5,
            "price": 6000.0
        },
        "moonglow": {
            "weight": 7.0,
            "price": 25000.0
        },
        "eggplant": {
            "weight": 5.0,
            "price": 12000.0
        },
        "passionfruit": {
            "weight": 3.0,
            "price": 3550.0
        },
        "lemon": {
            "weight": 1.0,
            "price": 350.0
        },
        "honeysuckle": {
            "weight": 12.0,
            "price": 100000.0
        },
        "nectarine": {
            "weight": 3.0,
            "price": 48000.0
        },
        "pink lily": {
            "weight": 6.0,
            "price": 65000.0
        },
        "purple dahlia": {
            "weight": 12.0,
            "price": 75000.0
        },
        "bendboo": {
            "weight": 18.0,
            "price": 155000.0
        },
        "cocovine": {
            "weight": 14.0,
            "price": 66666.0
        },
        "ice cream bean": {
            "weight": 4.0,
            "price": 4500.0
        },
        "lime": {
            "weight": 1.0,
            "price": 350.0
        }
    },
    "divine": {
        "loquat": {
            "weight": 6.5,
            "price": 8000.0
        },
        "feijoa": {
            "weight": 10.0,
            "price": 13000.0
        },
        "pitcher plant": {
            "weight": 12.0,
            "price": 32000.0
        },
        "traveler's fruit": {
            "weight": 15.0,
            "price": 70000.
        },
        "rosy delight": {
            "weight": 10.0,
            "price": 69000.0
        },
        "pepper": {
            "weight": 5.0,
            "price": 8000.0
        },
        "cacao": {
            "weight": 8.0,
            "price": 12000.0
        },
        "grape": {
            "weight": 3.0,
            "price": 7850.0
        },
        "mushroom": {
            "weight": 25.0,
            "price": 151000.0
        },
        "cherry blossom": {
            "weight": 3.0,
            "price": 500.0
        },
        "crimson vine": {
            "weight": 1.0,
            "price": 1250.0
        },
        "candy blossom": {
            "weight": 3.0,
            "price": 100000.0
        },
        "lotus": {
            "weight": 20.0,
            "price": 35000.0
        },
        "venus fly trap": {
            "weight": 10.0,
            "price": 85000.0
        },
        "cursed fruit": {
            "weight": 30.0,
            "price": 25570.0
        },
        "soul fruit": {
            "weight": 25.0,
            "price": 7750.0
        },
        "mega mushroom": {
            "weight": 70.0,
            "price": 500.0
        },
        "moon blossom": {
            "weight": 3.0,
            "price": 66666.0
        },
        "hive fruit": {
            "weight": 8.0,
            "price": 62000.0
        },
        "sunflower": {
            "weight": 16.5,
            "price": 160000.0
        },
        "dragon pepper": {
            "weight": 6.0,
            "price": 81000.0
        }
    },
    "prismatic": {
        "sugar apple": {
            "weight": 9.0,
            "price": 50000.0
        },
        "ember lily": {
            "weight": 12.0,
            "price": 66666.0
        },
        "elephant ears": {
            "weight": 18.0,
            "price": 77000.0
        },
        "beanstalk": {
            "weight": 10.0,
            "price": 28000.0
        }
    },
    "unknown": {
        "noble flower": {
            "weight": 5.0,
            "price": 20000.0
        },
        "blue lollipop": {
            "weight": 1.0,
            "price": 50000.0
        },
        "burning bud": {
            "weight": 15.0,
            "price": 135375.0
        },
        "purple cabbage": {
            "weight": 5.0,
            "price": 500.0
        }
    }
}

# mutations according to: https://www.pockettactics.com/grow-a-garden-mutations
# format is: "mutation":<multiplier>

mutations={
    "growth":{
        "ripe": 1,
        "gold": 20,
        "rainbow": 50,
    },
    "environtment":{
        "wet": 2,
        "windstruck": 2,
        "moonlit": 2,
        "chilled": 2,
        "choc": 2,
        "bloodlit": 4,
        "twisted": 5,
        "drenched": 5,
        "frozen": 10,
        "aurora": 90,
        "shocked": 100,
        "celestial": 120,
        "pollinated": 3,
        "burnt": 4,
        "verdant": 4,
        "wiltproof": 4,
        "cloudtouched": 5,
        "honey glazed": 5,
        "heavenly": 5,
        "fried": 8,
        "cooked": 25,
        "zombified": 25,
        "molten": 25,
        "sundried": 85,
        "paradisal": 100,
        "alienlike": 100,
        "galactic": 120,
        "disco": 125,
        "voidtouched": 135,
        "plasma": 150,
        "dawnbound": 150,
        "starised": 230
    }
}


