TransOrg - Sistema de Transporte de Órgãos para Transplantes
========

##### Stable Version [![Build Status - Stable Version](https://travis-ci.org/TransportadoraOrgaos/pi2-transport_orgaos.svg?branch=master)](https://travis-ci.org/TransportadoraOrgaos/pi2-transport_orgaos)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dev Version [![Build Status - Dev Version](https://travis-ci.org/TransportadoraOrgaos/pi2-transport_orgaos.svg?branch=development)](https://travis-ci.org/TransportadoraOrgaos/pi2-transport_orgaos)

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

  Antes, verifique se já não tem o pip instalado em sua máquina:
  
  ```
  $pip --version
  ```
  
  Caso dê erro de `command not found`, segue instruções de instalação:

  1.1 - Ubuntu (Linux)

  ```
  $ sudo apt-get update && sudo apt-get install -y python-pip
  ```
  
  __troubleshooting__
  
  Caso o `pip` apresente problemas, executar os comandos a seguir:
  
  ```
  $ sudo apt-get remove python-pip
  $ cd ~/Downloads
  $ wget https://bootstrap.pypa.io/get-pip.py
  $ python get-pip.py
  ```
  
  1.2 - macOS
  
  ```
  $ sudo easy_install pip
  ```

2 - Clonar o repositório:

```
$ cd
$ git clone https://github.com/TransportadoraOrgaos/pi2-transport_orgaos.git
$ cd pi2-transport_orgaos
```

3 - Instalar os pacotes python:

```
$ pip install -r requirements.txt
```

__troubleshooting 1__

Caso o `pip install` apresente problema de `permission denied`, executar os comandos a seguir:

```
$ sudo -H pip install -r requirements.txt
```

__troubleshooting 2__

Caso a instalação do módulo `cairocffi` apresente o problema a seguir:

```
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-y0b_ir/cairocff
```
Executar os comandos a seguir:

```
$ sudo apt-get install libffi-dev
$ sudo -H pip install -r requirements.txt
```

3 - Rodar o servidor

 ```
 $ python manage.py runserver
 ```
