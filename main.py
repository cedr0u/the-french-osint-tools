import requests
import json
from colorama import Fore, Style

print("T.F.O.T")
print("The.French.Osint.Tools")
print()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def menu():
    print("[1] Education")
    print("[v] Version")
    print("[exit] quitter")

menu()
choix_menu = str(input(Fore.RED + "Entrez votre choix : "))
print(Style.RESET_ALL)

def menu_Education():
    def menu_Education_print():
        print("[1] info/annuaire établissements")
        print("[2] stats taille colleges et lycees")
        print("[3] calendrier scolaire")
        print("[4] jours feries")
        print("[exit] quitter")

    print()
    menu_Education_print()
    choix_menu_Education = str(input(Fore.RED + "Entrez votre choix : "))
    print(Style.RESET_ALL)

    while choix_menu_Education != "exit":
        if choix_menu_Education == "1":
            print("API info établissements")
            limite = str(input(Fore.BLUE + "Entrez la limite du nombre de resultats [100 max] : "))
            where = str("\"" + (input(Fore.BLUE + "Entrez la ville ou village : ")) + "\"")
            print(Style.RESET_ALL)
            parameters = {
            "limit": limite,
            "where": where}
            response = requests.get("https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/records", params=parameters)
            jprint(response.json())
        elif choix_menu_Education == "2":
            print("API Taille des collèges et des lycées")
            limite = str(input(Fore.BLUE + "Entrez la limite du nombre de resultats [100 max] : "))
            offset = str(input(Fore.BLUE + "Entrez le decalage ou l'index du premier résultat : "))
            print(Style.RESET_ALL)
            parameters = {
            "limit": limite,
            "offset": offset}
            response = requests.get("https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-taille-colleges-lycees/records", params=parameters)
            jprint(response.json())
        elif choix_menu_Education == "3":
            print("API calendrier scolaire")
            limite = 100
            where = str("\"" + (input(Fore.BLUE + "Entrez la region ou tres grande ville proche : ")) + "\"")
            print(Style.RESET_ALL)
            parameters = {
            "limit": limite,
            "where": where}
            response = requests.get("https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-calendrier-scolaire/records", params=parameters)
            jprint(response.json())
        elif choix_menu_Education == "4":
            print("API jours feries")
            zones = str(input(Fore.BLUE + "Entrez la zone [ metropole, alsace-moselle, guadeloupe, guyane, la-reunion, martinique, mayotte, nouvelle-caledonie, polynesie-francaise, saint-barthelemy, saint-martin, saint-pierre-et-miquelon, wallis-et-futuna ] : "))
            annes = str(input(Fore.BLUE + "Entrez l'annee résultats [ exemple: 2023 ] : "))
            print(Style.RESET_ALL)
            response = requests.get(f'https://calendrier.api.gouv.fr/jours-feries/{zones}/{annes}.json')
            jprint(response.json())
        else :
            print("choix invalide")
    
        print()
        menu_Education_print()
        choix_menu_Education = str(input(Fore.RED + "Entrez votre choix : "))
        print(Style.RESET_ALL)

while choix_menu != "exit":
    if choix_menu == "1":
        menu_Education()
    elif choix_menu == "v":
        print("version 0.3")
        print("04/09/23")
    else :
        print("choix invalide")

    print()
    menu()
    choix_menu = str(input(Fore.RED + "Entrez votre choix : "))
    print(Style.RESET_ALL)

print("cedrou, 2023")