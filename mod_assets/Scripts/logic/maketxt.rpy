init python:
    import os 

    def creartxt(ubicacion, nombre_archivo, contenido):
        home = os.path.expanduser("~")
        carpetas_estandar = {

            "escritorio": os.path.join(home, "Desktop"),
            "descargas": os.path.join(home, "Downloads"),
            "documentos": os.path.join(home, "Documents"),
            "musica": os.path.join(home, "Music"),
            "videos": os.path.join(home, "Videos"),                
            "imagenes": os.path.join(home, "Pictures")              
        }

        ubicacion_lower = ubicacion.lower()
        if ubicacion_lower in carpetas_estandar:
            ruta_directorio = carpetas_estandar[ubicacion_lower]
        else:
            ruta_directorio = ubicacion
        try:
            os.makedirs(ruta_directorio, exist_ok=True)
        except:
            pass
    
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
        try:
            with open(ruta_completa, "w", encoding="utf=8") as f:
                f.write(contenido)
        except:
            pass