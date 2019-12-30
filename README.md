# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/vpilotto/wttd.svg?branch=master)](https://travis-ci.org/vpilotto/wttd)

## Como desenvolver ?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```
git clone https://github.com/vpilotto/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/active
pip install -r requirements-dev.txt
cp contrio/env-sample .env
python manage.py test
```


## Como fazer o deploy ?

1. Crie um instância no heroku
2. Envie as configuracões para o heroku
3. Define uma SECRET_KEY segura para instância
4. Define DEBUG=False
5. Configure o servico de email
6. Envie o código para o heroku

```
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configura o email
git push heroku master --force
```