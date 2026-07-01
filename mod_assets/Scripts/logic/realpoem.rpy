init python:
    import os
    import sys
    import subprocess

    def crear_txt_desktop():
        escritorio = os.path.join(os.path.expanduser('~'), 'Desktop')
        if not os.path.exists(escritorio):
            escritorio = os.path.join(os.path.expanduser('~'), 'Escritorio')
            
        archivo_escritorio = os.path.join(escritorio, "poema.txt")
        
        try:
            with open(archivo_escritorio, "w", encoding="utf-8") as f:
                f.write(" ") 
        except Exception as e:
            pass

    def opengamebase():
        ruta = config.basedir
        try:
            if sys.platform == "win32":
                os.startfile(ruta)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", ruta])
            else:
                subprocess.Popen(["xdg-open", ruta])
        except Exception as e:
            pass

    def checar_poema():
        archivo_ruta = os.path.join(config.basedir, "poema.txt")
        if not os.path.exists(archivo_ruta):
            
            renpy.call("noexiste")
        
        try:
            with open(archivo_ruta, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
        except:
            
            renpy.call("noexiste")
            
        if not contenido:
            renpy.call("establanco")
        
        
        palabras = contenido.split()
        num_palabras = len(palabras)
        
        tiene_monika = "monika" in contenido or "Monika" in contenido
        
        if not tiene_monika:
            renpy.call("tienemonika")
        

        if num_palabras < 20:
            renpy.call("pocotexto")
        

        renpy.jump("a1_2")

# Borra el archivo poema.txt de la carpeta base
    def borrar_poematxt():
        archivo_ruta = os.path.join(config.basedir, "poema.txt")
        
        if os.path.exists(archivo_ruta):
            try:
                os.remove(archivo_ruta)
            except Exception as e:
                pass

label noexiste:
    call screen dialog(message="No esta el archivo poema.txt en la carpeta.\nVerifica si esta todo en orden", ok_action=Return())
    return 

label establanco:
    call screen dialog(message="Por favor, escribe tu poema.\nNo es tan dificil como parece", ok_action=Return())
    return

label tienemonika:
    call screen dialog(message="Monika dijo que la dedicaras en ella. escribe su nombre\n Esta la hará feliz", ok_action=Return())
    return
label pocotexto:
    call screen dialog(message="Falta mas, tu poema es demasiado corto, dale mas pasión al poema", ok_action=Return())
    return