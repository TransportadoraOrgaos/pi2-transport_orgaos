TransOrg - Sistema de Transporte de Órgãos para Transplantes
========
Sistema de controle de informações relativas à câmaras de transporte de órgãos para transplante. TransOrg é um projeto da disciplina Projeto
Integrador 2 da Universidade de Brasília, campus do Gama.

Integrantes
-----------
Anna Larissa

Cristiano Costa

João Paulo

Lucas Couto

Instruções para Instalação
--------------------------

1 - Dependências Necessárias:
  ```
  sudo apt-get update && sudo apt-get install -y git python3-dev \
  python-django postgresql postgresql-contrib pgadmin3 python-psycopg2 npm
  ```

2 - Clonar o Repositório

3 - Atualize o banco de dados e rode o servidor:
  ```
  python manage.py migrate
 
  ```
4 - Rodar o Servidor
 ```
 python manage.py runserver

 ```