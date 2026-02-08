#Version de pyton
FROM python:3.10-slim

#Dossier de travail dans le conteneur
WORKDIR /app

#Copie du fichier des dépendances
COPY requirements.txt .

#Installation des bibliothèques présentes dans le ficheir requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Copie de tout le reste du code
COPY . .

#Commande qui se lance au démarrage du conteneur
CMD ["python", "main.py"]