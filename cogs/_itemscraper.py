"""
Temporary Scrape script to get prices
DO NOT MAKE MY LIFE HARD BY MANUALLY TYPING PRICES THIS IS NOT FUN.
"""

# Of course made by yours truly, Chatgpt

import json # for formatting
import requests
from bs4 import BeautifulSoup

base_url = "https://growagarden.fandom.com/wiki/"

def prettify(json_data):
    return json.dumps(json_data, indent=4, separators=(',', ': '))

def get_pets():
    url="https://growagarden.fandom.com/wiki/Pets"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return f"[ERROR]: {e}"

    soup = BeautifulSoup(res.text, 'html.parser')
    tables=soup.find_all("div", class_="tabber wds-tabber")[:2]
    pets={}
    
    for table in tables:
        categories=[category.text for category in table.find_all("div", class_="wds-tabs__tab-label")]
        print(categories)
        # Pets seperated by category
        categories_div = table.find_all("div",class_="wikia-gallery wikia-gallery-caption-below wikia-gallery-position-left wikia-gallery-spacing-medium wikia-gallery-border-none wikia-gallery-captions-center wikia-gallery-caption-size-medium")
        
        for category_name, category in zip(categories,categories_div):
            pets[category_name.lower()] = pets.get(category_name.lower(),[]) # Makes sure it is a lisit for errors
            for pet in category.find_all("div",class_="lightbox-caption"):
                pet_name = pet.find("a").text.lower()
                pets[category_name.lower()].append(pet_name)
            pets[category_name.lower()]=sorted(pets[category_name.lower()])
    # Final sort
    for category in pets:
        pets[category]=sorted(pets[category])
    
    return pets

def get_mutations():
    url="https://growagarden.fandom.com/wiki/Mutations"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"[ERROR]: {e}")
        return {}
    soup = BeautifulSoup(res.text, 'html.parser')
    tables=soup.find_all("table", class_="wikitable")[:2]
    
    mutations={
        "growth":{ # Default mutations
                "none":1,
                "ripe": 1,
                "gold": 20,
                "rainbow": 50
            },
        "environment":{}
    }
    
    # Standard
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            # print(cells)
            if len(cells) == 5 and not "Name" in cells[0].text and not cells[0].text.lower() in mutations["growth"].keys(): # Checks if its a valid row that has mutations
                mutation = cells[0].text.strip().lower()
                multiplier = int(cells[2].text.replace("x","").replace("×","").strip()) # Fuck you, the guy who added that "×"
                mutations["environment"][mutation] = multiplier
    
    # Final sort
    mutations["environment"] = dict(sorted(mutations["environment"].items()))
    
    return mutations

def get_fruit_data():
    url = "https://growagarden.fandom.com/wiki/Crops"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return f"[ERROR]: {e}"
    soup = BeautifulSoup(res.text, 'html.parser')
    tables=soup.find_all("div", class_="tabber wds-tabber")[:2]
    
    fruit_names_dict={}
    
    for table in tables:
        categories=table.find_all("div", class_="wds-tabs__tab-label")
        
        # Fruits seperated by category
        fruit_categories=table.find_all("div",class_="wikia-gallery wikia-gallery-caption-below wikia-gallery-position-left wikia-gallery-spacing-medium wikia-gallery-border-none wikia-gallery-captions-center wikia-gallery-caption-size-medium")
        
        for category, fruit_category in zip(categories,fruit_categories):
            category_name = category.find("a").text.lower()
            fruit_names_dict[category_name] = fruit_names_dict.get(category_name,{})
            
            fruit_links = [div.find("a")["href"] for div in fruit_category.find_all("div",class_="lightbox-caption")]
            fruit_names = [div.find("a").text.lower() for div in fruit_category.find_all("div",class_="lightbox-caption")]
            
            fruit=sorted(zip(fruit_names,fruit_links))
            
            for fruit_name, fruit_link in fruit:
                base_value=0
                base_weight=0
                print("[DEBUG] Searching for: ", fruit_name)
                url= f"https://growagarden.fandom.com{fruit_link}"
                try:
                    res = requests.get(url, timeout=10)
                    res.raise_for_status()
                except Exception as e:
                    print(f"[ERROR]: {e}")
                    print(f"Skipping {fruit_name} in {category_name}...")
                    continue
                
                fruit_soup=BeautifulSoup(res.text, 'html.parser')
                table= fruit_soup.find("section",class_="pi-item pi-group pi-border-color") # Finds the table that holds all the values
                
                base_value_element= table.find(attrs={"data-source":"base_value"}) # Finds the value element that holds the value
                base_weight_element = table.find(attrs={"data-source": "base_weight"})
                try:
                    base_value = float(
                        base_value_element
                        .find("b")
                        .text
                        .replace(",","")
                        )
                    base_weight = float(
                        base_weight_element
                        .find("div",class_="pi-data-value pi-font")
                        .text
                        .replace("kg","")
                        .replace("~","")
                        .strip()
                        )
                except Exception as e:
                    print(f"[ERROR]: {e}")
                    print(f"Skipping {fruit_name} in {category_name}...")
                finally:
                    fruit_names_dict[category_name][fruit_name]={"value":base_value or "N/A","weight":base_weight or "N/A"}
    
    # Final sort
    for category in fruit_names_dict.keys():
        fruit_names_dict[category] = dict(sorted(fruit_names_dict[category].items()))
    
    return fruit_names_dict

def get_gears():
    url="https://growagarden.fandom.com/wiki/Gears"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return f"[ERROR]: {e}"

    soup = BeautifulSoup(res.text, 'html.parser')
    table=soup.find("div", class_="tabber wds-tabber")
    gears={}
    
    # Sometimes mfs adding a type even though it has nothing inside
    categories=[category.text for category in table.find_all("div", class_="wds-tabs__tab-label") if not "Prismatic" in category.text]
    
    # Gears seperated by category
    tables = table.find_all("table", class_="wikitable") 
    
    for category, table in zip(categories, tables):
        gear_names = [
            row.find_all("td")[0].text.lower().strip()
            for row in table.find_all("tr")[1:]
            if row.find_all("td")
        ]
        
        gears[category.lower()] = gear_names
    
    return gears

if __name__ == "__main__":
    print(prettify(get_gears()))
    print(prettify(get_fruit_data()))
    print(prettify(get_mutations()))
    print(prettify(get_gears()))