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

Instruções para instalação
--------------------------

1 - Dependências necessárias:

  * git
  * python
  * django

  ```
  $ sudo apt-get update && sudo apt-get install -y git python3-dev python-django
  ```
2 - Instalar o pacote python necessário:

 * requests
 
 ```
 $ pip install requests
 ```

2 - Clonar o repositório:

```
$ git clone https://github.com/TransportadoraOrgaos/pi2-transport_orgaos.git
$ cd pi2-transport_orgaos
$ cd transportadora_orgaos
```

3 - Rodar o servidor

 ```
 $ python manage.py runserver
 ```
