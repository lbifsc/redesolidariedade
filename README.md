## Rede de Solidariedade

Projeto de Extensão IFSC 2021/2 - Rede Solidariedade

## Para Rodar o Projeto:

certifique-se que está na raiz do repositorio "[...]/redesolidariedade/"

1 - Crie e rode uma venv
```bash
  python -m venv venv
  venv/scripts/activate
```

2 - Instale o pip e os requirements
```bash
  python -m pip install --upgrade pip
  pip install -r requirements.txt
```

3 - Inicialize o banco de dados e os arquivos estáticos
```bash
  cd app
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
```

4 - Crie uma secret key para o arquivo .env
```bash
  SECRET_KEY = "coloque a secret key aqui"
```

5 - Crie um Super-Usuário e rode o projeto
```bash
  python manage.py createsuperuser
  python manage.py runserver
```

6 - Faça login com o usuário criado e cadastre uma Entidade e um Representante no módulo de grupos

7 - Atribua ao usuário do representante o papel de administrador atravez do módulo de grupos

8 - Acesse o django admin ( 127.0.0.1/admin ) e exclua o usuário criado em terminal

9 - agora é só logar com o usuario do representante. Por padrão o usuário é o nome do representante Ex.: "Joao Pedro" e a senha inicial é "novousuario"

Agora é só utilizar o sistema! Cadastre categorias e itens, famílias, integrantes famíliares e realize doações!

