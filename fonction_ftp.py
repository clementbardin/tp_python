# Code pour l'accès au serveur FTP et le téléchargement du fichier menu.json
from ftplib import FTP

def telecharger_menu():
    hote_ftp = 'ftp.example.com'  # Remplacez par le serveur FTP approprié
    nom_utilisateur = 'votre_nom_utilisateur'
    mot_de_passe = 'votre_mot_de_passe'

    try:
        ftp = FTP(hote_ftp)
        ftp.login(nom_utilisateur, mot_de_passe)
        ftp.cwd('Jeudi')  # Accédez au dossier "Jeudi" sur le serveur FTP

        with open('menu.json', 'wb') as f:
            ftp.retrbinary('RETR menu.json', f.write)

        ftp.quit()
        print("Fichier menu.json téléchargé avec succès !")
    except Exception as e:
        print(f"Erreur lors du téléchargement de menu.json : {str(e)}")

# Exemple d'utilisation :
# telecharger_menu()
