import requests

#goku, vegeta, gohan, bulma, piccolo, freezer, zarbon, dodoria, ginyu, celula, gohan
character_name = input('Enter a Character name: ')
url = f'https://dragonball-api.com/api/characters?name={character_name}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    for char in data:
        name = char['name']
        print(f'Name = {name}')
        
        ki = char['ki']
        print(f'Ki = {ki}')

        maxki = char['maxKi']
        print(f'Max ki = {maxki}')

        race = char['race']
        print(f'Race = {race}')

        gender = char['gender']
        print(f'Gender = {gender}')

        affiliation = char['affiliation']
        print(f'Affiliation = {affiliation}')
else:
    print('Data is not fetched')