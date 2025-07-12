# 🌍 IP Logger + Rastreador GPS en Tiempo Real

Una aplicación educativa desarrollada en Python (usando Flask y Ngrok) que permite:

- Detectar la IP pública de quien accede al sitio.
- Obtener su ubicación aproximada por IP (ciudad, país, coordenadas IP, ISP).
- Solicitar permiso del navegador para capturar ubicación GPS en tiempo real.
- Guardar toda la información en archivos `.txt` separados.

> ⚠️ Este proyecto es solo con fines académicos y debe usarse con consentimiento del visitante.

---

## 📦 Archivos generados

| Archivo           | Contenido                                                  |
|-------------------|-------------------------------------------------------------|
| `ips.txt`         | IP, ciudad, región, país, coordenadas IP, ISP               |
| `rastro_gps.txt`  | Coordenadas GPS precisas en tiempo real, IP, enlace a mapa |

---

## 🚀 Requisitos

- Python 3.7 o superior
- [Ngrok](https://ngrok.com/)
- Cuenta en [ipinfo.io](https://ipinfo.io/) (opcional)
- Navegador moderno (Chrome, Firefox, Edge, etc.)

---

## 🔧 Instalación

1. Clona este repositorio o copia los archivos a tu máquina:

```bash
git clone https://github.com/Brxyden2007/IPLogger.git
cd IP logger
```

2. Instala las dependencias:

```bash
pip install flask pyngrok requests
```

3. Conecta tu cuenta de Ngrok (si no lo has hecho):

```bash
ngrok config add-authtoken TU_AUTHTOKEN
```

---

## ▶️ Cómo usar

1. Ejecuta el archivo principal:

```bash
python ip_logger.py
```

2. El script iniciará Flask localmente y abrirá un túnel con Ngrok:

```
[+] Enlace público generado por ngrok: https://ejemplo.ngrok.io
```

3. Comparte ese enlace con tus compañeros de prueba.  
   Cuando entren, se detectará su IP y se solicitará acceso a su GPS.

4. Toda la información se irá guardando automáticamente en los archivos:

```
ips.txt
rastro_gps.txt
```

---

## 📍 ¿Qué detecta exactamente?

### Desde IP pública:

- Dirección IP
- Ciudad
- Región / Estado
- País
- Coordenadas IP
- Proveedor de Internet (ISP)

### Desde GPS (solo si el visitante acepta):

- Coordenadas exactas en tiempo real (latitud, longitud)
- Mapa con enlace a Google Maps

---

## 🛡️ Legalidad y ética

Este proyecto está diseñado para **demostrar conceptos educativos sobre geolocalización y privacidad**. No debe usarse sin consentimiento informado del visitante.

---

## ✨ Autor

**Nombre:** Brayden Poveda  
**Correo:** braydenpoveda@gmail.com
**GitHub:** [@Brxyden2007](https://github.com/Brxyden2007)

---

## 📝 Licencia

MIT License – libre para usar, modificar y distribuir con atribución.
