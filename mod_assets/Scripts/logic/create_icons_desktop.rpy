init python:
    import os
    import shutil
    import datetime

    # --- Función para mover los archivos reales ---
    def move_desktop_files(to_backup=True):
        escritorio = os.path.expanduser("~/Desktop")
        carpeta_backup = os.path.join(escritorio, "DesktopBackup_temp")
        
        # Archivos que NO queremos tocar (los tuyos)
        prefijo_tuyo = "hello_"

        if to_backup:
            # OCULTAR: Mover archivos originales a la carpeta temporal
            if not os.path.exists(carpeta_backup):
                os.makedirs(carpeta_backup)
            
            for archivo in os.listdir(escritorio):
                ruta_completa = os.path.join(escritorio, archivo)
                # Solo movemos lo que NO sea tu archivo hello_
                if not archivo.startswith(prefijo_tuyo) and archivo != "DesktopBackup_temp":
                    try:
                        shutil.move(ruta_completa, os.path.join(carpeta_backup, archivo))
                    except:
                        pass
        else:
            # RESTAURAR: Mover archivos de vuelta
            if os.path.exists(carpeta_backup):
                for archivo in os.listdir(carpeta_backup):
                    ruta_backup = os.path.join(carpeta_backup, archivo)
                    shutil.move(ruta_backup, os.path.join(escritorio, archivo))
                
                # Borrar la carpeta temporal
                try:
                    os.rmdir(carpeta_backup)
                except:
                    pass

    def create_icons_desktop():
        # --- 1. PREPARACIÓN ---
        directorio_base = config.basedir
        carpeta_temp = os.path.join(directorio_base, "temp")
        if not os.path.exists(carpeta_temp): os.makedirs(carpeta_temp)
        
        ruta_origen = os.path.join(directorio_base, "game", "mod_assets", "images", "hello.png")
        ruta_temp_img = os.path.join(carpeta_temp, "hello_temp.png")
        escritorio = os.path.expanduser("~/Desktop")

        if not os.path.exists(ruta_origen): return

        # --- 2. OCULTAR ICONOS REALES ---
        move_desktop_files(to_backup=True)

        # --- 3. CREAR TUS ICONOS ---
        shutil.copy(ruta_origen, ruta_temp_img)
        for i in range(1, 150):
            try:
                shutil.copy(ruta_temp_img, os.path.join(escritorio, f"hello_{i}.png"))
            except:
                pass

    def remove_icons_desktop():
        escritorio = os.path.expanduser("~/Desktop")
        
        # --- 1. ELIMINAR TUS ICONOS ---
        for i in range(1, 150):
            ruta_archivo = os.path.join(escritorio, f"hello_{i}.png")
            if os.path.exists(ruta_archivo):
                try:
                    os.remove(ruta_archivo)
                except:
                    pass

        # --- 2. RESTAURAR ICONOS REALES ---
        move_desktop_files(to_backup=False)