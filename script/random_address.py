import random
import requests
from pycep_correios import get_address_from_cep, WebService


def get_list_ceps_bairros(estado='sp', municipio='piracicaba', loops=20):
    """
    Função que auxilia na definição de endereços aleatórios em uma cidade.

    :param estado: sigla da unidade da federação (default: "sp")
    :param municipio: nome do município (default: "piracicaba")
    :param loop: quanto maior o número de loops, maior a lista  (default: 20)
    :return: Output consiste em duas listas (list_ceps, list_bairros)
    """
    termos = [
        'rua', 'avenida', 'praça', 'bosque',  # Padrão
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro',
        'dezembro',  # Meses
        'marechal', 'sargento', 'duque', 'soldado', 'capitão', 'major',  # Patentes
        'dom', 'senhor', 'senhora',  # Pronomes de Tratamento
        'almeida', 'caetano', 'pedro', 'barbosa', 'rui', 'pinto', 'joão', 'são',  # Nomes
    ]
    i = 1
    list_ceps = []
    list_bairros = []
    while i <= loops:
        url = 'https://viacep.com.br/ws/{}/{}/{}/json/'.format(estado, municipio, random.choice(termos))
        resp = requests.get(url)
        json = resp.json()
        for data in json:
            list_ceps.append(data['cep'])
            list_bairros.append(data['bairro'])
        i += 1

    # CEPs
    list_ceps = list(set(list_ceps))
    list_ceps.sort()

    # Bairros
    list_bairros = list(set(list_bairros))
    list_bairros.sort()

    print(
        'Município: {}-{}\nCEPs distintos: {}\nBairros distintos: {}'.format(
            municipio.title(), estado.upper(),
            len(list_ceps),
            len(list_bairros)
        )
    )
    return list_ceps, list_bairros


def get_random_complete_address(cep):
    """
    Pega um endereço a parte de um CEP

    :param cep: Definição do CEP que se deseja obter o endereço (Exemplo: '13419-398')
    :return: String com o endereço completo.

    """
    # Endereço
    end = get_address_from_cep(cep, webservice=WebService.VIACEP)

    # Adiciona um número aleatório
    end['complemento'] = '{}'.format(random.randrange(1, 999))

    # Cria uma chave no dict com Endereço Completo
    end['endereco_completo'] = '{}, {} - {} - {}, {} - CEP: {}'.format(
        end['logradouro'],
        end['complemento'],
        end['bairro'],
        end['cidade'],
        end['uf'],
        end['cep'],
    )
    print('Endereço Aleatório:\n{}'.format(end['endereco_completo']))
    return end['endereco_completo']


if __name__ == '__main__':
    # Para testes apenas
    listas = get_list_ceps_bairros(estado='sp', municipio='piracicaba')
    end = get_random_complete_address(random.choice(listas[0]))
    print(end)
