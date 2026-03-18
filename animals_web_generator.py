"""
This module generates a web page for the animal 'animal_name'.
"""

import json
import data_fetcher

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
    

def serialize_animal(animal_obj):
    """Read JSON and convert it to HTML list items"""
    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    skin_type = characteristics.get("skin_type", "Unknown")
    animal_type = characteristics.get("type")
    locations = animal_obj.get("locations", [])
    location = locations[0] if locations else "Unknown"

    html = "<li class='cards__item'>"
    html += f"<div class='card__title'>{name}</div>"
    html += "<div class='card__text'>"
    html += f"<ul>"
    html += f"<li><strong>Diet:</strong> {diet}</li>"
    html += f"<li><strong>Skin type:</strong> {skin_type}</li>"
    html += f"<li><strong>Location:</strong> {location}</li>"
    if animal_type:
        html += f"<li><strong>Type:</strong> {animal_type}</li>"
    html += "</ul></div></li>"

    return html

def main():
    """ Main function """
    
    animal_name = input("Enter a name of an animal: ")

    #old ->data = load_data("animals_data.json")
    data = data_fetcher.fetch_data(animal_name)
    
    if not data:
        print(f'The animal "{animal_name}" was not found.')
        return

    # Save data to JSON file for copying
    with open('animals_data.json', 'w', encoding='utf-8') as animal_files:
        json.dump(data, animal_files, indent=4)

    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)

    with open('animals_template.html', 'r', encoding='utf-8') as template_file:
        html_content = template_file.read()

    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


if __name__ == '__main__':
    main()