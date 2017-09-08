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
  $ sudo apt-get update && sudo apt-get install -y git python3-dev python-django postgresql postgresql-contrib pgadmin3 python-psycopg2 npm
  ```

2 - Clonar o Repositório:

```
$ git clone https://github.com/TransportadoraOrgaos/pi2-transport_orgaos.git
$ cd pi2-transport_orgaos
```

3 - Configurar senha para o usuário postgres do banco de dados

```
$ sudo -u postgres psql postgres

psql (9.6.4)
Type "help" for help.

postgres=# \password postgres
Enter new password: 
Enter it again: 
postgres=# \q

```
* Entre com a senha: postgres

4 - Criar uma nova conexão no pgadmin:

```
$ pgadmin3
```

* Ao abrir a interface gráfica do pgadmin, clicar no ícone da tomada para criar uma nova conexão. Entrar com as seguintes informações:

```
name: postgreSQL
host: 127.0.0.1
password: postgres
```
* Não altere os outros campos

5 - Criar o banco de dados na nova conexão (pgadmin)

* Na barra lateral da interface gráfica do pgadmin, clicar com o mouse direito em databases > New Database...

* Criar um novo database com o nome: transorg

6 - Atualize o banco de dados e rode o servidor:
  ```
  $ cd transportadora_orgaos
  $ python manage.py migrate
 
  ```
7 - Rodar o Servidor
 ```
 $ python manage.py runserver

 ```
