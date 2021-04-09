from art import *
import json
from time import sleep
import requests

# MENU  ------------------------------------------------------------------------------------------------------------------------


# menu do programa --------------------------------------------------------------------------------------------------------------
def menu():
    op_menu = int(input('--------- MENU ---------\n'
                        '[1] VALIDAR URL\n'
                        '[2] EXPORTAR JSON\n'
                        '[3] EXPORTAR CSV\n'
                        '[4] ROTAS STAR WARS\n'
                        '[5] SAIR\n'
                        'Digite uma opção: '))
    if op_menu == 1:
        limpar_tela()
        verificar_url()
    elif op_menu == 2:
        limpar_tela()
        exportar_json()
    elif op_menu == 3:
        print('Em construção')
        retonar_menu_inicial()
    elif op_menu == 4:
        limpar_tela()
        menu_rotas_star_wars()
    else:
        limpar_tela()
        encerrar_programa()


#  menu das rotas para extração da lista ----------------------------------------------------------------------------------------
def menu_rotas_star_wars():
    print('\n---  QUAL ROTA STAR WARS VOCÊ DESEJA ACESSAR OS ITENS LISTADOS  -----')
    termo = int(input('[1] Filmes\n[2] Personagens\n[3] Planetas\n[4] Espécies\n[5] Naves\n[6] Veículos\nInsira sua opção: '))
    if termo == 1:
        mostrar_filmes()
    elif termo == 2:
        mostrar_personagens()
    elif termo == 3:
        mostrar_planetas()
    elif termo == 4:
        mostrar_especies()
    elif termo == 5:
        mostrar_naves()
    elif termo == 6:
        mostrar_veiculos()
    else:
        encerrar_programa()


# cabeçalho do programa -------------------------------------------------------------------------------------------------------
def iniciar():
    tprint('StarWars')
    op = str(input('Deseja continuar [S/N]: ')).upper()
    if op == "S":
        limpar_tela()
        menu()
    else:
        limpar_tela()
        encerrar_programa()


# retornar menu inicial --------------------------------------------------------------------------------------------------------
def retonar_menu_inicial():
    op_retorno = str(input('---\nDeseja retornar ao MENU INICIAL [S/N]: ')).upper()
    if op_retorno == "S":
        limpar_tela()
        menu()
    else:
        limpar_tela()
        encerrar_programa()


# EXPORTAÇÃO DE JSON, LISTA ----------------------------------------------------------------------------------------------------


# exporta json -----------------------------------------------------------------------------------------------------------------
def exportar_json():
    print('\n---  QUAL ROTA STAR WARS VOCÊ DESEJA EXPORTAR O JSON  -----')
    termo = int(input('[1] Filmes\n[2] Personagens\n[3] Planetas\n[4] Espécies\n[5] Naves\n[6] Veículos\nInsira sua opção: '))
    if termo == 1:
        retorna_objeto = requests.get("https://swapi.dev/api/films/")
        print(retorna_objeto.json())
        retonar_menu_inicial()
    elif termo == 2:
        retorna_objeto = requests.get("https://swapi.dev/api/people/")
        print(retorna_objeto.json())
        retonar_menu_inicial()
    elif termo == 3:
        retorna_objeto = requests.get("https://swapi.dev/api/planets/")
        print(retorna_objeto.json())
        retonar_menu_inicial()
    elif termo == 4:
        retorna_objeto = requests.get("https://swapi.dev/api/species/")
        print(retorna_objeto.json())
        retonar_menu_inicial()
    elif termo == 5:
        retorna_objeto = requests.get("https://swapi.dev/api/starships/")
        print(retorna_objeto.json())
        retonar_menu_inicial()
    elif termo == 6:
        retorna_objeto = requests.get("https://swapi.dev/api/vehicles/")
        print(retorna_objeto.json())
        retonar_menu_inicial()
    else:
        encerrar_programa()


# verifica a url ---------------------------------------------------------------------------------------------------------------
def verificar_url():
    url = str(input('Digite o site que você deseja acessar: '))
    url_valida = requests.get(url)
    print(f'---\nStatus Code: {url_valida.status_code}')
    retonar_menu_inicial()


# tela inicial do programa -----------------------------------------------------------------------------------------------------
def encerrar_programa():
    print('Encerrado o programa...')
    sleep(2)
    print('Fim')
    exit()


# limpar tela  -----------------------------------------------------------------------------------------------------------------
def limpar_tela():
    print('\n' * 20)


# inicia o programa -----------------------------------------------------------------------------------------------------------
iniciar()