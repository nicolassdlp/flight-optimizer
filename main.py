from geopy.distance import great_circle

#Données des aéroports
airports = {
    "LFPG": (49.0097, 2.5479),
    "KJFK": (40.6413, -73.7781)
}

def calculate_distance(depart, arrive):
    depart_coord = airports.get(depart)
    arrive_coord = airports.get(arrive)

    #Calcul de la distance orthodromique (distance du grand cercle en km)
    distance = great_circle(depart_coord, arrive_coord).kilometers

    print(f"--- Vol {depart} -> {arrive} ---")
    print(f"Distance: {round(distance, 2)} km")

if __name__ == "__main__":
    calculate_distance("LFPG", "KJFK")