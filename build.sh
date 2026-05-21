#!/usr/bin/env bash
# Lopeta skriptin suoritus heti, jos jokin komento epäonnistuu
set -o errexit

# 1. Päivitetään pip ja asennetaan riippuvuudet
pip install --upgrade pip
pip install -r requirements.txt

# 2. Kerätään staattiset tiedostot (esim. WhiteNoiselle)
python manage.py collectstatic --no-input

# 3. Ajetaan tietokantamigraatiot Renderin PostgreSQL-tietokantaan
python manage.py migrate
