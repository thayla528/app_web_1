import requests
from flask import request

base_url = "http://10.135.232.17:5001"


# criar as funcoes q irao pegar os dados da api
# nome da funcao deve ter o prefixo get, post

def get_funcionarios():
    # ------- 1- definir o endpoint que vai ser consumido-------

    endpoint = base_url + "/funcionarios"

    # ------- 2- fazer a requisicao (pedindo os dados)---------

    dados = requests.get(endpoint)

    # ------- 3 retornar os dados-----------------
    return dados.json()

def post_funcionario(dados_funcionario):
    endpoint = f"{base_url}/funcionarios"
    # Envia o dicionário como JSON para a API
    resposta = requests.post(endpoint, json=dados_funcionario)
    return resposta.json()



def get_funcionario_cpf(cpf):
    endpoint = base_url + "/funcionario"

    dados = {
        "cpf": cpf,
    }

    # 2- enviar os dados

    dados = requests.get(endpoint, json=dados)

    return dados.json()

def post_funcionario_cpf(cpf):
    endpoint = base_url + "/funcionario"

    dados = {
        "cpf": cpf,
    }

    # 2- enviar os dados

    dados = requests.post(endpoint, json=dados)

    return dados.json()
