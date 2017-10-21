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

1 - Instalação do pip:

  1.1 - Ubuntu (Linux)

  ```
  $ sudo apt-get update && sudo apt-get install -y python-pip
  ```
  
  1.2 - macOS
  
  ```
  $ sudo easy_install pip
  ```
  
2 - Instalar o pacotes python necessário:

 * Django
 * requests
 
 ```
 $ pip install Django
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
