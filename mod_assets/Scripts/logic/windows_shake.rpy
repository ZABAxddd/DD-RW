init python:
    import os
    import random
    import ctypes
    
    # Sistema de log para debuggear si falla
    def debug_log(msg):
        renpy.log("[WINDOW_SHAKE] " + str(msg))

    def get_window_handle():
        try:
            # GetActiveWindow es más seguro en procesos de una sola ventana
            hwnd = ctypes.windll.user32.GetActiveWindow()
            if hwnd:
                return hwnd
        except Exception as e:
            debug_log("Error obteniendo handle: " + str(e))
        return None

    def move_window(x, y):
        hwnd = get_window_handle()
        if hwnd:
            # Obtener posición actual para mantener el tamaño
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
            width = rect.right - rect.left
            height = rect.bottom - rect.top
            
            # MoveWindow(hwnd, x, y, width, height, repaint)
            ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)
        else:
            debug_log("No se pudo obtener el handle para mover.")

    # Almacenamos la posición inicial al arrancar
    _orig_x, _orig_y = 0, 0

    def guardar_posicion():
        global _orig_x, _orig_y
        hwnd = get_window_handle()
        if hwnd:
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
            _orig_x, _orig_y = rect.left, rect.top
            debug_log(f"Posicion guardada: {_orig_x}, {_orig_y}")
        else:
            debug_log("Fallo al guardar posicion.")

    class CDD_WindowShake(renpy.Displayable):
        def __init__(self, magnitud, duracion):
            super(CDD_WindowShake, self).__init__()
            self.magnitud = float(magnitud)
            self.duracion = float(duracion)
            self.start_time = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
                guardar_posicion()

            tiempo_transcurrido = st - self.start_time
            if tiempo_transcurrido >= self.duracion:
                # Restaurar al final
                move_window(_orig_x, _orig_y)
                return renpy.Render(1, 1)

            # Cálculo de fuerza
            intensidad = self.magnitud
            if (self.duracion - tiempo_transcurrido) < 2.0:
                intensidad *= (self.duracion - tiempo_transcurrido) / 2.0
            
            fuerza = int(40 * intensidad)
            dx = random.randint(-fuerza, fuerza)
            dy = random.randint(-fuerza, fuerza)
            
            move_window(_orig_x + dx, _orig_y + dy)
            
            renpy.redraw(self, 0)
            return renpy.Render(1, 1)

    def windows_shake(magnitud=0.5, duracion=5.0):
        if os.name == 'nt' and not _preferences.fullscreen:
        
            renpy.show_screen("shake_screen", magnitud=magnitud, duracion=duracion)

screen shake_screen(magnitud, duracion):
    add CDD_WindowShake(magnitud, duracion)
    timer duracion action Hide("shake_screen")