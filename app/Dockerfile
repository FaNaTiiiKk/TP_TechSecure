# Utilisation d'une image Python légère et stable
FROM python:3.10-slim

# Définition du dossier de travail dans le conteneur
WORKDIR /app

# Copie du fichier des dépendances
COPY requirements.txt requirements.txt

# Installation des packages Python requis
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout le reste du code de l'application (app.py, templates, static)
COPY . .

# Exposition du port interne utilisé par Flask
EXPOSE 5000

# Commande de lancement de l'application Flask
CMD ["python", "app.py"]