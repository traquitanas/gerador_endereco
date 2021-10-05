from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as f:
    long_description = f.read()


requirements = [
    'pycep_correios>=5.0.0',
    'requests>=2.25.1',
]

setup(
    name='gerador-endereco',
    version='1.0.0',
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='API para criação de endereços aleatórios em um município específico',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/open-dsa/gerador_endereco',
    packages=find_namespace_packages(
        where='script',
    ),
    # package_dir={
    #     'script': 'random_address',
    # },
    install_requires=requirements,
    keywords='python, endereço aleatório, address',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
)
