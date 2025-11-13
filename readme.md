## En cas de redemarrage ou de plantage de terminal, on dois toujours remettre l'envioronnement virtuel en route :

- se mettre a la racine du projet et taper :

```bash
source env/bin/activate
## ce qui affichera (env) devant le chemin du terminal
(env) romkappa@debian:~/workspace/django-web-app  main✔$
```

## Installer django si ce n'est pas deja fait sur votre machine :

```bash
pip install django
```

## Initialiser un projet django de base avec la commande suivant :

```bash
django-admin startproject merchex
```

## Ensuite installer ce qu'on appelle 'application' dans le projet, par exemple ici une liste de marchandise (ca permet de scinder le projet en plusieurs applications et de ce que j'aéi compris elle serait reutilisable par d'autres projet, a veridfier):

```bash
python manage.py startapp listings
```

- ensuite ajouter cette application dans le fichier settings.py dans la setcion, INSTALLED_APPS = [
  listings,

## Une fois un model créé (voir fichier models.py) on doit cree et appliqué une migration :

```bash
python manage.py makemigrations
python manage.py migrate
```
