import tkinter as tk
import math
import random
import time
import os
from PIL import Image, ImageTk, ImageDraw

class MinijuegoEscritorio:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.screen_w}x{self.screen_h}+0+0")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        
        # --- FIX TRANSPARENCIA ---
        COLOR_TRANSPARENTE = '#000001'
        try:
            self.root.attributes('-transparentcolor', COLOR_TRANSPARENTE)
        except tk.TclError:
            pass
            
        self.canvas = tk.Canvas(self.root, width=self.screen_w, height=self.screen_h, bg=COLOR_TRANSPARENTE, highlightthickness=0)
        self.canvas.pack()
        
        self.sprite_size = 64
        
        # --- CARGA DE SPRITES ANIMADOS Y FANTASMAS ---
        tipos_meteoritos = ['hello', 'glitch', 'n', 'y', 's']
        self.sprites = {tipo: [] for tipo in tipos_meteoritos}
        self.telegrafos = {tipo: [] for tipo in tipos_meteoritos}
        
        # Colores por si falla la carga de algún png (Rojo, Cian, Verde, Amarillo, Morado)
        colores_respaldo = [
            (255, 100, 100, 255), 
            (100, 255, 255, 255), 
            (100, 255, 100, 255), 
            (255, 255, 100, 255), 
            (200, 100, 255, 255)
        ]
        
        for tipo_idx, tipo in enumerate(tipos_meteoritos):
            # Carga frames del 1 al 5
            for i in range(1, 6): 
                ruta = os.path.join("game", "mod_assets", "images", f"{tipo}_{i}.png")
                try:
                    img_orig = Image.open(ruta).convert('RGBA')
                    img_res = img_orig.resize((self.sprite_size, self.sprite_size), Image.Resampling.LANCZOS)
                    self.sprites[tipo].append(ImageTk.PhotoImage(img_res))
                    
                    # Generar telégrafo (fantasma)
                    img_tel = img_res.copy()
                    r, g, b, a = img_tel.split()
                    a = a.point(lambda p: int(p * 0.4))
                    img_tel.putalpha(a)
                    draw = ImageDraw.Draw(img_tel)
                    draw.ellipse([2, 2, self.sprite_size-2, self.sprite_size-2], outline=(255, 50, 50, 180), width=3)
                    self.telegrafos[tipo].append(ImageTk.PhotoImage(img_tel))
                    
                except Exception:
                    # Fallback por si falta algún frame
                    img_falsa = Image.new('RGBA', (self.sprite_size, self.sprite_size), (0,0,0,0))
                    draw = ImageDraw.Draw(img_falsa)
                    draw.ellipse([4, 4, self.sprite_size-4, self.sprite_size-4], fill=colores_respaldo[tipo_idx], outline=(255,255,255,255), width=3)
                    self.sprites[tipo].append(ImageTk.PhotoImage(img_falsa))
                    
                    img_tel = img_falsa.copy()
                    r, g, b, a = img_tel.split()
                    a = a.point(lambda p: int(p * 0.4))
                    img_tel.putalpha(a)
                    draw_tel = ImageDraw.Draw(img_tel)
                    draw_tel.ellipse([2, 2, self.sprite_size-2, self.sprite_size-2], outline=(255, 50, 50, 180), width=3)
                    self.telegrafos[tipo].append(ImageTk.PhotoImage(img_tel))

        # --- CARGA DE BOCA ---
        self.bocas = []
        self.alertas = []
        ruta_boca = os.path.join("game", "mod_assets", "images", "mouth.png")
        try:
            img_boca_orig = Image.open(ruta_boca).resize((256, 128), Image.Resampling.NEAREST)
            self.boca_imgs = {
                'down': ImageTk.PhotoImage(img_boca_orig), 'up': ImageTk.PhotoImage(img_boca_orig.rotate(180, expand=True)),
                'left': ImageTk.PhotoImage(img_boca_orig.rotate(-90, expand=True)), 'right': ImageTk.PhotoImage(img_boca_orig.rotate(90, expand=True))
            }
        except Exception:
            img_vacia_h = tk.PhotoImage(width=256, height=128)
            img_vacia_v = tk.PhotoImage(width=128, height=256)
            self.boca_imgs = {'up': img_vacia_h, 'down': img_vacia_h, 'left': img_vacia_v, 'right': img_vacia_v}

        # --- SISTEMAS DE DIFICULTAD Y MEMORIA ---
        self.dificultad = 1
        self.intervalo_spawn = 4.5  
        self.tiempo_inicio = time.time()
        self.siguiente_spawn = self.tiempo_inicio + 2.0
        self.tiempo_cambio_dificultad = self.tiempo_inicio + 25.0
        self.siguiente_boca_spawn = self.tiempo_inicio + 15.0
        
        self.ultimos_patrones = ['', '', '']
        self.ultimos_patrones_bocas = ['normal', 'normal', 'normal']
        
        # --- VSYNC 60 FPS ---
        self.target_fps = 60
        self.frame_time = 1.0 / self.target_fps
        self.ultimo_frame = time.time()

        # --- POOL OPTIMIZADO ---
        self.max_meteoritos = 500
        self.pool_inactivos = []
        self.entidades_activas = []
        tipos_nombres = list(self.sprites.keys())
        
        for _ in range(self.max_meteoritos):
            tipo = random.choice(tipos_nombres)
            frame_inicial = random.randint(0, 4)
            obj_id = self.canvas.create_image(-500, -500, image=self.sprites[tipo][frame_inicial], anchor='center', state='hidden')
            self.pool_inactivos.append({
                'id': obj_id, 'x': -500.0, 'y': -500.0,
                'vx': 0.0, 'vy': 0.0, 'vx_real': 0.0, 'vy_real': 0.0,
                'tipo_mov': '', 'amp': 0, 'frec': 0, 'fase': 0,
                'base_x': 0.0, 'base_y': 0.0, 't_spawn': 0.0,
                'tipo': tipo,
                'frame': frame_inicial,
                't_frame': 0.0,
                'telegrafiando': False, 't_activacion': 0.0
            })
            
        print(f"[ZABA-Engine] INICIANDO EN NIVEL {self.dificultad} | Barras de Carga Activadas")
        self.root.after(1, self.game_loop)
        
    def crear_enemigo(self, x, y, vx, vy, tipo_mov='lineal', amplitud=0, frecuencia=0, fase=0):
        if not self.pool_inactivos: return
        
        e = self.pool_inactivos.pop()
        e['x'], e['y'] = float(x), float(y)
        e['vx_real'], e['vy_real'] = float(vx), float(vy)
        e['tipo_mov'] = tipo_mov
        e['amp'], e['frec'], e['fase'] = amplitud, frecuencia, fase
        e['base_x'], e['base_y'] = float(x), float(y)
        
        margen_seguro = 150
        es_adentro = (margen_seguro < x < self.screen_w - margen_seguro) and (margen_seguro < y < self.screen_h - margen_seguro)
        e['telegrafiando'] = es_adentro
        
        if es_adentro:
            tiempo_aviso = max(1.0, 1.8 - (self.dificultad * 0.1))
            e['t_activacion'] = time.time() + tiempo_aviso
            e['vx'] = e['vx_real'] * 0.08
            e['vy'] = e['vy_real'] * 0.08
            self.canvas.itemconfig(e['id'], image=self.telegrafos[e['tipo']][e['frame']], state='normal')
        else:
            e['t_spawn'] = time.time()
            e['vx'], e['vy'] = e['vx_real'], e['vy_real']
            self.canvas.itemconfig(e['id'], image=self.sprites[e['tipo']][e['frame']], state='normal')
        
        self.canvas.coords(e['id'], x, y)
        self.entidades_activas.append(e)

    def crear_alerta_boca(self, lado, delay=2.5):
        if lado == 'abajo':
            x, y = random.randint(0, self.screen_w - 256), self.screen_h
            datos = {'x': x, 'y': y, 'vx': 0, 'vy': -35, 'ax': 0, 'ay': 1.0, 'estado': 'in', 'origen': lado, 'img_in': self.boca_imgs['up'], 'img_out': self.boca_imgs['down'], 'w': 256, 'h': 128}
            ax1, ay1, ax2, ay2 = x, self.screen_h - 20, x + 256, self.screen_h
        elif lado == 'arriba':
            x, y = random.randint(0, self.screen_w - 256), -128
            datos = {'x': x, 'y': y, 'vx': 0, 'vy': 35, 'ax': 0, 'ay': -1.0, 'estado': 'in', 'origen': lado, 'img_in': self.boca_imgs['down'], 'img_out': self.boca_imgs['up'], 'w': 256, 'h': 128}
            ax1, ay1, ax2, ay2 = x, 0, x + 256, 20
        elif lado == 'der':
            x, y = self.screen_w, random.randint(0, self.screen_h - 256)
            datos = {'x': x, 'y': y, 'vx': -35, 'vy': 0, 'ax': 1.0, 'ay': 0, 'estado': 'in', 'origen': lado, 'img_in': self.boca_imgs['left'], 'img_out': self.boca_imgs['right'], 'w': 128, 'h': 256}
            ax1, ay1, ax2, ay2 = self.screen_w - 20, y, self.screen_w, y + 256
        elif lado == 'izq':
            x, y = -128, random.randint(0, self.screen_h - 256)
            datos = {'x': x, 'y': y, 'vx': 35, 'vy': 0, 'ax': -1.0, 'ay': 0, 'estado': 'in', 'origen': lado, 'img_in': self.boca_imgs['right'], 'img_out': self.boca_imgs['left'], 'w': 128, 'h': 256}
            ax1, ay1, ax2, ay2 = 0, y, 20, y + 256
        
        bg_id = self.canvas.create_rectangle(ax1, ay1, ax2, ay2, fill='#440000', outline='red', width=2)
        fill_id = self.canvas.create_rectangle(ax1, ay1, ax2, ay2, fill='red', outline='')
        
        tiempo_creacion = time.time()
        self.alertas.append({
            'bg_id': bg_id, 'fill_id': fill_id,
            'tiempo_creacion': tiempo_creacion,
            'tiempo_spawn': tiempo_creacion + delay,
            'datos': datos,
            'ax1': ax1, 'ay1': ay1, 'ax2': ax2, 'ay2': ay2,
            'origen': lado
        })

    def generar_bocas(self):
        patrones_disp = ['normal']
        if self.dificultad >= 5:
            patrones_disp.extend(['doble_lado', 'secuencia_ejes', 'ventilador'])
            
        disponibles = [p for p in patrones_disp if p not in self.ultimos_patrones_bocas]
        if not disponibles: disponibles = ['normal']
        
        patron = random.choice(disponibles)
        self.ultimos_patrones_bocas.pop(0)
        self.ultimos_patrones_bocas.append(patron)
        
        if patron == 'normal':
            cant = random.randint(1, 2 if self.dificultad >= 8 else 1)
            for _ in range(cant):
                self.crear_alerta_boca(random.choice(['arriba', 'abajo', 'izq', 'der']), delay=2.5)
                
        elif patron == 'doble_lado':
            cant = random.randint(2, 3)
            for _ in range(cant):
                self.crear_alerta_boca('izq', delay=2.5)
                self.crear_alerta_boca('der', delay=2.5)
                
        elif patron == 'secuencia_ejes':
            secuencia = random.choice([('izq', 'der', 'arriba', 'abajo'), ('arriba', 'abajo', 'izq', 'der')])
            self.crear_alerta_boca(secuencia[0], delay=2.5)
            self.crear_alerta_boca(secuencia[1], delay=2.5)
            self.crear_alerta_boca(secuencia[2], delay=4.5)
            self.crear_alerta_boca(secuencia[3], delay=4.5)
            self.crear_alerta_boca(secuencia[0], delay=6.5)
            self.crear_alerta_boca(secuencia[1], delay=6.5)
            
        elif patron == 'ventilador':
            vueltas = random.randint(2, 3)
            sentido = random.choice([['arriba', 'der', 'abajo', 'izq'], ['arriba', 'izq', 'abajo', 'der']])
            delay_acum = 2.0
            for _ in range(vueltas):
                for lado in sentido:
                    self.crear_alerta_boca(lado, delay=delay_acum)
                    delay_acum += 0.8 

    def generar_oleada(self):
        todos_los_patrones = ['circulo', 'muro_h', 'muro_v', 'esquinas', 'cruz_expansiva', 'anillo_doble','serpiente']
        patrones_disponibles = [p for p in todos_los_patrones if p not in self.ultimos_patrones]
        patron = random.choice(patrones_disponibles)
        
        self.ultimos_patrones.pop(0)
        self.ultimos_patrones.append(patron)
        
        margen = 100
        dif = self.dificultad
        multiplicador_vel = random.uniform(0.7, 1.5)
        vel_base = random.uniform(3.0 + (dif * 0.2), 4.5 + (dif * 0.3)) * multiplicador_vel
        centro_x, centro_y = self.screen_w / 2, self.screen_h / 2
        
        if patron == 'circulo':
            num_ondas = random.randint(1, 3 if dif >= 4 else 1)
            for _ in range(num_ondas):
                rx = random.randint(150, self.screen_w - 150)
                ry = random.randint(150, self.screen_h - 150)
                cantidad = int(8 + (dif * 1.2)) if num_ondas == 1 else int(5 + (dif * 0.8))
                vel_explosion = vel_base * random.uniform(0.6, 1.6)
                for i in range(cantidad):
                    angulo = (math.pi * 2 / cantidad) * i
                    self.crear_enemigo(rx, ry, math.cos(angulo) * vel_explosion, math.sin(angulo) * vel_explosion)
                
        elif patron == 'muro_h':
            cantidad = int(8 + (dif * 1.2))
            espaciado = self.screen_w / cantidad
            hueco_seguro = random.randint(2, cantidad - 4)
            dir_y = random.choice([1, -1])
            y_start = -margen if dir_y == 1 else self.screen_h + margen
            for i in range(cantidad):
                if i in [hueco_seguro, hueco_seguro + 1, hueco_seguro + 2]: continue
                self.crear_enemigo(i * espaciado, y_start, 0, vel_base * dir_y)
                
        elif patron == 'muro_v':
            cantidad = int(6 + (dif * 1.2))
            espaciado = self.screen_h / cantidad
            hueco_seguro = random.randint(2, cantidad - 4)
            dir_x = random.choice([1, -1])
            x_start = -margen if dir_x == 1 else self.screen_w + margen
            for i in range(cantidad):
                if i in [hueco_seguro, hueco_seguro + 1, hueco_seguro + 2]: continue
                self.crear_enemigo(x_start, i * espaciado, vel_base * dir_x, 0)
                
        elif patron == 'esquinas':
            cantidad = int(2 + (dif * 1.0))
            esquinas = [(0,0), (self.screen_w, 0), (0, self.screen_h), (self.screen_w, self.screen_h)]
            for ex, ey in esquinas:
                dx, dy = centro_x - ex, centro_y - ey
                dist = math.hypot(dx, dy)
                vx, vy = (dx/dist) * vel_base, (dy/dist) * vel_base
                for i in range(cantidad):
                    self.crear_enemigo(ex - vx*i*50, ey - vy*i*50, vx, vy)
                    
        elif patron == 'cruz_expansiva':
            brazos = 8 if dif >= 6 else 4
            orbes_por_brazo = int(4 + (dif * 0.5))
            rx = random.randint(int(centro_x - 300), int(centro_x + 300))
            ry = random.randint(int(centro_y - 200), int(centro_y + 200))
            for i in range(1, orbes_por_brazo + 1):
                vel_estela = vel_base * (0.8 + (i * 0.2))
                for b in range(brazos):
                    angulo = (math.pi * 2 / brazos) * b
                    angulo_final = angulo + (i * 0.1) if brazos == 4 else angulo
                    self.crear_enemigo(rx, ry, math.cos(angulo_final) * vel_estela, math.sin(angulo_final) * vel_estela)
                
        elif patron == 'anillo_doble':
            rx = random.randint(200, self.screen_w - 200)
            ry = random.randint(200, self.screen_h - 200)
            cantidad = int(8 + (dif * 1.2))
            for i in range(cantidad):
                angulo = (math.pi * 2 / cantidad) * i
                self.crear_enemigo(rx, ry, math.cos(angulo) * vel_base, math.sin(angulo) * vel_base)
                if dif >= 5:
                    self.crear_enemigo(rx, ry, math.cos(angulo) * (vel_base*0.6), math.sin(angulo) * (vel_base*0.6))
                
        elif patron == 'serpiente':
            orientacion = random.choice(['horizontal', 'vertical'])
            num_filas = 1 if dif < 5 else (2 if dif < 9 else 3)
            largo_serpiente = int(20 + (dif * 1.5))
            vel_px_sec = vel_base * 41.0
            distancia = 45.0
            
            frecuencia_unificada = random.uniform(1.5, 2.5)
            amplitud_unificada = random.uniform(80, 130)
            
            if orientacion == 'horizontal':
                espaciado = self.screen_h / (num_filas + 1)
                dir_x = random.choice([1, -1])
                x_start = -margen if dir_x == 1 else self.screen_w + margen
                for f in range(1, num_filas + 1):
                    y_base = f * espaciado
                    for i in range(largo_serpiente):
                        retraso_fase = - (frecuencia_unificada * (distancia / vel_px_sec) * i)
                        self.crear_enemigo(x_start - (i * distancia * dir_x), y_base, vel_base * dir_x, 0,
                                           'serpiente', amplitud_unificada, frecuencia_unificada, retraso_fase)
            else:
                espaciado = self.screen_w / (num_filas + 1)
                dir_y = random.choice([1, -1])
                y_start = -margen if dir_y == 1 else self.screen_h + margen
                for f in range(1, num_filas + 1):
                    x_base = f * espaciado
                    for i in range(largo_serpiente):
                        retraso_fase = - (frecuencia_unificada * (distancia / vel_px_sec) * i)
                        self.crear_enemigo(x_base, y_start - (i * distancia * dir_y), 0, vel_base * dir_y,
                                           'serpiente', amplitud_unificada, frecuencia_unificada, retraso_fase)

    def game_loop(self):
        tiempo_actual = time.time()
        dt = tiempo_actual - self.ultimo_frame
        
        if dt < self.frame_time:
            espera = int((self.frame_time - dt) * 1000)
            self.root.after(max(1, espera), self.game_loop)
            return
            
        if dt > 0.1: dt = 0.1
        self.ultimo_frame = tiempo_actual
        factor_velocidad = dt * 60.0
        
        # --- GESTOR DE DIFICULTAD ---
        if tiempo_actual >= self.tiempo_cambio_dificultad and self.dificultad < 10:
            self.dificultad += 1
            self.tiempo_cambio_dificultad = tiempo_actual + 25.0
            self.intervalo_spawn = max(2.2, 5.0 - (self.dificultad * 0.30))
        
        if tiempo_actual >= self.siguiente_spawn:
            self.generar_oleada()
            self.siguiente_spawn = tiempo_actual + self.intervalo_spawn
            
        if tiempo_actual >= self.siguiente_boca_spawn:
            self.generar_bocas()
            self.siguiente_boca_spawn = tiempo_actual + random.uniform(15.0 - (self.dificultad*0.4), 22.0 - (self.dificultad*0.6))
            
        mouse_x = self.root.winfo_pointerx()
        mouse_y = self.root.winfo_pointery()
        target_x = max(0, min(mouse_x, self.screen_w))
        target_y = max(0, min(mouse_y, self.screen_h))
        
        coords_func = self.canvas.coords
        itemconfig_func = self.canvas.itemconfig
        delete_func = self.canvas.delete
        sin_func = math.sin
        w, h = self.screen_w, self.screen_h
        margen_borrado = 1000

        # --- LÓGICA DE BARRAS DE CARGA DE BOCA ---
        alertas_vivas = []
        for a in self.alertas:
            t_restante = a['tiempo_spawn'] - tiempo_actual
            t_total = a['tiempo_spawn'] - a['tiempo_creacion']
            
            if t_restante <= 0:
                delete_func(a['bg_id'])
                delete_func(a['fill_id'])
                d = a['datos']
                d['id'] = self.canvas.create_image(d['x'], d['y'], image=d['img_in'], anchor='nw')
                self.bocas.append(d)
            else:
                progreso = 1.0 - (t_restante / max(t_total, 0.001))
                ax1, ay1, ax2, ay2 = a['ax1'], a['ay1'], a['ax2'], a['ay2']
                
                if a['origen'] == 'abajo':
                    ay1 = ay2 - ((ay2 - ay1) * progreso)
                elif a['origen'] == 'arriba':
                    ay2 = ay1 + ((ay2 - ay1) * progreso)
                elif a['origen'] == 'der':
                    ax1 = ax2 - ((ax2 - ax1) * progreso)
                elif a['origen'] == 'izq':
                    ax2 = ax1 + ((ax2 - ax1) * progreso)
                    
                coords_func(a['fill_id'], ax1, ay1, ax2, ay2)
                
                if t_restante < 0.5 and int(tiempo_actual * 20) % 2 == 0:
                    itemconfig_func(a['fill_id'], fill='yellow')
                else:
                    itemconfig_func(a['fill_id'], fill='red')
                    
                alertas_vivas.append(a)
        self.alertas = alertas_vivas

        # --- ACTUALIZACIÓN DE BOCAS (Muerden) ---
        bocas_vivas = []
        for b in self.bocas:
            b['vx'] += b['ax'] * factor_velocidad
            b['vy'] += b['ay'] * factor_velocidad
            if b['estado'] == 'in':
                if (b['origen'] == 'abajo' and b['vy'] >= 0) or (b['origen'] == 'arriba' and b['vy'] <= 0) or \
                   (b['origen'] == 'der' and b['vx'] >= 0) or (b['origen'] == 'izq' and b['vx'] <= 0):
                    b['estado'] = 'out'
                    itemconfig_func(b['id'], image=b['img_out'])
            
            b['x'] += b['vx'] * factor_velocidad
            b['y'] += b['vy'] * factor_velocidad
            coords_func(b['id'], b['x'], b['y'])
            
            if b['x'] < target_x < b['x'] + b['w'] and b['y'] < target_y < b['y'] + b['h']:
                delete_func(b['id'])
                continue
            if b['estado'] == 'out' and (b['x'] > w + 200 or b['x'] < -600 or b['y'] > h + 200 or b['y'] < -600):
                delete_func(b['id'])
                continue
            bocas_vivas.append(b)
        self.bocas = bocas_vivas

        # --- ACTUALIZACIÓN DE METEORITOS Y ANIMACIÓN ---
        entidades_vivas = []
        for e in self.entidades_activas:
            debe_morir = False
            
            # Animación de frames (cambia cada ~0.08 seg)
            e['t_frame'] += dt
            if e['t_frame'] >= 0.08:
                e['t_frame'] = 0
                e['frame'] = (e['frame'] + 1) % 5
                
                # Actualiza el frame en el canvas
                img_list = self.telegrafos if e['telegrafiando'] else self.sprites
                itemconfig_func(e['id'], image=img_list[e['tipo']][e['frame']])
            
            # Lógica de movimiento
            if e['telegrafiando']:
                if tiempo_actual >= e['t_activacion']:
                    e['telegrafiando'] = False
                    e['t_spawn'] = tiempo_actual
                    e['vx'], e['vy'] = e['vx_real'], e['vy_real']
                    e['base_x'], e['base_y'] = e['x'], e['y']
                    # Fuerza la actualización al frame normal inmediatamente
                    itemconfig_func(e['id'], image=self.sprites[e['tipo']][e['frame']])
                
                e['x'] += e['vx'] * factor_velocidad
                e['y'] += e['vy'] * factor_velocidad
                coords_func(e['id'], e['x'], e['y'])
                entidades_vivas.append(e)
                continue
            
            if e['tipo_mov'] == 'serpiente':
                t = tiempo_actual - e['t_spawn']
                e['base_x'] += e['vx'] * factor_velocidad
                e['base_y'] += e['vy'] * factor_velocidad
                
                if e['vy'] != 0:
                    e['x'] = e['base_x'] + sin_func(t * e['frec'] + e['fase']) * e['amp']
                    e['y'] = e['base_y']
                else:
                    e['x'] = e['base_x']
                    e['y'] = e['base_y'] + sin_func(t * e['frec'] + e['fase']) * e['amp']
            else:
                e['x'] += e['vx'] * factor_velocidad
                e['y'] += e['vy'] * factor_velocidad
            
            coords_func(e['id'], e['x'], e['y'])
            
            if e['x'] - 18 < target_x < e['x'] + 18 and e['y'] - 18 < target_y < e['y'] + 18:
                debe_morir = True
            elif (e['x'] < -margen_borrado or e['x'] > w + margen_borrado or e['y'] < -margen_borrado or e['y'] > h + margen_borrado):
                debe_morir = True
                
            if debe_morir:
                itemconfig_func(e['id'], state='hidden')
                self.pool_inactivos.append(e)
            else:
                entidades_vivas.append(e)
                
        self.entidades_activas = entidades_vivas
        self.root.after(1, self.game_loop)

if __name__ == "__main__":
    juego = MinijuegoEscritorio()
    juego.root.mainloop()