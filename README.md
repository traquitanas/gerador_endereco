# Gerador Endereço

<br>

Programa para gerar endereços *fakes* aleatórios, definido apenas o município. Elaborado visando popular um bancos de dados para um projeto realizado em um município específico.

<br>

----

### Como Instalar?

<br>

```bash
pip3 install gerador-endereco --upgrade
```

<br>

----

### Como usar?

<br>

Inicialmente é necessário gerar um conjunto/lista de CEPs únicos e aleatórios, definindo apenas a unidade da federação e nome do município. Como resultado, são geradas duas listas:

1. A primeira lista contem CEPs;
2. A segunda lista contem bairros.

```python
from gerador_endereco import *

list_ceps, list_bairros = get_list_ceps_bairros(estado='sp', municipio='piracicaba')

print(list_ceps[0:10])
print(list_bairros[0:10])
```

<br>

Uma vez com essa lista de CEPs aleatórios, é possível obter o logradouro completo por meio da função.

```python
cep = random.choice(listas[0])
get_random_complete_address(cep)
```

<br>

O resultado será um dicionário com um endereço aleatório, por exemplo:

```python
{'bairro': 'Nova Piracicaba',
 'cep': '13405-078',
 'cidade': 'Piracicaba',
 'endereco_completo': 'Praça Noêmia Godoy Leme, 121 - Nova Piracicaba - Piracicaba, SP - CEP: 13405-078',
 'logradouro': 'Praça Noêmia Godoy Leme',
 'numero': '121',
 'uf': 'SP'}
```

<br>

Caso tenha interesse, há um [*Google Colab*](https://colab.research.google.com/drive/1fljRarvBgD9Lm3k3PO23a6m_E8Zd5kFL?usp=sharing) para testes.

<br>

-----

### *TODO*:

1. Ajustar o *output* usando uma *OrderedDicts*;
