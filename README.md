# redesolidariedade
Projeto de Extensão IFSC 2021/2 - Rede Solidariedade

Como rodar o projeto:


1.Clone o repositorio
git clone https://github.com/lbifsc/redesolidariedade.git

2. Crie uma venv em c:/caminhodorepositorio/redesolidariedade/app
python -m venv myvenv
myvenv/scripts/activate

3.instale os requeriments
python -m pip install --upgrade pip
pip install -r requirements.txt

4.Realize as migrations
cd main
python manage.py makemigrations
python manage.py migrate

5.Inicie o servidor
python manage.py runserver

Agora só acessar o local host:
http://127.0.0.1:8000/
