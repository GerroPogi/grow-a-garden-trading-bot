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

fruits={
    "common":[
        "carrot",
        "strawberry",
        "chocolate carrot",
        "pink tulip"
    ],
    "uncommon":[
        "blueberry",
        "wild carrot",
        "rose",
        "orange tulip",
        "rose",
        "red lollipop",
        "nightshade",
        "manuka flower",
        "lavender",
        "crocus"
    ],
    "rare":[
        "tomato",
        "cauliflower",
        "delphinium",
        "peace lily",
        "pear",
        "raspberry",
        "corn",
        "daffodil",
        "candy sunflower",
        "mint",
        "glowshroom",
        "dandelion",
        "nectarshade",
        "foxglove",
        "succulent",
        "bee balm"
    ],
    "legendary":[
        "watermelon",
        "pumpkin",
        "banana",
        "aloe vera",
        "avocado",
        "cantaloupe",
        "rafflesia",
        "green apple",
        "bamboo",
        "cranberry",
        "durian",
        "moonflower",
        "starfruit",
        "papaya",
        "lilac",
        "lumira",
        "violet corn",
        "nectar thorn"
    ],
    "mythical":[ # had to use chatgpt now. ts hard
        "peach",
        "pineapple",
        "moon melon",
        "celestiberry",
        "kiwi",
        "guanabana",
        "bell pepper",
        "prickly pear",
        "parasol flower",
        "cactus",
        "lily of the valley",
        "dragon fruit",
        "easter egg",
        "moon mango",
        "mango",
        "coconut",
        "celestiberry",
        "blood banana",
        "moonglow",
        "eggplant",
        "passionfruit",
        "lemon",
        "honeysuckle",
        "nectarine",
        "pink lily",
        "purple dahlia",
        "bendboo",
        "cocovine",
        "ice cream bean",
        "lime"
    ],
    "divine":[
        "loquat",
        "feijoa",
        "pitcher plant",
        "traveler's fruit",
        "rosy delight",
        "pepper",
        "cacao",
        "grape",
        "mushroom",
        "cherry blossom",
        "crimson vine",
        "candy blossom",
        "lotus",
        "venus fly trap",
        "cursed fruit",
        "soul fruit",
        "mega mushroom",
        "moon blossom",
        "hive fruit",
        "sunflower",
        "dragon pepper"
    ],
    "prismatic":[
        "sugar apple",
        "ember lily",
        "elephant ears",
        "beanstalk"
    ],
    "unknown":[
        "noble flower",
        "blue lollipop",
        "burning bud",
        "purple cabbage"
    ]
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


