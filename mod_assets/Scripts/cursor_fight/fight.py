import tkinter as tk
import math
import random
import time
import os
from PIL import Image, ImageTk

class MinijuegoEscritorio:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.screen_w}x{self.screen_h}+0+0")
        self.root.overrideredirect(True) 
        self.root.attributes('-topmost', True) 
        
        try:
            self.root.attributes('-transparentcolor', 'black')
        except tk.TclError:
            pass 
            
        self.canvas = tk.Canvas(self.root, width=self.screen_w, height=self.screen_h, bg='black', highlightthickness=0)
        self.canvas.pack()
        
        self.sprite_size = 64
        
        # --- CARGA DE SPRITES PEQUEÑOS ---
        self.sprites = {}
        rutas_imagenes = {
            'basico': "hello.png",
            'fuego': "fire.png",
            'hielo': "ice.png",
            'veneno': "poison.png"
        }
        colores_respaldo = ['red', 'orange', 'cyan', 'purple']
        for i, (nombre, archivo) in enumerate(rutas_imagenes.items()):
            ruta = os.path.join("game", "mod_assets", "images", archivo)
            try:
                img_orig = Image.open(ruta)
                img_res = img_orig.resize((self.sprite_size, self.sprite_size), Image.Resampling.NEAREST)
                self.sprites[nombre] = ImageTk.PhotoImage(img_res)
            except Exception:
                img_vacia = tk.PhotoImage(width=self.sprite_size, height=self.sprite_size)
                self.sprites[nombre] = img_vacia 
                self.sprites[f"{nombre}_color"] = colores_respaldo[i % len(colores_respaldo)]

        # --- CARGA DEL SPRITE DE LA BOCA ---
        self.bocas = []
        self.siguiente_boca_spawn = time.time() + random.uniform(5.0, 8.0)
        
        ruta_boca = os.path.join("game", "mod_assets", "images", "mouth.png")
        try:
            # Precargamos todas las rotaciones para no gastar recursos en tiempo real
            img_boca_orig = Image.open(ruta_boca).resize((256, 128), Image.Resampling.NEAREST)
            self.boca_imgs = {
                'down': ImageTk.PhotoImage(img_boca_orig), # Mirando hacia arriba
                'up': ImageTk.PhotoImage(img_boca_orig.rotate(180, expand=True)), # Mirando hacia abajo
                'left': ImageTk.PhotoImage(img_boca_orig.rotate(-90, expand=True)), # Mirando a la izquierda (256x512)
                'right': ImageTk.PhotoImage(img_boca_orig.rotate(90, expand=True)) # Mirando a la derecha (256x512)
            }
        except Exception as e:
            print(f"Error cargando sprite boca: {e}")
            img_vacia_h = tk.PhotoImage(width=256, height=128)
            img_vacia_v = tk.PhotoImage(width=128, height=256)
            self.boca_imgs = {'up': img_vacia_h, 'down': img_vacia_h, 'left': img_vacia_v, 'right': img_vacia_v}

        self.enemigos = []
        
        # Variables de tiempo general
        self.tiempo_inicio = time.time()
        self.intervalo_spawn = 5.0  
        self.siguiente_spawn = self.tiempo_inicio + 2.0 
        self.ultimo_reduccion = self.tiempo_inicio
        
        self.root.after(16, self.game_loop)
        
    def crear_enemigo(self, x, y, vx, vy):
        tipos_disponibles = [k for k in self.sprites.keys() if not k.endswith('_color')]
        tipo_elegido = random.choice(tipos_disponibles)
        sprite_img = self.sprites[tipo_elegido]
        
        if sprite_img.width() == self.sprite_size and not hasattr(sprite_img, 'paste'):
            color = self.sprites.get(f"{tipo_elegido}_color", 'white')
            obj_id = self.canvas.create_oval(x, y, x + self.sprite_size, y + self.sprite_size, fill=color, outline='')
        else:
            obj_id = self.canvas.create_image(x, y, image=sprite_img, anchor='nw')
        
        self.enemigos.append({'id': obj_id, 'x': float(x), 'y': float(y), 'vx': float(vx), 'vy': float(vy)})

    def generar_bocas(self):
        cantidad = random.randint(1, 3)
        lados = ['arriba', 'abajo', 'izq', 'der']
        
        for _ in range(cantidad):
            lado = random.choice(lados)
            # Configuración de salto (inercia vs gravedad)
            if lado == 'abajo':
                x = random.randint(0, self.screen_w - 256) # Ajustado al ancho real
                y = self.screen_h
                obj_id = self.canvas.create_image(x, y, image=self.boca_imgs['up'], anchor='nw')
                self.bocas.append({'id': obj_id, 'x': x, 'y': y, 'vx': 0, 'vy': -35, 'ax': 0, 'ay': 1.0, 'estado': 'in', 'origen': lado, 'img_out': self.boca_imgs['down'], 'w': 256, 'h': 128}) # Hitbox corregida
            
            elif lado == 'arriba':
                x = random.randint(0, self.screen_w - 256) # Ajustado al ancho real
                y = -128 # Ajustado a la altura real
                obj_id = self.canvas.create_image(x, y, image=self.boca_imgs['down'], anchor='nw')
                self.bocas.append({'id': obj_id, 'x': x, 'y': y, 'vx': 0, 'vy': 35, 'ax': 0, 'ay': -1.0, 'estado': 'in', 'origen': lado, 'img_out': self.boca_imgs['up'], 'w': 256, 'h': 128}) # Hitbox corregida
            
            elif lado == 'der':
                x = self.screen_w
                y = random.randint(0, self.screen_h - 256) # Ajustado a la altura real tras rotar
                obj_id = self.canvas.create_image(x, y, image=self.boca_imgs['left'], anchor='nw')
                self.bocas.append({'id': obj_id, 'x': x, 'y': y, 'vx': -35, 'vy': 0, 'ax': 1.0, 'ay': 0, 'estado': 'in', 'origen': lado, 'img_out': self.boca_imgs['right'], 'w': 128, 'h': 256}) # Ancho y alto invertidos (vertical)
            
            elif lado == 'izq':
                x = -128 # Ajustado al ancho real tras rotar
                y = random.randint(0, self.screen_h - 256) # Ajustado a la altura real tras rotar
                obj_id = self.canvas.create_image(x, y, image=self.boca_imgs['right'], anchor='nw')
                self.bocas.append({'id': obj_id, 'x': x, 'y': y, 'vx': 35, 'vy': 0, 'ax': -1.0, 'ay': 0, 'estado': 'in', 'origen': lado, 'img_out': self.boca_imgs['left'], 'w': 128, 'h': 256}) # Ancho y alto invertidos (vertical)

    def generar_oleada(self):
        patrones = ['circulo', 'muro_h', 'muro_v', 'esquinas', 'cruz', 'anillo_doble', 'lluvia_diagonal', 'enjambre_random']
        patron = random.choice(patrones)
        margen = 100 
        velocidad = random.uniform(4.0, 8.0)
        centro_x, centro_y = self.screen_w / 2, self.screen_h / 2
        
        if patron == 'circulo':
            radio = max(self.screen_w, self.screen_h) / 2 + margen
            for i in range(12):
                angulo = (2 * math.pi / 12) * i
                x, y = centro_x + math.cos(angulo) * radio, centro_y + math.sin(angulo) * radio
                dx, dy = centro_x - x, centro_y - y
                d = math.hypot(dx, dy)
                self.crear_enemigo(x, y, (dx/d)*velocidad, (dy/d)*velocidad)
        elif patron == 'cruz':
            for i in range(1, 7):
                offset = i * 150
                self.crear_enemigo(centro_x, -margen - offset, 0, velocidad)
                self.crear_enemigo(centro_x, self.screen_h + margen + offset, 0, -velocidad)
                self.crear_enemigo(-margen - offset, centro_y, velocidad, 0)
                self.crear_enemigo(self.screen_w + margen + offset, centro_y, -velocidad, 0)
        elif patron == 'anillo_doble':
            for r_mult, v_mult, dir_g in [(1, 1, 1), (1.5, 0.7, -1)]:
                radio = (self.screen_w / 2) * r_mult + margen
                for i in range(8):
                    angulo = (2 * math.pi / 8) * i
                    x, y = centro_x + math.cos(angulo) * radio, centro_y + math.sin(angulo) * radio
                    dx, dy = centro_x - x, centro_y - y
                    d = math.hypot(dx, dy)
                    self.crear_enemigo(x, y, (dx/d)*velocidad*v_mult, (dy/d)*velocidad*v_mult)
        elif patron == 'lluvia_diagonal':
            for _ in range(15):
                x = random.randint(-margen, self.screen_w)
                y = random.randint(-margen*3, -margen)
                self.crear_enemigo(x, y, velocidad * 0.8, velocidad * 1.2)
        elif patron == 'enjambre_random':
            lado_orig = random.choice(['arriba', 'abajo', 'izq', 'der'])
            for _ in range(random.randint(10, 20)):
                if lado_orig == 'arriba':
                    self.crear_enemigo(random.randint(0, self.screen_w), -margen, random.uniform(-2, 2), random.uniform(velocidad*0.5, velocidad))
                elif lado_orig == 'abajo':
                    self.crear_enemigo(random.randint(0, self.screen_w), self.screen_h + margen, random.uniform(-2, 2), random.uniform(-velocidad, -velocidad*0.5))
                elif lado_orig == 'izq':
                    self.crear_enemigo(-margen, random.randint(0, self.screen_h), random.uniform(velocidad*0.5, velocidad), random.uniform(-2, 2))
                else:
                    self.crear_enemigo(self.screen_w + margen, random.randint(0, self.screen_h), random.uniform(-velocidad, -velocidad*0.5), random.uniform(-2, 2))
        elif patron == 'muro_h':
            espaciado = self.screen_w / 9
            for i in range(1, 9): self.crear_enemigo(i * espaciado, -margen, 0, velocidad)
        elif patron == 'muro_v':
            espaciado = self.screen_h / 9
            for i in range(1, 9): self.crear_enemigo(-margen, i * espaciado, velocidad, 0)
        else:
            self.crear_enemigo(-margen, -margen, velocidad, velocidad)

    def game_loop(self):
        tiempo_actual = time.time()
        
        # Timer Oleadas
        if tiempo_actual - self.ultimo_reduccion >= 10.0:
            self.intervalo_spawn = max(1.0, self.intervalo_spawn - 0.1)
            self.ultimo_reduccion += 10.0
        
        if tiempo_actual >= self.siguiente_spawn:
            self.generar_oleada()
            self.siguiente_spawn = tiempo_actual + self.intervalo_spawn
            
        # Timer Bocas
        if tiempo_actual >= self.siguiente_boca_spawn:
            self.generar_bocas()
            self.siguiente_boca_spawn = tiempo_actual + random.uniform(5.0, 8.0)
            
        mouse_x = self.root.winfo_pointerx()
        mouse_y = self.root.winfo_pointery()
        target_x = max(0, min(mouse_x, self.screen_w))
        target_y = max(0, min(mouse_y, self.screen_h))
        
        move_func = self.canvas.move
        delete_func = self.canvas.delete
        w, h = self.screen_w, self.screen_h
        
        # --- ACTUALIZACIÓN DE BOCAS ---
        bocas_vivas = []
        for b in self.bocas:
            # Aplicar gravedad
            b['vx'] += b['ax']
            b['vy'] += b['ay']
            
            # Comprobar si llegó al punto máximo del salto para girar la imagen
            if b['estado'] == 'in':
                cambio = False
                if b['origen'] == 'abajo' and b['vy'] >= 0: cambio = True
                elif b['origen'] == 'arriba' and b['vy'] <= 0: cambio = True
                elif b['origen'] == 'der' and b['vx'] >= 0: cambio = True
                elif b['origen'] == 'izq' and b['vx'] <= 0: cambio = True
                
                if cambio:
                    b['estado'] = 'out'
                    self.canvas.itemconfig(b['id'], image=b['img_out'])
            
            ex = b['x'] + b['vx']
            ey = b['y'] + b['vy']
            b['x'], b['y'] = ex, ey
            
            move_func(b['id'], b['vx'], b['vy'])
            
            # Hitbox rectangular (detecta colisión en cualquier parte del sprite)
            if ex < target_x < ex + b['w'] and ey < target_y < ey + b['h']:
                delete_func(b['id'])
                continue
                
            # Limpieza cuando salen de la pantalla
            if b['estado'] == 'out':
                if ex > w + 200 or ex < -600 or ey > h + 200 or ey < -600:
                    delete_func(b['id'])
                    continue
                    
            bocas_vivas.append(b)
        self.bocas = bocas_vivas

        # --- ACTUALIZACIÓN DE METEORITOS (SPRITES PEQUEÑOS) ---
        enemigos_vivos = []
        radio_col = 20
        margen = 200
        mitad = self.sprite_size / 2
        
        for e in self.enemigos:
            ex = e['x'] + e['vx']
            ey = e['y'] + e['vy']
            e['x'], e['y'] = ex, ey
            
            move_func(e['id'], e['vx'], e['vy'])
            
            cx = ex + mitad
            cy = ey + mitad
            dx = target_x - cx
            dy = target_y - cy
            
            if abs(dx) < radio_col and abs(dy) < radio_col:
                if (dx*dx + dy*dy) < (radio_col*radio_col):
                    delete_func(e['id'])
                    continue 
            
            if (ex < -margen or ex > w + margen or ey < -margen or ey > h + margen):
                delete_func(e['id'])
            else:
                enemigos_vivos.append(e)
                
        self.enemigos = enemigos_vivos
        
        self.root.after(16, self.game_loop)

if __name__ == "__main__":
    juego = MinijuegoEscritorio()
    juego.root.mainloop()