# redesolidariedade
# Projeto de Extensão IFSC 2021/2 - Rede Solidariedade
<br>
<h2>Como rodar o projeto:</h2>
<br>
<p>1.Clone o repositorio</p>
<p>git clone https://github.com/lbifsc/redesolidariedade.git</p>
<br>
<p>2. Crie uma venv em c:/caminhodorepositorio/redesolidariedade/app</p>
<p>python -m venv myvenv</p>
<p>myvenv/scripts/activate</p>
<br>
<p>3.instale os requeriments</p>
<p>python -m pip install --upgrade pip</p>
<p>pip install -r requirements.txt</p>
<br>
<p>4.Realize as migrations</p>
<p>cd main</p>
<p>python manage.py makemigrations</p>
<p>python manage.py migrate</p>
<br>
<p>5.Inicie o servidor</p>
<p>python manage.py runserver</p>
<br>
<p>Agora só acessar o local host:</p>
<a href='http://127.0.0.1:8000/'>Localhost</a>
