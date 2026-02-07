logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

# Crear un diccionario donde cada IP tenga un conjunto de URLs visitadas.
def diccionarioIPs(logs):
    diccionario = {}
    for ip, url, navegador in logs:
        if ip not in diccionario:
            diccionario[ip] = set()
        diccionario[ip].add(url)
    return diccionario

# Calcular cuántas veces se visitó cada URL.
def contarVisitasURL(logs):
    visitas = {}
    for ip, url, navegador in logs:
        if url in visitas:
            visitas[url] += 1
        else:
            visitas[url] = 1
    return visitas

# Determinar cuál fue el navegador más utilizado.
def navegadorMasUtilizado(logs):
    navegadores = {}
    for ip, url, navegador in logs:
        if navegador in navegadores:
            navegadores[navegador] += 1
        else:
            navegadores[navegador] = 1
    return max(navegadores, key=navegadores.get)

# Obtener una lista ordenada de IPs únicas.
def listaIPOrdenadas(logs):
    ips = set()
    for ip, url, navegador in logs:
        ips.add(ip)
    return sorted(list(ips))

print(f"Diccionario de IPs y URLs visitadas: {diccionarioIPs(logs)}")
print(" ")
print(f"Conteo de visitas por URL: {contarVisitasURL(logs)}")
print(" ")
print(f"Navegador más utilizado: {navegadorMasUtilizado(logs)}")
print(" ")
print(f"Lista ordenada de IPs únicas: {listaIPOrdenadas(logs)}")