import json
import requests
import constants

marvel_api_key = constants.marvel_api_key

while True:
    character = input("Enter a character name: ")
    if character == "":
        print("Please provide a valid character name")
        continue
    else:
        break


def get_character_information(character: str) -> json:
    api_url = f"https://gateway.marvel.com:443/v1/public/characters?name={character}&ts=1&apikey={marvel_api_key}"
    try:
        response = requests.get(api_url)
        current_character = response.json()
        information = current_character["data"]["results"]
        return information
    except requests.exceptions.RequestException as error:
        print(f"Sorry! Network error: {error}")
        return None


def check_character_information(information: json) -> str:
    if information:
        for details in information:
            name = details["name"]
            description = details["description"]
            if description == "":
                print("No description found")
                return 0
            print(f"Name: {name}")
            print(f"Description: {description}")
    elif character_information is None:
        return 0
    else:
        print("No data found or incorrect name entered")


character_information = get_character_information(character)
check_character_information(character_information)
