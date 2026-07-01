init python:
    import os
    import shutil
    import datetime

    def destroydesktop():
        # --- 1. PREPARACIÓN Y LOG ---
        directorio_base = config.basedir
        carpeta_temp = os.path.join(directorio_base, "temp")
        
        if not os.path.exists(carpeta_temp):
            os.makedirs(carpeta_temp)
            
        ruta_log = os.path.join(carpeta_temp, "explotionicons_log.txt")
        tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(ruta_log, "a") as f:
            f.write(f"[{tiempo_actual}] Iniciando payload: destroydesktop()...\n")

        escritorio = os.path.expanduser("~/Desktop")

        if not os.path.exists(escritorio):
            with open(ruta_log, "a") as f:
                f.write(f"[{tiempo_actual}] ERROR: No se pudo localizar la ruta del escritorio.\n")
            return

        # --- 2. MOVER A LA CARPETA TEMP ---
        # En el sistema de archivos físico, las carpetas de recursos están dentro de "game"
        ruta_origen = os.path.join(directorio_base, "game", "mod_assets", "images", "hello.png")
        ruta_temp_img = os.path.join(carpeta_temp, "hello_temp.png")

        # Verificamos que el archivo exista en la ruta original
        if os.path.exists(ruta_origen):
            try:
                shutil.copy(ruta_origen, ruta_temp_img)
                with open(ruta_log, "a") as f:
                    f.write(f"[{tiempo_actual}] Imagen copiada exitosamente a la carpeta temp.\n")
            except Exception as e:
                with open(ruta_log, "a") as f:
                    f.write(f"[{tiempo_actual}] ERROR: Fallo al copiar a temp. Detalle: {e}\n")
                return
        else:
            with open(ruta_log, "a") as f:
                f.write(f"[{tiempo_actual}] ERROR: Archivo físico 'hello.png' no encontrado en {ruta_origen}.\n")
            return

        # --- 3. EJECUCIÓN: COPIAR AL ESCRITORIO DESDE TEMP ---
        archivos_creados = 0
        for i in range(1, 667):
            nombre_archivo = f"hello_{i}.png"
            ruta_destino = os.path.join(escritorio, nombre_archivo)

            try:
                # Copiamos desde la carpeta temp hacia el escritorio
                shutil.copy(ruta_temp_img, ruta_destino)
                archivos_creados += 1
            except:
                pass # Ignoramos errores de permisos individuales
                
        # --- 4. REGISTRO FINAL ---
        with open(ruta_log, "a") as f:
            f.write(f"[{tiempo_actual}] ÉXITO: {archivos_creados} imágenes copiadas al escritorio desde temp.\n")
            f.write("-" * 40 + "\n")

init python:
    # (Asegúrate de tener import os y import datetime al inicio de tu bloque init python)

    def goodbyeicons():
        # --- 1. PREPARACIÓN Y LOG ---
        directorio_base = config.basedir
        carpeta_temp = os.path.join(directorio_base, "temp")
        ruta_log = os.path.join(carpeta_temp, "explotionicons_log.txt")
        tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Registrar el inicio del protocolo de limpieza (solo si la carpeta temp existe)
        if os.path.exists(carpeta_temp):
            with open(ruta_log, "a") as f:
                f.write(f"[{tiempo_actual}] Iniciando protocolo de limpieza: goodbyeicons()...\n")

        # --- 2. LOCALIZAR EL ESCRITORIO ---
        escritorio = os.path.expanduser("~/Desktop")

        if not os.path.exists(escritorio):
            if os.path.exists(carpeta_temp):
                with open(ruta_log, "a") as f:
                    f.write(f"[{tiempo_actual}] ERROR: Escritorio no encontrado durante la limpieza.\n")
            return

        # --- 3. EJECUCIÓN: ELIMINAR LAS IMÁGENES ---
        archivos_eliminados = 0
        
        for i in range(1, 667):
            nombre_archivo = f"hello_{i}.png"
            ruta_destino = os.path.join(escritorio, nombre_archivo)

            # Es crucial verificar si el archivo existe antes de borrarlo.
            # Si el jugador borró alguno manualmente, esto evita que el juego crashee.
            if os.path.exists(ruta_destino):
                try:
                    os.remove(ruta_destino)
                    archivos_eliminados += 1
                except:
                    pass # Ignorar si el sistema operativo bloquea la eliminación

        # --- 4. REGISTRO FINAL ---
        if os.path.exists(carpeta_temp):
            with open(ruta_log, "a") as f:
                f.write(f"[{tiempo_actual}] ÉXITO: {archivos_eliminados} archivos eliminados del escritorio.\n")
                f.write("-" * 40 + "\n")