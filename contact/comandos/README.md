Iniciar o projeto Django 

```
python -m venv venv
.\.venv\Scripts\activate
pip install django
django-admin startproject project .

python manage.py startapp contact
python manage.py runserver

```
Configurando o git

```
git config --global user.name 'Walter Magni' 
git config --global user.email 'waltermagni@terra.com.br'
git config --global init.defaultBranch main
git init
git add . 
git commit - m  
```

```
python manage.py makemigrations
python manage.py migrate

```
Criando e modificando a senha de um super usuario Django

```
python manage.py createsuperuser
python manage.py changepassword admin
```
