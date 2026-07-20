import os
import ctypes
import sys

def restore_system():
    # 1. Definir rutas
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    backup_file = os.path.join(base_dir, "wallpaper_backup.txt")

    print("Iniciando proceso de limpieza...")

    # 2. Limpieza de iconos (hello_1.png a hello_666.png)
    files_removed = 0
    for i in range(1, 667):
        target = os.path.join(desktop, f"hello_{i}.png")
        if os.path.exists(target):
            try:
                os.remove(target)
                files_removed += 1
            except:
                pass
    print(f"Iconos eliminados: {files_removed}")

    # 3. Restaurar Wallpaper
    if os.path.exists(backup_file):
        with open(backup_file, "r") as f:
            original_path = f.read().strip()
        
        try:
            # 20 es el código de SPI_SETDESKWALLPAPER
            ctypes.windll.user32.SystemParametersInfoW(20, 0, original_path, 3)
            print("Wallpaper restaurado exitosamente.")
            # Opcional: borrar el archivo de backup tras restaurar
            # os.remove(backup_file) 
        except Exception as e:
            print(f"Error restaurando wallpaper: {e}")
    else:
        print("No se encontró archivo de respaldo del wallpaper.")

    input("Presiona Enter para cerrar...")

if __name__ == "__main__":
    restore_system()