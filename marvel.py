import json
import requests
import constants


def main():
    character = get_character()
    character_information = get_character_information(character)
    if character_information is not None:
        check_character_information(character_information)


def get_character():
    while True:
        character = input("Enter a character name: ").strip()
        if character == "":
            print("Please provide a valid character name")
            continue
        else:
            return character
        

def get_character_information(character: str) -> json:
    marvel_api_key = constants.marvel_api_key
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
            if not description:
                print("No description found")
                return 0
            print(f"Name: {name}")
            print(f"Description: {description}")
    else:
        print("No data found or incorrect name entered")


if __name__ == "__main__":
    main()
