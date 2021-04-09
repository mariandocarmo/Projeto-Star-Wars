import requests
import json

class Rota:
    def __init__(self):
        self.response_personagens = requests.get('https://swapi.dev/api/people/')
        self.personagens = []
        self.response_planetas = requests.get('https://swapi.dev/api/planets/')
        self.planetas = []
        self.response_filmes = requests.get('https://swapi.dev/api/films/')
        self.filmes = []
        self.response_veiculos = requests.get('https://swapi.dev/api/vehicles/')
        self.veiculos = []
        self.response_especies = requests.get('https://swapi.dev/api/species/')
        self.especies = []
        self.response_naves = requests.get('https://swapi.dev/api/starships/')
        self.naves = []

    def mostrar_personagens(self):
        # Checando o status da requisição
        #response = requests.get('https://swapi.dev/api/people/')
        if (self.response_personagens):
            print(f"Situação de código: {self.response_personagens.status_code}")
        else:
            print(f"Ops! Falha no servidor. Situação de código: {self.response_personagens.status_code}")

        # Transformando dados de personagens json em dicionários filtrados por key=results
        dados_personagens = json.loads(self.response_personagens.text)['results']

        # Criando lista de personagens
        for self.personagem in dados_personagens:
            self.personagens.append(self.personagem['name'])
        print(f"Lista de personagens de Star Wars: {self.personagens}")

    def mostrar_planetas(self):
        # Checando o status da requisição
        if (self.response_planetas):
            print(f"Situação de código: {self.response_planetas.status_code}")
        else:
            print(f"Ops! Falha no servidor. Situação de código: {self.response_planetas.status_code}")

        # Transformando dados de planetas json em dicionários filtrados por key=results
        dados_planetas = json.loads(self.response_planetas.text)['results']

        # Criando lista de planetas
        for planeta in dados_planetas:
            self.planetas.append(planeta['name'])
        print(f"Lista de planetas de Star Wars: {self.planetas}")

    def mostrar_filmes(self):
        # Checando o status da requisição
        if (self.response_filmes):
            print(f"Situação de código: {self.response_filmes.status_code}")
        else:
            print(f"Ops! Falha no servidor. Situação de código: {self.response_filmes.status_code}")

        # Transformando dados de filmes json em dicionários filtrados por key=results
        dados_filme = json.loads(self.response_filmes.text)['results']

        # Criando lista de filmes
        for filme in dados_filme:
            self.filmes.append(filme['title'])
        print(f"Lista de filmes Star Wars: {self.filmes}")

    def mostrar_veiculos(self):
        # Checando o status da requisição
        if (self.response_veiculos):
            print(f"Situação de código: {self.response_veiculos.status_code}")
        else:
            print(f"Ops! Falha no servidor. Situação de código: {self.response_veiculos.status_code}")

        # Transformando dados de veículos json em dicionários filtrados por key=results
        dados_veiculos = json.loads(self.response_veiculos.text)['results']

        # Criando lista de veículos
        for veiculo in dados_veiculos:
            self.veiculos.append(veiculo['name'])
        print(f"Lista de veículos de Star Wars: {self.veiculos}")

    def mostrar_especies(self):
        # Checando o status da requisição
        if (self.response_especies):
            print(f"Situação de código: {self.response_especies.status_code}")
        else:
            print(f"Ops! Falha no servidor. Situação de código: {self.response_especies.status_code}")

        # Transformando dados de espécies json em dicionários filtrados por key=results
        dados_especies = json.loads(self.response_especies.text)['results']
        # Criando lista de espécies
        for especie in dados_especies:
            self.especies.append(especie['name'])
        print(f"Lista de espécies de Star Wars: {self.especies}")

    def mostrar_naves(self):
        # Checando o status da requisição
        if (self.response_naves):
            print(f"Situação de código: {self.response_naves.status_code}")
        else:
            print(f"Ops! Falha no servidor. Situação de código: {self.response_naves.status_code}")
        # Transformando dados de naves json em dicionários filtrados por key=results
        dados_naves = json.loads(self.response_naves.text)['results']

        # Criando lista de naves
        for nave in dados_naves:
            self.naves.append(nave['name'])
        print(f"Lista de naves de Star Wars: {self.naves}")

class Validacao:
        def __init__(self):
            self.url = str(input('Digite o site que você deseja acessar: '))
            self.url_valida = requests.get(self.url)
        # verifica a url ---------------------------------------------------------------------------------------------------------------
        def verificar_url(self):
            print(f'---\nStatus Code: {self.url_valida.status_code}')
        #retonar_menu_inicial()