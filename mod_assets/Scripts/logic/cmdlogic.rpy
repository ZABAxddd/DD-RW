default tiempo_cmd = 0

# Pantalla del temporizador y el video de fondo
screen pantalla_video_cmd():
    # Tu video en bucle (asegúrate de tener un video en formato .webm o .ogv en tu carpeta /game)
    # add "tu_video_estatico.webm" 

    # El temporizador interno de Ren'Py
    timer 1.0 action If(tiempo_cmd > 0, SetVariable("tiempo_cmd", tiempo_cmd - 1)) repeat True
    
    # Formateo a reloj (ej. 01:15)
    $ min = int(tiempo_cmd // 60)
    $ seg = int(tiempo_cmd % 60)
    
    text "[min:02d]:[seg:02d]" size 60 color "#ff0000" bold True align (0.5, 0.5)


init python:
    import os
    import sys
    import subprocess
    import json

    def preparar_evento_cmd(dialogos_inicio, dialogos_exito, dialogos_fallo, contenido_bat):
        basedir = config.basedir
        
        # 1. Crear el salvation.bat en la carpeta /game
        ruta_bat = os.path.join(basedir, "game", "salvation.bat")
        with open(ruta_bat, "w", encoding="utf-8") as f:
            f.write(contenido_bat)

        # 2. Asegurarse de que el canal de comunicación esté limpio
        ruta_flag = os.path.join(basedir, "cmd_flag.txt")
        if os.path.exists(ruta_flag):
            os.remove(ruta_flag)

        # 3. Construimos el código del CMD
        ruta_py = os.path.join(basedir, "monika_terminal.py")
        
        codigo_py = f"""import sys, time, os, threading

def slow_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

basedir = {repr(basedir)}
flag_file = os.path.join(basedir, "cmd_flag.txt")

intro = {json.dumps(dialogos_inicio)}
exito = {json.dumps(dialogos_exito)}
fallo = {json.dumps(dialogos_fallo)}

print("\\n")
for line in intro:
    slow_print(line)

input_result = [None]
def get_input():
    while True:
        try:
            val = input("\\nArrastra Salvation.bat aqui y presiona Enter > ")
            val = val.strip('"').strip("'").strip()
            if val.lower().endswith("salvation.bat"):
                input_result[0] = val
                break
            else:
                print("Ese no es el archivo correcto. Intenta de nuevo.")
        except:
            pass

t = threading.Thread(target=get_input)
t.daemon = True
t.start()

timeout_triggered = False
while t.is_alive():
    if os.path.exists(flag_file):
        with open(flag_file, "r", encoding="utf-8") as f:
            if "TIMEOUT" in f.read():
                timeout_triggered = True
                break
    time.sleep(0.2)

if timeout_triggered:
    print("\\n")
    for line in fallo:
        slow_print(line)
    time.sleep(3)
    os._exit(0)
else:
    print("\\n[Ejecutando script local...]")
    os.system('"' + input_result[0] + '"')
    print("\\n")
    for line in exito:
        slow_print(line)
        
    with open(flag_file, "w", encoding="utf-8") as f:
        f.write("SUCCESS")
    time.sleep(3)
    os._exit(0)
"""
        with open(ruta_py, "w", encoding="utf-8") as f:
            f.write(codigo_py)

        # 4. SOLUCIÓN AL ERROR DE VENTANA OCULTA
        # Obtenemos la ruta del ejecutable de Python de Ren'Py
        ejecutable_python = sys.executable
        
        if sys.platform == "win32":
            # Si Ren'Py está usando el ejecutable "invisible" (pythonw.exe), lo cambiamos al ejecutable "visible" (python.exe)
            if ejecutable_python.lower().endswith("pythonw.exe"):
                ejecutable_python = ejecutable_python[:-5] + ".exe"
            
            # Forzamos la apertura de una nueva ventana de comandos CMD real usando 'start'
            # Usamos una estructura de comillas dobles segura para rutas con espacios comunes en Windows
            comando = f'start "Terminal de Monika" "{ejecutable_python}" "{ruta_py}"'
            subprocess.Popen(comando, shell=True)
        else:
            # Soporte para sistemas basados en Linux (Lanza la terminal por defecto o xterm)
            os.system(f'xterm -e "{ejecutable_python} {ruta_py}" &')


    def comprobar_estado_cmd():
        # Ren'Py lee el archivo para saber si el jugador ya completó el puzzle
        ruta_flag = os.path.join(config.basedir, "cmd_flag.txt")
        if os.path.exists(ruta_flag):
            with open(ruta_flag, "r", encoding="utf-8") as f:
                if "SUCCESS" in f.read():
                    return "GANO"
        return "ESPERANDO"

    def enviar_timeout_cmd():
        # Ren'Py avisa a la consola negra que el tiempo se acabó
        ruta_flag = os.path.join(config.basedir, "cmd_flag.txt")
        with open(ruta_flag, "w", encoding="utf-8") as f:
            f.write("TIMEOUT")
            
    def limpiar_archivos_cmd():
        # Limpieza tras terminar la escena
        for archivo in ["cmd_flag.txt", "monika_terminal.py", "game/salvation.bat"]:
            ruta = os.path.join(config.basedir, archivo)
            if os.path.exists(ruta):
                try: os.remove(ruta)
                except: pass