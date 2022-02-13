<h1 align="center">Rede de Solidariedade</h1>
<p></p>
<p></p>
<p></p>
<p align="center">Projeto de Extensão IFSC 2021/2 - Rede Solidariedade</p>
<p></p>
<p></p>
<p></p>
<h2 align="center">Para Rodar o Projeto:</h2>
<p></p>
<p></p>
<p></p>
<h4 align="center">0. certifique-se que está na raiz do repositorio [...]/redesolidariedade/"</h4>
<h4 align="center">1. crie uma venv "python -m venv venv"</h4>
<h4 align="center">2. ative a venv "venv\Scripts\activate"</h4>
<h4 align="center">3. instale o pip "python -m pip install --upgrade pip"</h4>
<h4 align="center">4. va para a pasta app "cd app" </h4>
<h4 align="center">4. instale os requirements.txt "pip install -r requirements.txt"</h4>
<h4 align="center">5. va para a raiz do app "cd main"</h4>
<h4 align="center">5. va para o app main "cd main"</h4>
<h4 align="center">6. faça as migrations "python manage.py makemigrations"</h4>
<h4 align="center">7. migre os dados "python manage.py migrate"</h4>
<h4 align="center">7. crie um superuser "python manage.py createsuperuser"</h4>
<h4 align="center">8. rode o app "python manage.py runserver"</h4>
<h4 align="center">7. acesse a pagina admin</h4>
<a href='http://127.0.0.1:8000/admin' align="center">Admin</a>
<h4 align="center">7. crie um grupo de usuario chamado "user_admin" com todas as permissoes</h4>
<h4 align="center">7. crie um grupo de usuario chamado "user_common" sem nenhuma permissão</h4>
<h4 align="center">7. atribua ao super user criado anteriormente o grupo "user_admin"</h4>
<h4 align="center">7. acesse o site</h4>
<a href='http://127.0.0.1:8000/' align="center">Localhost</a>
