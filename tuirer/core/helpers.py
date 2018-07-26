import requests
#params = {'apikey': '-YOUR API KEY HERE-'}

api_root = 'https://swapi.co/api'

country1 = 'Brazil'
country2 = 'China'

pop_brazil = 0
pop_china = 0

url = f'http://api.population.io:80/1.0/wp-rank/2000-01-01/male/{country1}/today/'
url2 = f'http://api.population.io:80/1.0/wp-rank/2000-01-01/male/{country2}/today/'

def print_name():
    #import ipdb; ipdb.set_trace()
    #GET CHINA
    request = requests.get(url)
    data = request.json()
    print(data)

    pop_brazil = data['rank']

    #GET BRASIL
    request = requests.get(url2)
    data = request.json()
    print(data)
    pop_china = data['rank']

    return str(f'Subitação da China com o brazil é: {pop_china - pop_brazil}')


def get_character_name(id):
    url = f'{api_root}/people/{id}'
    name = requests.get(url).json()['name']
    return name
