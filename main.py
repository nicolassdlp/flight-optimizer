from geopy.distance import great_circle
from jupyter_server.utils import fetch

#Données des aéroports (ça reprensente une base de donnée qui sera ensuite transformée en base de donnée mysql
airports = {
    "LFPG": (49.0097, 2.5479),
    "KJFK": (40.6413, -73.7781),
    "LFMN": (43.6653, 7.2150)
}

#Déclaration des modèles d'avions (on prend un A32O)  (modele de mini base de données)
avions_performances = {
    "vitesse_kmh": 850,
    "consomation_kg/h": 2400,
}

def calculate_flight(dep_conso, arr_conso):
    dep_coord = airports.get(dep_conso)
    arr_coord = airports.get(arr_conso)

    if not dep_coord or not arr_coord:
        return "Aéroport Inconnu"

    #Calcul de la distance
    distance_km = great_circle(dep_coord, arr_coord).kilometers

    #Calcul du temps de vol (Temps = Distance / Vitesse)
    #Le résultat est en heures décimales (ex: 1.5 = 1h30)
    temps_vol = distance_km / avions_performances["vitesse_kmh"]

    #Calcul de la consommation (Carburant = Temps * Consommation horaire)
    consommation_kg = temps_vol * avions_performances["consomation_kg/h"]

    #Affichage des résultats dans la console
    print(f"\n--- Rapport de vol : {dep_conso} -> {arr_conso} ---")
    print(f"Distance : {distance_km:.2f} km")
    print(f"Temps de vol : {temps_vol:.2f} h")
    print(f"Consommation de carburant : {consommation_kg:.2f} kg")
    print("-" * 40)

if __name__ == "__main__":
    calculate_flight("LFPG", "KJFK")