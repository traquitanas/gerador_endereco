# Gerador Endereço

<br>

Programa para gerar endereços aleatórios d'um município para popular um banco de dados.

<br>

----

### Como Instalar?

```bash
pip install gerador-endereco --upgrade
```

<br>

----

### Como usar?

1. Inicialmente é necessário gerar um conjunto/lista de CEPs únicos e aleatórios, definindo apenas a unidade da federação e nome do município.

Como resultado, são geradas duas listas: a primeira contendo CEPs e a segunda contendo bairros.

```python
import random
from gerador_endereco import *

listas = get_list_ceps_bairros(estado='sp', municipio='piracicaba')
```

<br>

2. Uma vez com essa lista de CEPs aleatórios, é possível obter o logradouro completo por meio da função.

```python
cep = random.choice(listas[0])
get_random_complete_address(cep)
```

<br>

----

### Referências

- [**GitHub**: consulta_correios](https://github.com/arthurfortes/consulta_correios)
- [**Medium**: Consultar Endereços e CEPs brasileiros utilizando python](https://fortes-arthur.medium.com/consultar-endereços-e-ceps-brasileiros-utilizando-python-9c8f14f4592)
