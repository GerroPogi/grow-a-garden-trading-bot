"""
Temporary Scrape script to get prices
DO NOT MAKE MY LIFE HARD BY MANUALLY TYPING PRICES THIS IS NOT FUN.
"""

# Of course made by yours truly, Chatgpt

import json
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

base_url = "https://growagarden.fandom.com/wiki/"

# All fruit names (flattened from dictionary)
fruits = {
    "common": {
        "carrot": {"weight": 0.28, "price": 20},
        "strawberry": {"weight": 0.3, "price": 20},
        "chocolate carrot": {"weight": 0.28, "price": 11000},
        "pink tulip": {"weight": 0.05, "price": 850}
    },
    "uncommon": [
        "blueberry", "wild carrot", "rose", "orange tulip", "red lollipop",
        "nightshade", "manuka flower", "lavender", "crocus"
    ],
    "rare": [
        "tomato", "cauliflower", "delphinium", "peace lily", "pear", "raspberry",
        "corn", "daffodil", "candy sunflower", "mint", "glowshroom", "dandelion",
        "nectarshade", "foxglove", "succulent", "bee balm"
    ],
    "legendary": [
        "watermelon", "pumpkin", "banana", "aloe vera", "avocado", "cantaloupe",
        "rafflesia", "green apple", "bamboo", "cranberry", "durian", "moonflower",
        "starfruit", "papaya", "lilac", "lumira", "violet corn", "nectar thorn"
    ],
    "mythical": [
        "peach", "pineapple", "moon melon", "celestiberry", "kiwi", "guanabana",
        "bell pepper", "prickly pear", "parasol flower", "cactus", "lily of the valley",
        "dragon fruit", "easter egg", "moon mango", "mango", "coconut", "blood banana",
        "moonglow", "eggplant", "passionfruit", "lemon", "honeysuckle", "nectarine",
        "pink lily", "purple dahlia", "bendboo", "cocovine", "ice cream bean", "lime"
    ],
    "divine": [
        "loquat", "feijoa", "pitcher plant", "traveler's fruit", "rosy delight", "pepper",
        "cacao", "grape", "mushroom", "cherry blossom", "crimson vine", "candy blossom",
        "lotus", "venus fly trap", "cursed fruit", "soul fruit", "mega mushroom",
        "moon blossom", "hive fruit", "sunflower", "dragon pepper"
    ],
    "prismatic": [
        "sugar apple", "ember lily", "elephant ears", "beanstalk"
    ],
    "unknown": [
        "noble flower", "blue lollipop", "burning bud", "purple cabbage"
    ]
}



def get_fruit_data(fruit):
    url = base_url + fruit.title().replace(" ", "_")
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return f"[ERROR] {fruit}: {e}"

    soup = BeautifulSoup(res.text, 'html.parser')
    group_section = soup.find("section", class_="pi-item pi-group pi-border-color")
    if not group_section:
        return f"[SKIP] {fruit}: No info box found."
    

    value_element = group_section.find(attrs={"data-source": "base_value"})
    weight_element = group_section.find(attrs={"data-source": "base_weight"})

    base_value = float(value_element.get_text(strip=True).replace("Base Value","").replace("~","").replace(",","")) if value_element else "N/A"
    
    # mfs in wiki adding random ahh characters
    base_weight = float(weight_element.get_text(strip=True).replace("Base Weight","").replace("kg","").replace("~","").replace(" ","").replace("(estimate)","")) if weight_element else "N/A"

    return {"weight":base_weight,"price":base_value}

new_fruits={}

print("Fetching fruit data from Fandom Wiki...\n")
for category in fruits:
    new_fruits[category]={}
    print("Category: ", category.capitalize())
    for fruit in fruits[category]:
        data= get_fruit_data(fruit)
        new_fruits[category][fruit]=data
        print("Fruit added: ", fruit.capitalize(),data)

# print(get_fruit_data("rafflesia"))

print(json.dumps(new_fruits,indent=4))