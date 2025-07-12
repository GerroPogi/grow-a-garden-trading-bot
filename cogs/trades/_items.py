"""

Basically holds information for every item it will trade lmao

Its 100% easier than puting it in a json or in a database (real)

"""

# Pets according to: https://growagarden.fandom.com/wiki/Pets#Mythical

pets={
    "common": [
        "bunny",
        "crab",
        "dog",
        "golden lab",
        "hedgehog",
        "kiwi",
        "seagull",
        "starfish"
    ],
    "uncommon": [
        "bald eagle",
        "bee",
        "black bunny",
        "blood hedgehog",
        "cat",
        "chicken",
        "cow",
        "deer",
        "frog",
        "mole",
        "moon cat",
        "panda",
        "polar bear",
        "sea otter",
        "silver monkey"
    ],
    "rare": [
        "blood kiwi",
        "chicken zombie",
        "cooked owl",
        "echo frog",
        "firefly",
        "flamingo",
        "golden bee",
        "hamster",
        "honey bee",
        "monkey",
        "night owl",
        "orange tabby",
        "orangutan",
        "owl",
        "pig",
        "rooster",
        "sea turtle",
        "seal",
        "spotted deer",
        "toucan",
        "wasp"
    ],
    "legendary": [
        "blood owl",
        "capybara",
        "caterpillar",
        "meerkat",
        "moth",
        "ostrich",
        "peacock",
        "petal bee",
        "pterodactyl",
        "raccoon",
        "raptor",
        "sand snake",
        "scarlet macaw",
        "stegosaurus",
        "tarantula hawk",
        "triceratops",
        "turtle"
    ],
    "mythical": [
        "axolotl",
        "bear bee",
        "brontosaurus",
        "brown mouse",
        "butterfly",
        "giant ant",
        "grey mouse",
        "hyacinth macaw",
        "mimic octopus",
        "pack bee",
        "praying mantis",
        "red dragon",
        "red giant ant",
        "snail",
        "squirrel"
    ],
    "divine": [
        "disco bee",
        "dragonfly",
        "fennec fox",
        "queen bee (pet)",
        "red fox",
        "t-rex"
    ]
}

# Gears according to: https://growagarden.fandom.com/wiki/Gears#Common

gears = {
    "common": [
        "watering can"
    ],
    "uncommon": [
        "trowel",
        "recall wrench"
    ],
    "rare": [
        "basic sprinkler",
        "firework"
    ],
    "legendary": [
        "advanced sprinkler",
        "star caller",
        "night staff"
    ],
    "mythical": [
        "godly sprinkler",
        "chocolate sprinkler",
        "magnifying glass",
        "nectar staff",
        "pollen radar"
    ],
    "divine": [
        "master sprinkler",
        "cleaning spray",
        "favorite tool",
        "harvest tool",
        "friendship pot",
        "honey sprinkler"
    ],
    "craftables": [
        "lightning rod",
        "berry blusher sprinkler",
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
            "value": 20.0,
            "weight": 0.28
        },
        "chocolate carrot": {
            "value": 11000.0,
            "weight": 0.28
        },
        "pink tulip": {
            "value": 850.0,
            "weight": 0.05
        },
        "strawberry": {
            "value": 15.0,
            "weight": 0.3
        }
    },
    "uncommon": {
        "blue lollipop": {
            "value": 50000.0,
            "weight": 1.0
        },
        "blueberry": {
            "value": 20.0,
            "weight": 0.2
        },
        "crocus": {
            "value": 30000.0,
            "weight": 0.28
        },
        "lavender": {
            "value": 25000.0,
            "weight": 0.28
        },
        "manuka flower": {
            "value": 25000.0,
            "weight": 0.3
        },
        "nightshade": {
            "value": 3500.0,
            "weight": 0.5
        },
        "orange tulip": {
            "value": 850.0,
            "weight": 0.05
        },
        "red lollipop": {
            "value": 50000.0,
            "weight": 4.0
        },
        "rose": {
            "value": 5000.0,
            "weight": 1.0
        },
        "stonebite": {
            "value": 35000.0,
            "weight": 1.0
        },
        "wild carrot": {
            "value": 25000.0,
            "weight": 0.3
        }
    },
    "rare": {
        "bee balm": {
            "value": 18000.0,
            "weight": 1.0
        },
        "candy sunflower": {
            "value": 80000.0,
            "weight": 1.5
        },
        "cauliflower": {
            "value": 40.0,
            "weight": 5.0
        },
        "corn": {
            "value": 40.0,
            "weight": 2.0
        },
        "daffodil": {
            "value": 1000.0,
            "weight": 0.2
        },
        "dandelion": {
            "value": 50000.0,
            "weight": 4.0
        },
        "delphinium": {
            "value": 24000.0,
            "weight": 0.36
        },
        "foxglove": {
            "value": 20000.0,
            "weight": 2.0
        },
        "glowshroom": {
            "value": 300.0,
            "weight": 0.75
        },
        "liberty lily": {
            "value": 30000.0,
            "weight": 6.5
        },
        "mint": {
            "value": 5250.0,
            "weight": 1.0
        },
        "nectarshade": {
            "value": 50000.0,
            "weight": 0.8
        },
        "noble flower": {
            "value": 20000.0,
            "weight": 5.0
        },
        "paradise petal": {
            "value": 25000.0,
            "weight": 2.75
        },
        "peace lily": {
            "value": 24000.0,
            "weight": 0.6
        },
        "pear": {
            "value": 20000.0,
            "weight": 3.0
        },
        "raspberry": {
            "value": 100.0,
            "weight": 0.75
        },
        "succulent": {
            "value": 25000.0,
            "weight": 5.0
        },
        "tomato": {
            "value": 30.0,
            "weight": 0.5
        }
    },
    "legendary": {
        "aloe vera": {
            "value": 69000.0,
            "weight": 5.5
        },
        "avocado": {
            "value": 350.0,
            "weight": 6.5
        },
        "bamboo": {
            "value": 4000.0,
            "weight": 4.0
        },
        "banana": {
            "value": 1750.0,
            "weight": 1.5
        },
        "boneboo": {
            "value": 141141.0,
            "weight": 15.0
        },
        "cantaloupe": {
            "value": 34000.0,
            "weight": 5.5
        },
        "cranberry": {
            "value": 3500.0,
            "weight": 1.0
        },
        "durian": {
            "value": 7500.0,
            "weight": 8.0
        },
        "firework flower": {
            "value": 151000.0,
            "weight": 20.0
        },
        "green apple": {
            "value": 300.0,
            "weight": 3.0
        },
        "horned dinoshroom": {
            "value": 69000.0,
            "weight": 5.0
        },
        "lilac": {
            "value": 35000.0,
            "weight": 3.0
        },
        "lumira": {
            "value": 85000.0,
            "weight": 6.0
        },
        "moonflower": {
            "value": 9500.0,
            "weight": 2.0
        },
        "nectar thorn": {
            "value": 40111.0,
            "weight": 7.0
        },
        "papaya": {
            "value": 1000.0,
            "weight": 3.0
        },
        "pumpkin": {
            "value": 3400.0,
            "weight": 8.0
        },
        "rafflesia": {
            "value": 3500.0,
            "weight": 8.0
        },
        "starfruit": {
            "value": 15000.0,
            "weight": 3.0
        },
        "violet corn": {
            "value": 50000.0,
            "weight": 3.0
        },
        "watermelon": {
            "value": 3000.0,
            "weight": 7.0
        },
        "white mulberry": {
            "value": "N/A",
            "weight": "N/A"
        }
    },
    "mythical": {
        "bell pepper": {
            "value": 5500.0,
            "weight": 8.0
        },
        "bendboo": {
            "value": 155000.0,
            "weight": 18.0
        },
        "blood banana": {
            "value": 6000.0,
            "weight": 1.5
        },
        "cactus": {
            "value": 3400.0,
            "weight": 7.0
        },
        "celestiberry": {
            "value": 10000.0,
            "weight": 2.0
        },
        "coconut": {
            "value": 400.0,
            "weight": 14.0
        },
        "cocovine": {
            "value": 66666.0,
            "weight": 14.0
        },
        "dragon fruit": {
            "value": 4750.0,
            "weight": 12.0
        },
        "easter egg": {
            "value": 2500.0,
            "weight": 3.0
        },
        "eggplant": {
            "value": 12000.0,
            "weight": 5.0
        },
        "firefly fern": {
            "value": 72000.0,
            "weight": 5.0
        },
        "guanabana": {
            "value": 70500.0,
            "weight": 4.0
        },
        "honeysuckle": {
            "value": 100000.0,
            "weight": 12.0
        },
        "ice cream bean": {
            "value": 4500.0,
            "weight": 4.0
        },
        "kiwi": {
            "value": 2750.0,
            "weight": 5.0
        },
        "lemon": {
            "value": 350.0,
            "weight": 1.0
        },
        "lily of the valley": {
            "value": 49120.0,
            "weight": 6.0
        },
        "lime": {
            "value": 350.0,
            "weight": 1.0
        },
        "mango": {
            "value": 6500.0,
            "weight": 15.0
        },
        "moon melon": {
            "value": 18000.0,
            "weight": 8.0
        },
        "moonglow": {
            "value": 25000.0,
            "weight": 7.0
        },
        "nectarine": {
            "value": 48000.0,
            "weight": 3.0
        },
        "parasol flower": {
            "value": 200000.0,
            "weight": 6.0
        },
        "passionfruit": {
            "value": 3550.0,
            "weight": 3.0
        },
        "peach": {
            "value": 300.0,
            "weight": 2.0
        },
        "pineapple": {
            "value": 2000.0,
            "weight": 3.0
        },
        "pink lily": {
            "value": 65000.0,
            "weight": 6.0
        },
        "prickly pear": {
            "value": 7000.0,
            "weight": 7.0
        },
        "purple dahlia": {
            "value": 75000.0,
            "weight": 12.0
        },
        "suncoil": {
            "value": 80000.0,
            "weight": 10.0
        }
    },
    "divine": {
        "cacao": {
            "value": 12000.0,
            "weight": 8.0
        },
        "candy blossom": {
            "value": 100000.0,
            "weight": 3.0
        },
        "cherry blossom": {
            "value": 500.0,
            "weight": 3.0
        },
        "crimson vine": {
            "value": 1250.0,
            "weight": 1.0
        },
        "cursed fruit": {
            "value": 25570.0,
            "weight": 30.0
        },
        "dragon pepper": {
            "value": 81000.0,
            "weight": 6.0
        },
        "feijoa": {
            "value": 13000.0,
            "weight": 10.0
        },
        "fossilight": {
            "value": 89000.0,
            "weight": 4.0
        },
        "grape": {
            "value": 7850.0,
            "weight": 3.0
        },
        "hive fruit": {
            "value": 62000.0,
            "weight": 8.0
        },
        "loquat": {
            "value": 8000.0,
            "weight": 6.5
        },
        "lotus": {
            "value": 35000.0,
            "weight": 20.0
        },
        "mega mushroom": {
            "value": 500.0,
            "weight": 70.0
        },
        "moon blossom": {
            "value": 66666.0,
            "weight": 3.0
        },
        "moon mango": {
            "value": 60000.0,
            "weight": 15.0
        },
        "mushroom": {
            "value": 151000.0,
            "weight": 25.0
        },
        "pepper": {
            "value": 8000.0,
            "weight": 5.0
        },
        "pitcher plant": {
            "value": 32000.0,
            "weight": 12.0
        },
        "rosy delight": {
            "value": 69000.0,
            "weight": 10.0
        },
        "soul fruit": {
            "value": 7750.0,
            "weight": 25.0
        },
        "sunflower": {
            "value": 160000.0,
            "weight": 16.5
        },
        "traveler's fruit": {
            "value": 70000.0,
            "weight": 15.0
        },
        "venus fly trap": {
            "value": 85000.0,
            "weight": 10.0
        }
    },
    "prismatic": {
        "beanstalk": {
            "value": 28000.0,
            "weight": 10.0
        },
        "burning bud": {
            "value": 70000.0,
            "weight": 12.0
        },
        "elephant ears": {
            "value": 77000.0,
            "weight": 18.0
        },
        "ember lily": {
            "value": 66666.0,
            "weight": 12.0
        },
        "sugar apple": {
            "value": 50000.0,
            "weight": 9.0
        }
    },
    "transcendent": {
        "amber spine": {
            "value": "N/A",
            "weight": "N/A"
        },
        "bone blossom": {
            "value": 175000.0,
            "weight": 7.0
        },
        "giant pinecone": {
            "value": "N/A",
            "weight": "N/A"
        },
        "grand volcania": {
            "value": "N/A",
            "weight": "N/A"
        },
        "horsetail": {
            "value": "N/A",
            "weight": "N/A"
        },
        "lingonberry": {
            "value": "N/A",
            "weight": "N/A"
        },
        "purple cabbage": {
            "value": 500.0,
            "weight": 5.0
        }
    }
}
# mutations according to: https://www.pockettactics.com/grow-a-garden-mutations
# format is: "mutation":<multiplier>

mutations={
    "growth": {
        "none": 1,
        "ripe": 1,
        "gold": 20,
        "rainbow": 50
    },
    "environment": {
        "alienlike": 100,
        "amber": 10,
        "ancientamber": 50,
        "aurora": 90,
        "bloodlit": 4,
        "burnt": 4,
        "celestial": 120,
        "ceramic": 30,
        "chilled": 2,
        "choc": 2,
        "clay": 3,
        "cloudtouched": 5,
        "cooked": 10,
        "dawnbound": 150,
        "disco": 125,
        "drenched": 5,
        "fried": 8,
        "frozen": 10,
        "heavenly": 5,
        "historicamber": 150,
        "honeyglazed": 5,
        "meteoric": 125,
        "molten": 25,
        "moonlit": 2,
        "oldamber": 20,
        "paradisal": 100,
        "plasma": 5,
        "pollinated": 3,
        "sandy": 3,
        "shocked": 100,
        "sundried": 85,
        "twisted": 5,
        "verdant": 4,
        "voidtouched": 135,
        "wet": 2,
        "wiltproof": 4,
        "windstruck": 2,
        "zombified": 25
    }
}
