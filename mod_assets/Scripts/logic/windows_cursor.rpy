init python:
    import ctypes
    from ctypes import wintypes
    import sys

    # Estructura para capturar las coordenadas del cursor en Windows
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    _window_following_active = False
    _cached_hwnd = None

    def window_follow_loop():
        global _cached_hwnd
        # Solo se ejecuta en Windows, si la función está activa y está en modo ventana
        if _window_following_active and sys.platform == "win32" and not _preferences.fullscreen:
            if not _cached_hwnd:
                _cached_hwnd = ctypes.windll.user32.FindWindowW(None, config.window_title)
            
            if _cached_hwnd:
                pt = POINT()
                ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
                
                rect = wintypes.RECT()
                ctypes.windll.user32.GetWindowRect(_cached_hwnd, ctypes.byref(rect))
                w = rect.right - rect.left
                h = rect.bottom - rect.top
                
                # Calcula la posición para que el centro de la ventana esté en el cursor
                new_x = pt.x - (w // 2)
                new_y = pt.y - (h // 2)
                
                # Mueve la ventana (El 5 equivale a los flags SWP_NOSIZE | SWP_NOZORDER)
                ctypes.windll.user32.SetWindowPos(_cached_hwnd, 0, new_x, new_y, 0, 0, 5)

    # Añadimos la función al bucle periódico de Ren'Py (se ejecuta unas 20 veces por segundo)
    config.periodic_callback = window_follow_loop

    def windows_follow_cursor():
        global _window_following_active, _cached_hwnd
        _cached_hwnd = ctypes.windll.user32.FindWindowW(None, config.window_title)
        _window_following_active = True

    def windows_unfollow_cursor():
        global _window_following_active
        _window_following_active = False