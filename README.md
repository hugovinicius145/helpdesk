<h1>Projeto de API com Django Rest Framework Para Criação de um Help Desk.</h1>

<h3>Requisitos:</h3>
<ul>
    <li>Python 3 (Ou superior).</li>
    <li>PIP.</li>
    <li>MySql.</li>
</ul>

<h3>Configuração da Base de Dados</h3>
<ul>
    <li>Crie uma Database chamada helpDesk</li>
    <li>Crie um arquivo de configuração MySql</li>
    <li>
        <ul>
            <li>
            ```
            !includedir /etc/mysql/conf.d/
            !includedir /etc/mysql/mysql.conf.d/
            [client]
            database = helpDesk
            user = nome_de_usuario
            password = sua_senha
            default-character-set = utf8
            ```
            </li>
        </ul>
    </li>
    <li>Reinicie o MySql</li>
</ul>

<h3>Configuração da API</h3>
<ul>
    <li>Crie um Ambiente Virtual Python:</li>
    > python3 -m venv venv
    <li>Ative o Ambiente Virtual:</li>
    > source venv/bin/activate
    <li>Instale as dependências do projeto:</li>
    > pip install -r requirements.txt
    <li>Crie um super usuario de admin:</li>
    > python manage.py createsuperuser
    <li>Valide as configurções dos Models:</li>
    > python manage.py makemigrations
    <li>Crie as tabelas do banco de dados:</li>
    > python manage.py migrate
    <li><strong>Execute a Aplicação:</strong></li>
    > python manage.py runserver

</ul>