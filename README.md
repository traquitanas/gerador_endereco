# Gerador Endereço

<br>

Programa para gerar endereços aleatórios d'um município para popular um banco de dados.

### Instalar

```python
pip install gerador-endereco
```

### Como usar?

- Inicialmente é necessário gerar um conjunto/lista de CEPs únicos e aleatórios, definindo apenas a unidade da federação e nome do município.
Como resultado, são geradas duas listas: a primeira contendo CEPs e a segunda contendo bairros.

```python
listas = get_list_ceps_bairros(estado='sp', municipio='piracicaba')
```

<br>

- Uma vez com essa lista de CEPs aleatórios, é possível obter o lougradouro completo por meio da função.
- 
```python
cep = random.choice(listas[0])
get_random_complete_address(cep)
```
-------

### Autor

- [Michel Metran](https://michelmetran.github.io/)
