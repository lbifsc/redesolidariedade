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
<h4 align="center">1. certifique-se que está na raiz do repositorio [...]/redesolidariedade/"</h4>
<h4 align="center">2. crie uma venv "python -m venv venv"</h4>
<h4 align="center">3. ative a venv "venv\Scripts\activate"</h4>
<h4 align="center">4. instale o pip "python -m pip install --upgrade pip"</h4>
<h4 align="center">5. instale os requirements.txt "pip install -r requirements.txt"</h4>
<h4 align="center">6. va para a pasta app "cd app" </h4>
<h4 align="center">7. va para a raiz do app "cd main"</h4>
<h4 align="center">8. faça as migrations "python manage.py makemigrations"</h4>
<h4 align="center">9. migre os dados "python manage.py migrate"</h4>
<h4 align="center">10. crie um superuser "python manage.py createsuperuser"</h4>
<h4 align="center">11. Você deve gerar uma secretkey para o arquivo .env, que por padrão vai estar vazia.</h4>
<h4 align="center">12. rode o app "python manage.py runserver"</h4>
<h4 align="center">13. acesse a pagina <a href='http://127.0.0.1:8000/admin' target="_blank">Admin</a></h4>
<h4 align="center">14. crie um grupo de usuario chamado "user_admin" com todas as permissoes</h4>
<h4 align="center">15. crie um grupo de usuario chamado "user_common" sem nenhuma permissão</h4>
<h4 align="center">16. atribua ao super user criado anteriormente o grupo "user_admin"</h4>
<h4 align="center">17. acesse o <a href='http://127.0.0.1:8000/' target="_blank">Site</a></h4>
