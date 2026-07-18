init python:
    import os
    import sys
    import datetime as dt
    import subprocess
    import ctypes

    # Variable global para almacenar el fondo de pantalla original antes de modificarlo
    backup_wallpaper = {
        "win32_path": None,
        "linux_commands": []
    }

    def escribir_log(mensaje):
        temp_dir = os.path.join(config.basedir, "temp")
        if not os.path.exists(temp_dir):
            try:
                os.makedirs(temp_dir)
            except Exception:
                pass 
        
        log_path = os.path.join(temp_dir, "wallpaperlog.txt")
        tiempo = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"[{tiempo}] {mensaje}\n")
        except:
            pass

    def detectar_wine():
        if sys.platform == "win32":
            try:
                ctypes.windll.ntdll.wine_get_version
                return True
            except AttributeError:
                return False
        return False

    def extraer_imagen_fisica(ruta_interna, ruta_destino):
        if not renpy.loadable(ruta_interna):
            escribir_log(f"Error: No se encontró el recurso '{ruta_interna}'.")
            return False
            
        try:
            archivo_interno = renpy.file(ruta_interna)
            with open(ruta_destino, "wb") as f_out:
                f_out.write(archivo_interno.read())
            archivo_interno.close()
            return True
        except Exception as e:
            escribir_log(f"Error crítico al extraer imagen: {e}")
            return False

    def obtener_salida_comando(comando):
        """Función auxiliar para leer la configuración de Linux antes de cambiarla."""
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            if resultado.returncode == 0:
                return resultado.stdout.strip()
        except:
            pass
        return None

    def cambiar_wallpaper_android(ruta_absoluta):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WallpaperManager = autoclass('android.app.WallpaperManager')
            BitmapFactory = autoclass('android.graphics.BitmapFactory')
            
            context = PythonActivity.mActivity
            wp_manager = WallpaperManager.getInstance(context)
            bitmap = BitmapFactory.decodeFile(ruta_absoluta)
            
            if bitmap:
                wp_manager.setBitmap(bitmap)
                escribir_log("Android: Wallpaper cambiado con éxito mediante WallpaperManager.")
                return True
            else:
                escribir_log("Android: Error al decodificar la imagen.")
                return False
        except Exception as e:
            escribir_log(f"Android: Error (¿Falta el permiso SET_WALLPAPER?): {e}")
            return False

    def ejecutar_comando_linux(comando, entorno_detectado):
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            if resultado.returncode == 0:
                escribir_log(f"Linux ({entorno_detectado}): Comando ejecutado exitosamente.")
            else:
                escribir_log(f"Linux ({entorno_detectado}): Fallo el comando. Log: {resultado.stderr.strip()}")
        except Exception as e:
            escribir_log(f"Linux ({entorno_detectado}): Error al lanzar subprocess: {e}")

    def change_wallpaper():
        global backup_wallpaper
        escribir_log("--- Iniciando función change_wallpaper() ---")
        
        ruta_interna = "mod_assets/images/btc.jpg"
        temp_dir = os.path.join(config.basedir, "temp")
        
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
            
        ruta_fisica = os.path.join(temp_dir, "btc.png")
        
        # 1. Obtener el archivo físico
        if not extraer_imagen_fisica(ruta_interna, ruta_fisica):
            escribir_log("Fallo: Deteniendo el proceso porque no hay archivo físico.")
            return
        
        ruta_absoluta = os.path.abspath(ruta_fisica).replace('\\', '/')
        escribir_log(f"Imagen preparada en ruta física: {ruta_absoluta}")

        # 2. Detectar Plataforma
        plataforma = sys.platform
        escribir_log(f"Sistema detectado por Python: {plataforma}")

        # Comprobar si estamos en Android
        if renpy.variant("touch") or renpy.android:
            escribir_log("Plataforma real detectada: Android")
            escribir_log("Aviso: En Android no se puede respaldar el fondo original por políticas del SO.")
            cambiar_wallpaper_android(ruta_absoluta)
            escribir_log("--- Fin del proceso hellopc() ---")
            return

        if plataforma == "win32":
            es_wine = detectar_wine()
            if es_wine:
                escribir_log("Plataforma real detectada: Linux ejecutando juego mediante WINE.")
                escribir_log("Aviso: Cambiar el wallpaper del host Linux desde adentro de Wine es inestable.")
                ruta_absoluta_wine = f"Z:{ruta_absoluta}" 
                try:
                    subprocess.run(f"z:/bin/sh -c \"gsettings set org.cinnamon.desktop.background picture-uri 'file://{ruta_absoluta}'\"", shell=True)
                    escribir_log("Intento de inyección de comando Linux a través de Wine enviado.")
                except Exception as e:
                    escribir_log(f"Fallo al escapar de Wine: {e}")
            else:
                escribir_log("Plataforma real detectada: Windows Nativo")
                
                # RESPALDO WINDOWS: Obtenemos el fondo actual antes de cambiarlo
                try:
                    SPI_GETDESKWALLPAPER = 115
                    buffer = ctypes.create_unicode_buffer(512)
                    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 512, buffer, 0)
                    backup_wallpaper["win32_path"] = buffer.value
                    escribir_log(f"Fondo original Windows respaldado exitosamente.")
                except Exception as e:
                    escribir_log(f"Fallo al respaldar fondo en Windows: {e}")

                # APLICACIÓN WINDOWS
                try:
                    ruta_win = ruta_absoluta.replace('/', '\\')
                    SPI_SETDESKWALLPAPER = 20
                    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, ruta_win, 3)
                    escribir_log("Windows: Comando SystemParametersInfoW ejecutado con éxito.")
                except Exception as e:
                    escribir_log(f"Windows: Error al ejecutar API: {e}")

        elif plataforma.startswith("linux"):
            escribir_log("Plataforma real detectada: Linux Nativo (.sh)")
            
            entorno_escritorio = os.environ.get("XDG_CURRENT_DESKTOP", os.environ.get("DESKTOP_SESSION", "desconocido")).lower()
            escribir_log(f"Entorno de escritorio detectado: {entorno_escritorio}")
            
            backup_wallpaper["linux_commands"] = [] # Limpiamos historial previo
            
            if "cinnamon" in entorno_escritorio:
                val = obtener_salida_comando("gsettings get org.cinnamon.desktop.background picture-uri")
                if val: backup_wallpaper["linux_commands"].append(f"gsettings set org.cinnamon.desktop.background picture-uri {val}")
                ejecutar_comando_linux(f"gsettings set org.cinnamon.desktop.background picture-uri 'file://{ruta_absoluta}'", "Cinnamon")
                
            elif "gnome" in entorno_escritorio:
                val_light = obtener_salida_comando("gsettings get org.gnome.desktop.background picture-uri")
                val_dark = obtener_salida_comando("gsettings get org.gnome.desktop.background picture-uri-dark")
                if val_light: backup_wallpaper["linux_commands"].append(f"gsettings set org.gnome.desktop.background picture-uri {val_light}")
                if val_dark: backup_wallpaper["linux_commands"].append(f"gsettings set org.gnome.desktop.background picture-uri-dark {val_dark}")
                ejecutar_comando_linux(f"gsettings set org.gnome.desktop.background picture-uri 'file://{ruta_absoluta}'", "GNOME (Claro)")
                ejecutar_comando_linux(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{ruta_absoluta}'", "GNOME (Oscuro)")
                
            elif "mate" in entorno_escritorio:
                val = obtener_salida_comando("gsettings get org.mate.background picture-filename")
                if val: backup_wallpaper["linux_commands"].append(f"gsettings set org.mate.background picture-filename {val}")
                ejecutar_comando_linux(f"gsettings set org.mate.background picture-filename '{ruta_absoluta}'", "MATE")
                
            elif "xfce" in entorno_escritorio:
                val = obtener_salida_comando("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image")
                if val: backup_wallpaper["linux_commands"].append(f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s '{val}'")
                comando = f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s '{ruta_absoluta}' --create --type string"
                ejecutar_comando_linux(comando, "XFCE4 (MONITOR 0)")
                comando_all = f"for prop in $(xfconf-query -c xfce4-desktop -p /backdrop -l | grep last-image); do xfconf-query -c xfce4-desktop -p $prop -s '{ruta_absoluta}'; done"
                ejecutar_comando_linux(comando_all, "XFCE4 (Todos los Monitores)")
                
            elif "kde" in entorno_escritorio or "plasma" in entorno_escritorio:
                escribir_log("Aviso: KDE no admite respaldo directo y sencillo desde CLI sin un script avanzado.")
                script_kde = f"var Desktops = desktops(); for (i=0;i<Desktops.length;i++) {{ d = Desktops[i]; d.wallpaperPlugin = 'org.kde.image'; d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); d.writeConfig('Image', 'file://{ruta_absoluta}'); }}"
                comando = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \"{script_kde}\""
                ejecutar_comando_linux(comando, "KDE Plasma")
                
            elif "lxde" in entorno_escritorio:
                ejecutar_comando_linux(f"pcmanfm --set-wallpaper '{ruta_absoluta}'", "LXDE")
                
            elif "hyprland" in entorno_escritorio:
                ejecutar_comando_linux(f"hyprctl hyprpaper preload '{ruta_absoluta}' && hyprctl hyprpaper wallpaper ',{ruta_absoluta}'", "Hyprland (Hyprpaper)")
            else:
                escribir_log(f"Linux: Entorno '{entorno_escritorio}' no emparejado directamente. Intentando feh como fallback.")
                ejecutar_comando_linux(f"feh --bg-scale '{ruta_absoluta}'", "Fallback (feh)")

        escribir_log("--- Fin del proceso hellopc() ---")

    def restore_wallpaper():
        global backup_wallpaper
        escribir_log("--- Iniciando función restore_wallpaper() ---")
        
        plataforma = sys.platform

        if renpy.variant("touch") or renpy.android:
            escribir_log("Android: Restaurar fondo de pantalla original no está soportado (limitaciones para extraer o clonar el Bitmap en uso).")
            escribir_log("--- Fin del proceso restorepc() ---")
            return

        if plataforma == "win32":
            es_wine = detectar_wine()
            if not es_wine:
                if backup_wallpaper.get("win32_path"):
                    try:
                        SPI_SETDESKWALLPAPER = 20
                        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, backup_wallpaper["win32_path"], 3)
                        escribir_log("Windows: Fondo original restaurado con éxito.")
                        try:
                            with open(os.path.join(config.basedir, "wallpaper_backup.txt"), "w") as f:
                                f.write(backup_wallpaper["win32_path"])
                        except:                 
                            pass
                    except Exception as e:
                        escribir_log(f"Windows: Error al restaurar mediante la API: {e}")
                else:
                    escribir_log("Windows: No se encontró una ruta original guardada para restaurar.")
            else:
                escribir_log("Linux (Wine): Restauración automatizada no soportada a través de Wine.")

        elif plataforma.startswith("linux"):
            comandos_restauracion = backup_wallpaper.get("linux_commands", [])
            if comandos_restauracion:
                for cmd in comandos_restauracion:
                    ejecutar_comando_linux(cmd, "Restauración")
            else:
                escribir_log("Linux: No hay comandos de restauración guardados para este entorno.")
                
        escribir_log("--- Fin del proceso restorepc() ---")