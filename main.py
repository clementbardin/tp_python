from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from fonction_email import envoyer_email


class DistributeurApp(App):
    def build(self):
        self.layout = FloatLayout()

        self.label_prix = Label(text="Prix : $0.0", size_hint=(None, None), pos=(50, 350))
        self.layout.add_widget(self.label_prix)

        self.label_montant_inseré = Label(text="Montant inséré : $0.0", size_hint=(None, None), pos=(50, 300))
        self.layout.add_widget(self.label_montant_inseré)

        self.bouton_retour_monnaie = Button(text="Retour de monnaie", size_hint=(None, None), size=(150, 50),
                                            pos=(50, 250))
        self.bouton_retour_monnaie.bind(on_press=self.retour_monnaie)
        self.layout.add_widget(self.bouton_retour_monnaie)

        self.boutons_produits = []

        self.ajouter_produit("Café", 0.3)
        self.ajouter_produit("Thé", 0.25)
        self.ajouter_produit("Cappuccino", 0.3)  # Remplacé "Soda" par "Cappuccino" avec un prix de 0.3
        self.ajouter_produit("Eau", 0.2)

        self.boutons_argent = []

        self.ajouter_bouton_argent(0.05)
        self.ajouter_bouton_argent(0.1)
        self.ajouter_bouton_argent(0.2)
        self.ajouter_bouton_argent(0.5)

        self.bouton_acheter = Button(text="Acheter", size_hint=(None, None), size=(150, 50), pos=(50, 50))
        self.bouton_acheter.bind(on_press=self.acheter_produit)
        self.layout.add_widget(self.bouton_acheter)

        self.montant_inseré = 0.0
        self.prix_produit_selectionné = 0.0

        return self.layout

    def ajouter_produit(self, nom_produit, prix_produit):
        bouton = Button(text=nom_produit, size_hint=(None, None), size=(150, 50),
                        pos=(50, 200 - len(self.boutons_produits) * 50))
        bouton.bind(on_press=self.selectionner_produit)
        bouton.nom_produit = nom_produit
        bouton.prix_produit = prix_produit
        self.layout.add_widget(bouton)
        self.boutons_produits.append(bouton)

    def ajouter_bouton_argent(self, montant):
        bouton = Button(text=f"Inserer ${montant:.2f}", size_hint=(None, None), size=(150, 50),
                        pos=(250, 200 - len(self.boutons_argent) * 50))
        bouton.bind(on_press=lambda instance, montant=montant: self.inserer_argent(montant))
        self.layout.add_widget(bouton)
        self.boutons_argent.append(bouton)

    def selectionner_produit(self, instance):
        self.prix_produit_selectionné = instance.prix_produit
        self.nom_produit_selectionné = instance.nom_produit  # Stocker le nom du produit sélectionné
        self.label_prix.text = f"Prix : ${self.prix_produit_selectionné:.2f}"

    def inserer_argent(self, montant):
        self.montant_inseré += montant
        self.maj_montant_inseré()

    def acheter_produit(self, instance):
        if self.prix_produit_selectionné <= self.montant_inseré:
            self.montant_inseré -= self.prix_produit_selectionné
            self.label_prix.text = f"Prix : $0.0"
            self.maj_montant_inseré()

            envoyer_email(destinataire, sujet, message)
        else:
            montant_restant = self.prix_produit_selectionné - self.montant_inseré
            self.label_prix.text = f"Prix : ${self.prix_produit_selectionné:.2f}"
            self.label_prix.text += f"\nMontant inséré : ${self.montant_inseré:.2f}"
            self.label_prix.text += f"\nMontant à rembourser : ${montant_restant:.2f}"

    def retour_monnaie(self, instance):
        self.montant_inseré = 0.0
        self.label_montant_inseré.text = f"Montant inséré : ${self.montant_inseré:.2f}"

    def maj_montant_inseré(self):
        self.label_montant_inseré.text = f"Montant inséré : ${self.montant_inseré:.2f}"


if __name__ == '__main__':
    app = DistributeurApp()
    app.run()