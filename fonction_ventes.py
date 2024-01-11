import yaml
from ftplib import FTP
import json

def telecharger_menu():
    hote_ftp = 'ftp.example.com'
    nom_utilisateur = 'votre_nom_utilisateur'
    mot_de_passe = 'votre_mot_de_passe'

    try:
        ftp = FTP(hote_ftp)
        ftp.login(nom_utilisateur, mot_de_passe)
        ftp.cwd('Jeudi')

        with open('menu.json', 'wb') as f:
            ftp.retrbinary('RETR menu.json', f.write)

        ftp.quit()
        
        with open('menu.json', 'r') as f:
            menu = json.load(f)
            return [(item['nom'], item['prix']) for item in menu]

    except Exception as e:
        print(f"Erreur lors du téléchargement du menu : {str(e)}")
        return []

def enregistrer_ventes_yaml(ventes, fichier_chemin):
    with open(fichier_chemin, 'w') as file:
        yaml.dump(ventes, file)
