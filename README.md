# Gerador Endereço

<br>

Programa para gerar endereços aleatórios de um município específico, com objetivo de popular bancos de dados.

<br>

----

### Como Instalar?

<br>

```bash
pip install gerador-endereco --upgrade
```

<br>

----

### Como usar?

<br>

Inicialmente é necessário gerar um conjunto/lista de CEPs únicos e aleatórios, definindo apenas a unidade da federação e nome do município. Como resultado, são geradas duas listas:

1. A primeira lista contem CEPs;
2. A segunda lista contem bairros.

```python
import random
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

O resultado será um endereço aleatório, por exemplo:

```python
Rua José Alexandre de Almeida, 291 - Água das Pedras - Piracicaba, SP - CEP: 13404-206
```

<br>

Caso tenha interesse, há um [*Google Colab*](https://colab.research.google.com/drive/1fljRarvBgD9Lm3k3PO23a6m_E8Zd5kFL?usp=sharing) para testes.
