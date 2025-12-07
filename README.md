# Tilavaraus

Tilavarausjärjestelmä Django-projektina


Visual Studio Coden asennus https://code.visualstudio.com/

Python extensions-plugin Visual Studio Codeen https://marketplace.visualstudio.com/items?itemName=ms-python.python

Pythonin asennus https://www.python.org/downloads/

Virtuaaliympäristön luominen tapahtuu komennolla 'py -3 -m venv .venv' ja aktivointi komennolla '.venv\scripts\activate'.

Pythonin laajennusten asennustyökalu pip asennetaan komennolla 'python -m pip install --upgrade pip'.

Django asennetaan komennolla 'python -m pip install django'.

Django-projektin pohjan voi luoda komennolla 'django-admin startproject projektin_nimi'. Tämä generoi kansioon projektin minimisisällön.

Migraatioiden tekemiseen käytetään komentoja 'python manage.py makemigrations' ja 'python manage.py migrate'.

Projektin käynnistys tapahtuu komennolla 'python manage.py runserver'.

Django REST Frameworkin ottaminen käyttöön tapahtuu komennolla 'pip install djangorestframework' ja lisäämällä 'setting.py' -tiedoston 'INSTALLED_APPS'-osioon 'rest_framework'.

Superuser-tunnuksen luominen tapahtuu komennolla 'manage.py createsuperuser'.
