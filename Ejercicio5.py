partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

# Calcular el total de puntos por jugador.
def puntosPorJugador(partidas):
    puntos_jugadores = {}
    for jugador, mapa, puntos in partidas:
        if jugador in puntos_jugadores:
            puntos_jugadores[jugador] += puntos
        else:
            puntos_jugadores[jugador] = puntos
    return puntos_jugadores
# Obtener un conjunto con los mapas jugados.
def mapasJugados(partidas):
    mapas = set()
    for jugador, mapa, puntos in partidas:
        mapas.add(mapa)
    return mapas
# Calcular el promedio de puntos por jugador.
def promedioPuntos(partidas):
    puntos_jugadores = {}
    partidas_jugadores = {}
    for jugador, mapa, puntos in partidas:
        if jugador in puntos_jugadores:
            puntos_jugadores[jugador] += puntos
            partidas_jugadores[jugador] += 1
        else:
            puntos_jugadores[jugador] = puntos
            partidas_jugadores[jugador] = 1
    return {jugador: puntos_jugadores[jugador] / partidas_jugadores[jugador] for jugador in puntos_jugadores}
# Determinar en qué mapa se obtuvieron más puntos en total
def mapaMayorPuntos(partidas):
    puntos_mapas = {}
    for jugador, mapa, puntos in partidas:
        if mapa in puntos_mapas:
            puntos_mapas[mapa] += puntos
        else:
            puntos_mapas[mapa] = puntos
    return max(puntos_mapas, key=puntos_mapas.get)

print(f"Puntos totales por jugador: {puntosPorJugador(partidas)}")
print(" ")
print(f"Mapas jugados: {mapasJugados(partidas)}")
print(" ")
print(f"Promedio de puntos por jugador: {promedioPuntos(partidas)}")
print(" ")
print(f"El mapa con más puntos en total es: {mapaMayorPuntos(partidas)}")
