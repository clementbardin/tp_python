from json import*
import csv

donnees_json = ("boisson.json")

with open(donnees_json, newline="", encoding="utf-8") as fichier_json:
    lecteur_json = load(fichier_json)

stock_csv = ("stock.csv")

with open(stock_csv, newline="", encoding="utf-8") as stock:
    lecteur_csv = csv.reader(stock)

    for ligne in lecteur_csv:
        print(ligne)

def main():
    while True:
        choice = int(displayMenu())
        match choice:
            case 1:
                requirePayment(2)
            case 2:
                requirePayment(2)
            case 3:
                requirePayment(3.5)
            case 4:
                requirePayment(4)
            case 5:
                requirePayment(4)
            case 6:
                requirePayment(5)
            case 7:
                requirePayment(6)
            case 0:
                break

        isContinue = input("Voulez-vous continuer ? y or n")
        if isContinue == "y":
            print("\n ------------------- \n")
        if isContinue == "n":
            break

    print("Passez une bonne journée.")


def displayMenu():
    print("1. Café noir | 2 coin")
    print("2. Café au lait | 2 coin")
    print("3. Chocolat au lait | 3.5 coin")
    print("4. Thé | 4 coin")
    print("5. Ice-Tea | 4 coin")
    print("6. Coca-Cola | 5 coin")
    print("7. Redbull | 6 coin")
    print("0. Quitter")
    choice = input("Bonjour, choisissez votre boisson : ")
    return int(choice)


def requirePayment(paymentAmount):
    balance = 0
    while balance < paymentAmount:
        print("Vous devez payer " + str(paymentAmount - balance) + " coins")
        print("1. 0.5 coin")
        print("2. 1 coin")
        print("3. 2 coins")
        choice = int(input("Insérez vos coins : "))
        if choice == 1:
            balance += 0.5
        if choice == 2:
            balance += 1
        if choice == 3:
            balance += 2

    if balance > paymentAmount:
        print("Votre monnaie : " + str(balance - paymentAmount))

main()
print(lecteur_json)