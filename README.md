# Projeto de API com Django Rest Framework Para Criação de um Help Desk.

### Requisitos:
<ul>
    <li>Python 3 (Ou superior).</li>
    <li>PIP.</li>
    <li>MySql.</li>
</ul>

### Configuração da Base de Dados

Crie uma Database chamada helpDesk

Crie um arquivo de configuração MySql
> /etc/mysql/helpDesk.cnf

```
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/
[client]
database = helpDesk
user = nome_de_usuario
password = sua_senha
default-character-set = utf8
```
Reinicie o MySql

### Configuração da API


Crie um Ambiente Virtual Python:
> python3 -m venv venv

Ative o Ambiente Virtual:
> source venv/bin/activate

Instale as dependências do projeto:
> pip install -r requirements.txt

Crie um super usuario de admin:
> python manage.py createsuperuser

Valide as configurções dos Models:
> python manage.py makemigrations

Crie as tabelas do banco de dados:
> python manage.py migrate

<strong>Execute a Aplicação:</strong>
> python manage.py runserver

