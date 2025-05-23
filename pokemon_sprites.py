# pokemon_sprites.py
"""
Kreative grafische Pokemon-Darstellungen mit tkinter Canvas
"""
import tkinter as tk
import math
from game_data import POKEMON_DATA, COLORS

class PokemonSprite:
    """Klasse für das Zeichnen von Pokemon-Sprites"""
    
    @staticmethod
    def draw_pokemon(canvas, pokemon_name, x, y, size=80):
        """Zeichnet ein Pokemon basierend auf seinem Typ"""
        if pokemon_name not in POKEMON_DATA:
            return
            
        data = POKEMON_DATA[pokemon_name]
        sprite_type = data.get("sprite_type", "default")
        color = data["color"]
        
        # Lösche vorherige Sprites
        canvas.delete("pokemon_sprite")
        
        # Rufe die entsprechende Zeichenfunktion auf
        if sprite_type == "lizard_fire":
            PokemonSprite._draw_glumanda(canvas, x, y, size, color)
        elif sprite_type == "turtle_water":
            PokemonSprite._draw_schiggy(canvas, x, y, size, color)
        elif sprite_type == "plant_bulb":
            PokemonSprite._draw_bisasam(canvas, x, y, size, color)
        elif sprite_type == "electric_mouse":
            PokemonSprite._draw_pikachu(canvas, x, y, size, color)
        elif sprite_type == "rat_normal":
            PokemonSprite._draw_rattfratz(canvas, x, y, size, color)
        elif sprite_type == "bird_flying":
            PokemonSprite._draw_taubsi(canvas, x, y, size, color)
        elif sprite_type == "caterpillar_bug":
            PokemonSprite._draw_raupy(canvas, x, y, size, color)
        elif sprite_type == "beetle_poison":
            PokemonSprite._draw_hornliu(canvas, x, y, size, color)
        elif sprite_type == "bat_poison":
            PokemonSprite._draw_zubat(canvas, x, y, size, color)
        elif sprite_type == "mole_ground":
            PokemonSprite._draw_digda(canvas, x, y, size, color)
        elif sprite_type == "psychic_humanoid":
            PokemonSprite._draw_abra(canvas, x, y, size, color)
        elif sprite_type == "fighter_muscle":
            PokemonSprite._draw_machollo(canvas, x, y, size, color)
        else:
            PokemonSprite._draw_default(canvas, x, y, size, color)
    
    @staticmethod
    def _draw_glumanda(canvas, x, y, size, color):
        """Zeichnet Glumanda - Feuer-Echse mit Flamme"""
        # Körper (orange-roter Kreis)
        body_size = size * 0.7
        canvas.create_oval(
            x - body_size//2, y - body_size//2,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#CC3333", width=3, tags="pokemon_sprite"
        )
        
        # Bauch (hellerer Kreis)
        belly_size = size * 0.4
        canvas.create_oval(
            x - belly_size//2, y - belly_size//4,
            x + belly_size//2, y + belly_size//2 + belly_size//4,
            fill="#FFAA88", outline="", tags="pokemon_sprite"
        )
        
        # Schwanz mit Flamme (gewellte Linie)
        tail_x = x + size//2
        tail_y = y
        for i in range(3):
            flame_x = tail_x + i * 8
            flame_y = tail_y - i * 6
            canvas.create_oval(
                flame_x - 4, flame_y - 8,
                flame_x + 4, flame_y + 8,
                fill="#FF6600" if i % 2 == 0 else "#FFAA00",
                outline="", tags="pokemon_sprite"
            )
        
        # Augen (schwarze Punkte)
        eye_size = 4
        canvas.create_oval(
            x - 12, y - 15, x - 12 + eye_size, y - 15 + eye_size,
            fill="black", tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + 8, y - 15, x + 8 + eye_size, y - 15 + eye_size,
            fill="black", tags="pokemon_sprite"
        )
        
        # Kleine Arme
        canvas.create_oval(
            x - size//2 - 8, y - 5, x - size//2 + 8, y + 10,
            fill=color, outline="#CC3333", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + size//2 - 8, y - 5, x + size//2 + 8, y + 10,
            fill=color, outline="#CC3333", width=2, tags="pokemon_sprite"
        )
    
    @staticmethod
    def _draw_schiggy(canvas, x, y, size, color):
        """Zeichnet Schiggy - Wasser-Schildkröte"""
        # Panzer (großer blauer Kreis)
        shell_size = size * 0.8
        canvas.create_oval(
            x - shell_size//2, y - shell_size//2,
            x + shell_size//2, y + shell_size//2,
            fill=color, outline="#2266CC", width=4, tags="pokemon_sprite"
        )
        
        # Panzer-Muster (sechseck-ähnlich)
        for i in range(6):
            angle = i * math.pi / 3
            px = x + math.cos(angle) * shell_size//4
            py = y + math.sin(angle) * shell_size//4
            canvas.create_oval(
                px - 6, py - 6, px + 6, py + 6,
                fill="#1144AA", outline="", tags="pokemon_sprite"
            )
        
        # Kopf (kleinerer Kreis oben)
        head_size = size * 0.4
        head_y = y - shell_size//3
        canvas.create_oval(
            x - head_size//2, head_y - head_size//2,
            x + head_size//2, head_y + head_size//2,
            fill="#6699FF", outline="#2266CC", width=2, tags="pokemon_sprite"
        )
        
        # Augen
        canvas.create_oval(
            x - 8, head_y - 5, x - 4, head_y - 1,
            fill="black", tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + 4, head_y - 5, x + 8, head_y - 1,
            fill="black", tags="pokemon_sprite"
        )
        
        # Beine (4 kleine Kreise)
        leg_positions = [(-shell_size//3, shell_size//3), (shell_size//3, shell_size//3),
                        (-shell_size//3, -shell_size//6), (shell_size//3, -shell_size//6)]
        for leg_x, leg_y in leg_positions:
            canvas.create_oval(
                x + leg_x - 8, y + leg_y - 8,
                x + leg_x + 8, y + leg_y + 8,
                fill="#6699FF", outline="#2266CC", width=2, tags="pokemon_sprite"
            )
        
        # Wassertropfen (für Wasser-Typ)
        canvas.create_polygon(
            x + shell_size//2 + 10, y - 20,
            x + shell_size//2 + 15, y - 10,
            x + shell_size//2 + 5, y - 10,
            fill="#00AAFF", outline="", tags="pokemon_sprite"
        )
    
    @staticmethod
    def _draw_bisasam(canvas, x, y, size, color):
        """Zeichnet Bisasam - Pflanze mit Zwiebel"""
        # Körper (grüner Kreis)
        body_size = size * 0.6
        canvas.create_oval(
            x - body_size//2, y - body_size//2,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#228833", width=3, tags="pokemon_sprite"
        )
        
        # Zwiebel auf dem Rücken (größerer grüner Kreis oben)
        bulb_size = size * 0.5
        bulb_y = y - body_size//3
        canvas.create_oval(
            x - bulb_size//2, bulb_y - bulb_size//2,
            x + bulb_size//2, bulb_y + bulb_size//2,
            fill="#66BB66", outline="#228833", width=3, tags="pokemon_sprite"
        )
        
        # Flecken auf der Zwiebel
        for i in range(4):
            angle = i * math.pi / 2
            spot_x = x + math.cos(angle) * bulb_size//4
            spot_y = bulb_y + math.sin(angle) * bulb_size//4
            canvas.create_oval(
                spot_x - 4, spot_y - 4, spot_x + 4, spot_y + 4,
                fill="#339944", outline="", tags="pokemon_sprite"
            )
        
        # Augen (freundlich)
        canvas.create_oval(x - 10, y - 8, x - 6, y - 4, fill="black", tags="pokemon_sprite")
        canvas.create_oval(x + 6, y - 8, x + 10, y - 4, fill="black", tags="pokemon_sprite")
        
        # Kleine weiße Glanzpunkte in den Augen
        canvas.create_oval(x - 9, y - 7, x - 7, y - 5, fill="white", tags="pokemon_sprite")
        canvas.create_oval(x + 7, y - 7, x + 9, y - 5, fill="white", tags="pokemon_sprite")
        
        # Beine
        canvas.create_oval(
            x - body_size//2 - 5, y + body_size//3,
            x - body_size//2 + 5, y + body_size//3 + 15,
            fill=color, outline="#228833", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_size//2 - 5, y + body_size//3,
            x + body_size//2 + 5, y + body_size//3 + 15,
            fill=color, outline="#228833", width=2, tags="pokemon_sprite"
        )
        
        # Kleine Blätter um die Zwiebel
        for i in range(3):
            angle = i * 2 * math.pi / 3
            leaf_x = x + math.cos(angle) * (bulb_size//2 + 8)
            leaf_y = bulb_y + math.sin(angle) * (bulb_size//2 + 8)
            canvas.create_polygon(
                leaf_x, leaf_y - 8,
                leaf_x - 6, leaf_y + 4,
                leaf_x + 6, leaf_y + 4,
                fill="#44AA44", outline="", tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_pikachu(canvas, x, y, size, color):
        """Zeichnet Pikachu - Elektro-Maus"""
        # Körper (gelber Kreis)
        body_size = size * 0.7
        canvas.create_oval(
            x - body_size//2, y - body_size//2,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#CCAA00", width=3, tags="pokemon_sprite"
        )
        
        # Ohren (spitze Dreiecke oben)
        ear_height = size * 0.4
        # Linkes Ohr
        canvas.create_polygon(
            x - body_size//3, y - body_size//2,
            x - body_size//3 - 10, y - body_size//2 - ear_height,
            x - body_size//3 + 10, y - body_size//2 - ear_height + 5,
            fill=color, outline="#CCAA00", width=2, tags="pokemon_sprite"
        )
        # Schwarze Ohrenspitzen
        canvas.create_polygon(
            x - body_size//3 - 8, y - body_size//2 - ear_height + 5,
            x - body_size//3 - 10, y - body_size//2 - ear_height,
            x - body_size//3 + 5, y - body_size//2 - ear_height + 8,
            fill="black", tags="pokemon_sprite"
        )
        
        # Rechtes Ohr
        canvas.create_polygon(
            x + body_size//3, y - body_size//2,
            x + body_size//3 + 10, y - body_size//2 - ear_height,
            x + body_size//3 - 10, y - body_size//2 - ear_height + 5,
            fill=color, outline="#CCAA00", width=2, tags="pokemon_sprite"
        )
        canvas.create_polygon(
            x + body_size//3 + 8, y - body_size//2 - ear_height + 5,
            x + body_size//3 + 10, y - body_size//2 - ear_height,
            x + body_size//3 - 5, y - body_size//2 - ear_height + 8,
            fill="black", tags="pokemon_sprite"
        )
        
        # Augen (große schwarze Kreise)
        canvas.create_oval(x - 12, y - 12, x - 4, y - 4, fill="black", tags="pokemon_sprite")
        canvas.create_oval(x + 4, y - 12, x + 12, y - 4, fill="black", tags="pokemon_sprite")
        
        # Weiße Glanzpunkte
        canvas.create_oval(x - 10, y - 10, x - 6, y - 6, fill="white", tags="pokemon_sprite")
        canvas.create_oval(x + 6, y - 10, x + 10, y - 6, fill="white", tags="pokemon_sprite")
        
        # Rote Wangen (Elektro-Beutel)
        canvas.create_oval(
            x - body_size//2 - 5, y - 5,
            x - body_size//2 + 10, y + 10,
            fill="#FF6666", outline="", tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_size//2 - 10, y - 5,
            x + body_size//2 + 5, y + 10,
            fill="#FF6666", outline="", tags="pokemon_sprite"
        )
        
        # Schwanz (Blitz-Form)
        tail_points = [
            x + body_size//2, y,
            x + body_size//2 + 15, y - 10,
            x + body_size//2 + 25, y - 5,
            x + body_size//2 + 20, y + 5,
            x + body_size//2 + 30, y + 15,
            x + body_size//2 + 15, y + 10
        ]
        canvas.create_polygon(tail_points, fill=color, outline="#CCAA00", width=2, tags="pokemon_sprite")
        
        # Elektro-Funken
        for i in range(3):
            spark_x = x + body_size//2 + 35 + i * 8
            spark_y = y - 15 + i * 10
            canvas.create_line(
                spark_x - 3, spark_y - 3, spark_x + 3, spark_y + 3,
                fill="#FFFF00", width=2, tags="pokemon_sprite"
            )
            canvas.create_line(
                spark_x - 3, spark_y + 3, spark_x + 3, spark_y - 3,
                fill="#FFFF00", width=2, tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_rattfratz(canvas, x, y, size, color):
        """Zeichnet Rattfratz - Ratte"""
        # Körper (länglicher Kreis)
        body_width = size * 0.8
        body_height = size * 0.5
        canvas.create_oval(
            x - body_width//2, y - body_height//2,
            x + body_width//2, y + body_height//2,
            fill=color, outline="#885544", width=2, tags="pokemon_sprite"
        )
        
        # Kopf (Kreis vorne)
        head_size = size * 0.4
        head_x = x - body_width//3
        canvas.create_oval(
            head_x - head_size//2, y - head_size//2,
            head_x + head_size//2, y + head_size//2,
            fill=color, outline="#885544", width=2, tags="pokemon_sprite"
        )
        
        # Lange Nase
        canvas.create_oval(
            head_x - head_size//2 - 10, y - 8,
            head_x - head_size//2 + 5, y + 8,
            fill="#DDBB99", outline="#885544", width=1, tags="pokemon_sprite"
        )
        
        # Große Vorderzähne
        canvas.create_rectangle(
            head_x - head_size//2 - 8, y - 3,
            head_x - head_size//2 - 4, y + 8,
            fill="white", outline="black", width=1, tags="pokemon_sprite"
        )
        canvas.create_rectangle(
            head_x - head_size//2 - 2, y - 3,
            head_x - head_size//2 + 2, y + 8,
            fill="white", outline="black", width=1, tags="pokemon_sprite"
        )
        
        # Ohren (spitz)
        canvas.create_polygon(
            head_x - 5, y - head_size//2,
            head_x - 12, y - head_size//2 - 15,
            head_x + 2, y - head_size//2 - 8,
            fill=color, outline="#885544", width=1, tags="pokemon_sprite"
        )
        canvas.create_polygon(
            head_x + 5, y - head_size//2,
            head_x + 12, y - head_size//2 - 15,
            head_x - 2, y - head_size//2 - 8,
            fill=color, outline="#885544", width=1, tags="pokemon_sprite"
        )
        
        # Augen (kleine schwarze Punkte)
        canvas.create_oval(head_x - 8, y - 8, head_x - 4, y - 4, fill="black", tags="pokemon_sprite")
        canvas.create_oval(head_x + 4, y - 8, head_x + 8, y - 4, fill="black", tags="pokemon_sprite")
        
        # Langer Schwanz (gewellt)
        tail_start_x = x + body_width//2
        for i in range(5):
            segment_x = tail_start_x + i * 12
            segment_y = y + math.sin(i * 0.8) * 8
            canvas.create_oval(
                segment_x - 3, segment_y - 3,
                segment_x + 3, segment_y + 3,
                fill=color, outline="", tags="pokemon_sprite"
            )
        
        # Pfoten
        canvas.create_oval(
            x - body_width//2 - 5, y + body_height//2 - 5,
            x - body_width//2 + 5, y + body_height//2 + 10,
            fill=color, outline="#885544", width=1, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_width//3, y + body_height//2 - 5,
            x + body_width//3 + 10, y + body_height//2 + 10,
            fill=color, outline="#885544", width=1, tags="pokemon_sprite"
        )
    
    @staticmethod
    def _draw_taubsi(canvas, x, y, size, color):
        """Zeichnet Taubsi - kleiner Vogel"""
        # Körper (ovaler Kreis)
        body_size = size * 0.6
        canvas.create_oval(
            x - body_size//2, y - body_size//4,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#996633", width=2, tags="pokemon_sprite"
        )
        
        # Kopf (kleinerer Kreis oben)
        head_size = size * 0.35
        head_y = y - body_size//3
        canvas.create_oval(
            x - head_size//2, head_y - head_size//2,
            x + head_size//2, head_y + head_size//2,
            fill=color, outline="#996633", width=2, tags="pokemon_sprite"
        )
        
        # Schnabel (orange Dreieck)
        canvas.create_polygon(
            x - head_size//2 - 8, head_y,
            x - head_size//2 - 15, head_y - 5,
            x - head_size//2 - 15, head_y + 5,
            fill="#FF8800", outline="#CC6600", width=1, tags="pokemon_sprite"
        )
        
        # Augen (große schwarze Kreise)
        canvas.create_oval(x - 6, head_y - 6, x - 2, head_y - 2, fill="black", tags="pokemon_sprite")
        canvas.create_oval(x + 2, head_y - 6, x + 6, head_y - 2, fill="black", tags="pokemon_sprite")
        
        # Weiße Glanzpunkte
        canvas.create_oval(x - 5, head_y - 5, x - 3, head_y - 3, fill="white", tags="pokemon_sprite")
        canvas.create_oval(x + 3, head_y - 5, x + 5, head_y - 3, fill="white", tags="pokemon_sprite")
        
        # Flügel (links und rechts)
        # Linker Flügel
        wing_points_left = [
            x - body_size//2, y - body_size//6,
            x - body_size//2 - 20, y - body_size//3,
            x - body_size//2 - 25, y,
            x - body_size//2 - 15, y + body_size//6,
            x - body_size//2, y
        ]
        canvas.create_polygon(wing_points_left, fill="#BBAA88", outline="#996633", width=1, tags="pokemon_sprite")
        
        # Rechter Flügel
        wing_points_right = [
            x + body_size//2, y - body_size//6,
            x + body_size//2 + 20, y - body_size//3,
            x + body_size//2 + 25, y,
            x + body_size//2 + 15, y + body_size//6,
            x + body_size//2, y
        ]
        canvas.create_polygon(wing_points_right, fill="#BBAA88", outline="#996633", width=1, tags="pokemon_sprite")
        
        # Schwanzfedern
        for i in range(3):
            tail_x = x + body_size//2 + 5 + i * 8
            tail_y = y + body_size//4 + i * 3
            canvas.create_polygon(
                tail_x, tail_y,
                tail_x + 15, tail_y - 10,
                tail_x + 20, tail_y + 5,
                tail_x + 10, tail_y + 8,
                fill="#BBAA88", outline="#996633", width=1, tags="pokemon_sprite"
            )
        
        # Kleine Krallen
        canvas.create_line(x - 5, y + body_size//2, x - 5, y + body_size//2 + 8, fill="black", width=2, tags="pokemon_sprite")
        canvas.create_line(x + 5, y + body_size//2, x + 5, y + body_size//2 + 8, fill="black", width=2, tags="pokemon_sprite")
    
    @staticmethod
    def _draw_raupy(canvas, x, y, size, color):
        """Zeichnet Raupy - Raupe"""
        # Körper (mehrere verbundene Kreise)
        segment_size = size // 6
        num_segments = 5
        
        for i in range(num_segments):
            segment_x = x - (num_segments//2 - i) * segment_size
            segment_y = y + math.sin(i * 0.5) * 5
            
            # Wechselnde Farben für Segmente
            seg_color = color if i % 2 == 0 else "#66AA66"
            
            canvas.create_oval(
                segment_x - segment_size, segment_y - segment_size,
                segment_x + segment_size, segment_y + segment_size,
                fill=seg_color, outline="#556644", width=2, tags="pokemon_sprite"
            )
        
        # Kopf (vorderstes Segment, größer)
        head_x = x - (num_segments//2) * segment_size - segment_size//2
        head_size = segment_size * 1.2
        canvas.create_oval(
            head_x - head_size, y - head_size,
            head_x + head_size, y + head_size,
            fill=color, outline="#556644", width=3, tags="pokemon_sprite"
        )
        
        # Große Augen
        canvas.create_oval(
            head_x - head_size//2, y - head_size//2,
            head_x - head_size//4, y - head_size//4,
            fill="black", outline="white", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            head_x + head_size//4, y - head_size//2,
            head_x + head_size//2, y - head_size//4,
            fill="black", outline="white", width=2, tags="pokemon_sprite"
        )
        
        # Antennenfühler
        canvas.create_line(
            head_x - head_size//3, y - head_size,
            head_x - head_size//3 - 8, y - head_size - 12,
            fill="#556644", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            head_x - head_size//3 - 10, y - head_size - 15,
            head_x - head_size//3 - 6, y - head_size - 11,
            fill="#FF6666", tags="pokemon_sprite"
        )
        
        canvas.create_line(
            head_x + head_size//3, y - head_size,
            head_x + head_size//3 + 8, y - head_size - 12,
            fill="#556644", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            head_x + head_size//3 + 6, y - head_size - 15,
            head_x + head_size//3 + 10, y - head_size - 11,
            fill="#FF6666", tags="pokemon_sprite"
        )
        
        # Kleine Beine unter jedem Segment
        for i in range(num_segments):
            segment_x = x - (num_segments//2 - i) * segment_size
            leg_y = y + segment_size + 2
            canvas.create_oval(
                segment_x - 3, leg_y,
                segment_x + 3, leg_y + 6,
                fill="#556644", tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_hornliu(canvas, x, y, size, color):
        """Zeichnet Hornliu - Gift-Käfer"""
        # Körper (oval)
        body_width = size * 0.7
        body_height = size * 0.5
        canvas.create_oval(
            x - body_width//2, y - body_height//2,
            x + body_width//2, y + body_height//2,
            fill=color, outline="#663366", width=3, tags="pokemon_sprite"
        )
        
        # Horn (großer Stachel oben)
        horn_points = [
            x, y - body_height//2,
            x - 8, y - body_height//2 - 25,
            x + 8, y - body_height//2 - 25
        ]
        canvas.create_polygon(horn_points, fill="#444444", outline="black", width=2, tags="pokemon_sprite")
        
        # Giftstacheln am Horn
        for i in range(3):
            spike_y = y - body_height//2 - 5 - i * 6
            canvas.create_polygon(
                x - 3 - i, spike_y,
                x - 8 - i, spike_y - 4,
                x + 2 - i, spike_y - 2,
                fill="#AA44AA", tags="pokemon_sprite"
            )
            canvas.create_polygon(
                x + 3 + i, spike_y,
                x + 8 + i, spike_y - 4,
                x - 2 + i, spike_y - 2,
                fill="#AA44AA", tags="pokemon_sprite"
            )
        
        # Komplexe Augen (facettiert)
        eye_size = 12
        canvas.create_oval(
            x - body_width//3 - eye_size//2, y - 8,
            x - body_width//3 + eye_size//2, y + 8,
            fill="#FF4444", outline="black", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_width//3 - eye_size//2, y - 8,
            x + body_width//3 + eye_size//2, y + 8,
            fill="#FF4444", outline="black", width=2, tags="pokemon_sprite"
        )
        
        # Facetten in den Augen
        for i in range(3):
            for j in range(3):
                facet_x = x - body_width//3 - 6 + i * 4
                facet_y = y - 6 + j * 4
                canvas.create_oval(
                    facet_x, facet_y, facet_x + 2, facet_y + 2,
                    fill="#660000", tags="pokemon_sprite"
                )
                facet_x = x + body_width//3 - 6 + i * 4
                canvas.create_oval(
                    facet_x, facet_y, facet_x + 2, facet_y + 2,
                    fill="#660000", tags="pokemon_sprite"
                )
        
        # Beine (6 Stück)
        leg_positions = [
            (-body_width//2 - 5, -body_height//4),
            (-body_width//2 - 5, 0),
            (-body_width//2 - 5, body_height//4),
            (body_width//2 + 5, -body_height//4),
            (body_width//2 + 5, 0),
            (body_width//2 + 5, body_height//4)
        ]
        
        for leg_x, leg_y in leg_positions:
            canvas.create_line(
                x + leg_x//2, y + leg_y,
                x + leg_x, y + leg_y + 10,
                fill="#663366", width=3, tags="pokemon_sprite"
            )
            # Kleine Klauen
            canvas.create_oval(
                x + leg_x - 2, y + leg_y + 8,
                x + leg_x + 2, y + leg_y + 12,
                fill="black", tags="pokemon_sprite"
            )
        
        # Giftige Aura (lila Punkte)
        for i in range(5):
            aura_x = x + (i - 2) * 15 + math.sin(i) * 10
            aura_y = y - body_height//2 - 35 - math.cos(i) * 8
            canvas.create_oval(
                aura_x - 2, aura_y - 2, aura_x + 2, aura_y + 2,
                fill="#BB66BB", outline="", tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_zubat(canvas, x, y, size, color):
        """Zeichnet Zubat - Fledermaus"""
        # Körper (kleiner Kreis)
        body_size = size * 0.4
        canvas.create_oval(
            x - body_size//2, y - body_size//2,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#442266", width=2, tags="pokemon_sprite"
        )
        
        # Keine Augen (blind)
        # Aber große Ohren
        ear_points_left = [
            x - body_size//2, y - body_size//2,
            x - body_size//2 - 15, y - body_size//2 - 20,
            x - body_size//2 - 8, y - body_size//2 - 5,
        ]
        canvas.create_polygon(ear_points_left, fill=color, outline="#442266", width=2, tags="pokemon_sprite")
        
        ear_points_right = [
            x + body_size//2, y - body_size//2,
            x + body_size//2 + 15, y - body_size//2 - 20,
            x + body_size//2 + 8, y - body_size//2 - 5,
        ]
        canvas.create_polygon(ear_points_right, fill=color, outline="#442266", width=2, tags="pokemon_sprite")
        
        # Große Flügel (Membran)
        # Linker Flügel
        wing_left_points = [
            x - body_size//2, y,
            x - body_size//2 - 30, y - 15,
            x - body_size//2 - 35, y + 5,
            x - body_size//2 - 25, y + 20,
            x - body_size//2 - 10, y + 15,
            x - body_size//2, y + body_size//2
        ]
        canvas.create_polygon(wing_left_points, fill="#6644AA", outline="#442266", width=2, tags="pokemon_sprite")
        
        # Rechter Flügel
        wing_right_points = [
            x + body_size//2, y,
            x + body_size//2 + 30, y - 15,
            x + body_size//2 + 35, y + 5,
            x + body_size//2 + 25, y + 20,
            x + body_size//2 + 10, y + 15,
            x + body_size//2, y + body_size//2
        ]
        canvas.create_polygon(wing_right_points, fill="#6644AA", outline="#442266", width=2, tags="pokemon_sprite")
        
        # Flügel-Membrane (dünne Linien)
        for i in range(4):
            membrane_x = x - body_size//2 - 10 - i * 6
            canvas.create_line(
                membrane_x, y - 5, membrane_x, y + 15,
                fill="#442266", width=1, tags="pokemon_sprite"
            )
            membrane_x = x + body_size//2 + 10 + i * 6
            canvas.create_line(
                membrane_x, y - 5, membrane_x, y + 15,
                fill="#442266", width=1, tags="pokemon_sprite"
            )
        
        # Mund (geöffnet für Echolot)
        canvas.create_oval(
            x - 4, y + 2, x + 4, y + 8,
            fill="black", outline="", tags="pokemon_sprite"
        )
        
        # Kleine weiße Reißzähne
        canvas.create_polygon(
            x - 2, y + 3, x - 4, y + 6, x, y + 6,
            fill="white", tags="pokemon_sprite"
        )
        canvas.create_polygon(
            x + 2, y + 3, x + 4, y + 6, x, y + 6,
            fill="white", tags="pokemon_sprite"
        )
        
        # Schallwellen (für Echolot)
        for i in range(3):
            wave_radius = (i + 1) * 8
            canvas.create_arc(
                x - wave_radius, y - wave_radius,
                x + wave_radius, y + wave_radius,
                start=70, extent=40,
                outline="#AAAAFF", width=1, style="arc", tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_digda(canvas, x, y, size, color):
        """Zeichnet Digda - Maulwurf (nur Kopf sichtbar)"""
        # Erdloch (braunes Oval)
        hole_width = size * 0.8
        hole_height = size * 0.3
        canvas.create_oval(
            x - hole_width//2, y + size//4,
            x + hole_width//2, y + size//4 + hole_height,
            fill="#654321", outline="#543210", width=3, tags="pokemon_sprite"
        )
        
        # Kopf (aus der Erde ragend)
        head_size = size * 0.6
        canvas.create_oval(
            x - head_size//2, y - head_size//4,
            x + head_size//2, y + head_size//2,
            fill=color, outline="#996633", width=3, tags="pokemon_sprite"
        )
        
        # Nase (rosa Kreis)
        nose_size = 8
        canvas.create_oval(
            x - nose_size//2, y,
            x + nose_size//2, y + nose_size,
            fill="#FF8888", outline="#CC6666", width=2, tags="pokemon_sprite"
        )
        
        # Augen (kleine schwarze Punkte)
        canvas.create_oval(x - 8, y - 10, x - 4, y - 6, fill="black", tags="pokemon_sprite")
        canvas.create_oval(x + 4, y - 10, x + 8, y - 6, fill="black", tags="pokemon_sprite")
        
        # Kleine weiße Glanzpunkte
        canvas.create_oval(x - 7, y - 9, x - 5, y - 7, fill="white", tags="pokemon_sprite")
        canvas.create_oval(x + 5, y - 9, x + 7, y - 7, fill="white", tags="pokemon_sprite")
        
        # Whiskers/Schnurrhaare
        canvas.create_line(x - head_size//2, y - 5, x - head_size//2 - 10, y - 8, fill="black", width=1, tags="pokemon_sprite")
        canvas.create_line(x - head_size//2, y + 5, x - head_size//2 - 10, y + 2, fill="black", width=1, tags="pokemon_sprite")
        canvas.create_line(x + head_size//2, y - 5, x + head_size//2 + 10, y - 8, fill="black", width=1, tags="pokemon_sprite")
        canvas.create_line(x + head_size//2, y + 5, x + head_size//2 + 10, y + 2, fill="black", width=1, tags="pokemon_sprite")
        
        # Kleine Erdklumpen um das Loch
        for i in range(4):
            clump_angle = i * math.pi / 2
            clump_x = x + math.cos(clump_angle) * (hole_width//2 + 15)
            clump_y = y + size//4 + hole_height//2 + math.sin(clump_angle) * 10
            canvas.create_oval(
                clump_x - 4, clump_y - 4, clump_x + 4, clump_y + 4,
                fill="#654321", outline="", tags="pokemon_sprite"
            )
        
        # Tunnel-Andeutung (dunkler Bereich im Loch)
        canvas.create_oval(
            x - hole_width//3, y + size//4 + 5,
            x + hole_width//3, y + size//4 + hole_height - 5,
            fill="#332211", outline="", tags="pokemon_sprite"
        )
    
    @staticmethod
    def _draw_abra(canvas, x, y, size, color):
        """Zeichnet Abra - Psycho-Humanoid"""
        # Körper (gelber humanoider Kreis)
        body_size = size * 0.6
        canvas.create_oval(
            x - body_size//2, y - body_size//4,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#CC9900", width=2, tags="pokemon_sprite"
        )
        
        # Kopf (größer, typisch für Psycho-Types)
        head_size = size * 0.5
        head_y = y - body_size//3
        canvas.create_oval(
            x - head_size//2, head_y - head_size//2,
            x + head_size//2, head_y + head_size//2,
            fill=color, outline="#CC9900", width=2, tags="pokemon_sprite"
        )
        
        # Geschlossene Augen (schläft/meditiert)
        canvas.create_arc(
            x - 12, head_y - 8, x - 4, head_y,
            start=0, extent=180, fill="black", width=2, tags="pokemon_sprite"
        )
        canvas.create_arc(
            x + 4, head_y - 8, x + 12, head_y,
            start=0, extent=180, fill="black", width=2, tags="pokemon_sprite"
        )
        
        # Psychische Aura (leuchtende Kreise um den Kopf)
        for i in range(3):
            aura_radius = head_size//2 + 10 + i * 8
            canvas.create_oval(
                x - aura_radius, head_y - aura_radius,
                x + aura_radius, head_y + aura_radius,
                outline="#FFAAFF", width=1, fill="", tags="pokemon_sprite"
            )
        
        # Arme (dünn, humanoider Stil)
        # Linker Arm
        canvas.create_line(
            x - body_size//2, y - body_size//6,
            x - body_size//2 - 15, y + body_size//6,
            fill=color, width=5, tags="pokemon_sprite"
        )
        # Hand
        canvas.create_oval(
            x - body_size//2 - 18, y + body_size//6 - 4,
            x - body_size//2 - 10, y + body_size//6 + 4,
            fill=color, outline="#CC9900", width=1, tags="pokemon_sprite"
        )
        
        # Rechter Arm
        canvas.create_line(
            x + body_size//2, y - body_size//6,
            x + body_size//2 + 15, y + body_size//6,
            fill=color, width=5, tags="pokemon_sprite"
        )
        # Hand
        canvas.create_oval(
            x + body_size//2 + 10, y + body_size//6 - 4,
            x + body_size//2 + 18, y + body_size//6 + 4,
            fill=color, outline="#CC9900", width=1, tags="pokemon_sprite"
        )
        
        # Beine (einfache Linien)
        canvas.create_line(
            x - body_size//4, y + body_size//2,
            x - body_size//4, y + body_size//2 + 15,
            fill=color, width=5, tags="pokemon_sprite"
        )
        canvas.create_line(
            x + body_size//4, y + body_size//2,
            x + body_size//4, y + body_size//2 + 15,
            fill=color, width=5, tags="pokemon_sprite"
        )
        
        # Füße
        canvas.create_oval(
            x - body_size//4 - 6, y + body_size//2 + 12,
            x - body_size//4 + 6, y + body_size//2 + 18,
            fill=color, outline="#CC9900", width=1, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_size//4 - 6, y + body_size//2 + 12,
            x + body_size//4 + 6, y + body_size//2 + 18,
            fill=color, outline="#CC9900", width=1, tags="pokemon_sprite"
        )
        
        # Psychische Energie-Funken
        for i in range(6):
            spark_angle = i * math.pi / 3
            spark_x = x + math.cos(spark_angle) * (head_size//2 + 25)
            spark_y = head_y + math.sin(spark_angle) * (head_size//2 + 25)
            canvas.create_polygon(
                spark_x, spark_y - 3,
                spark_x - 3, spark_y + 3,
                spark_x + 3, spark_y + 3,
                fill="#FFAAFF", outline="", tags="pokemon_sprite"
            )
        
        # Meditierende Pose-Indikator (kleine Schwebelinien)
        for i in range(3):
            hover_y = y + body_size//2 + 20 + i * 3
            canvas.create_line(
                x - 15, hover_y, x + 15, hover_y,
                fill="#DDDDDD", width=1, tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_machollo(canvas, x, y, size, color):
        """Zeichnet Machollo - Kampf-Pokemon"""
        # Muskulöser Körper
        body_size = size * 0.7
        canvas.create_oval(
            x - body_size//2, y - body_size//3,
            x + body_size//2, y + body_size//2,
            fill=color, outline="#993333", width=3, tags="pokemon_sprite"
        )
        
        # Kopf (kleiner als Körper, typisch für Kämpfer)
        head_size = size * 0.4
        head_y = y - body_size//2
        canvas.create_oval(
            x - head_size//2, head_y - head_size//2,
            x + head_size//2, head_y + head_size//2,
            fill=color, outline="#993333", width=2, tags="pokemon_sprite"
        )
        
        # Entschlossene Augen
        canvas.create_polygon(
            x - 8, head_y - 5, x - 12, head_y - 8, x - 4, head_y - 8,
            fill="black", tags="pokemon_sprite"
        )
        canvas.create_polygon(
            x + 8, head_y - 5, x + 12, head_y - 8, x + 4, head_y - 8,
            fill="black", tags="pokemon_sprite"
        )
        
        # Weiße Glanzpunkte (entschlossener Blick)
        canvas.create_oval(x - 7, head_y - 7, x - 5, head_y - 5, fill="white", tags="pokemon_sprite")
        canvas.create_oval(x + 5, head_y - 7, x + 7, head_y - 5, fill="white", tags="pokemon_sprite")
        
        # Muskulöse Arme (sehr groß)
        # Linker Arm (angewinkelt)
        arm_points_left = [
            x - body_size//2, y - body_size//4,
            x - body_size//2 - 25, y - body_size//6,
            x - body_size//2 - 30, y + body_size//6,
            x - body_size//2 - 15, y + body_size//4,
            x - body_size//2, y
        ]
        canvas.create_polygon(arm_points_left, fill=color, outline="#993333", width=2, tags="pokemon_sprite")
        
        # Bizeps-Wölbung (linker Arm)
        canvas.create_oval(
            x - body_size//2 - 22, y - body_size//4,
            x - body_size//2 - 8, y - body_size//12,
            fill="#DD6666", outline="#993333", width=1, tags="pokemon_sprite"
        )
        
        # Rechter Arm (angewinkelt)
        arm_points_right = [
            x + body_size//2, y - body_size//4,
            x + body_size//2 + 25, y - body_size//6,
            x + body_size//2 + 30, y + body_size//6,
            x + body_size//2 + 15, y + body_size//4,
            x + body_size//2, y
        ]
        canvas.create_polygon(arm_points_right, fill=color, outline="#993333", width=2, tags="pokemon_sprite")
        
        # Bizeps-Wölbung (rechter Arm)
        canvas.create_oval(
            x + body_size//2 + 8, y - body_size//4,
            x + body_size//2 + 22, y - body_size//12,
            fill="#DD6666", outline="#993333", width=1, tags="pokemon_sprite"
        )
        
        # Fäuste
        canvas.create_oval(
            x - body_size//2 - 18, y + body_size//4 - 6,
            x - body_size//2 - 6, y + body_size//4 + 6,
            fill=color, outline="#993333", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_size//2 + 6, y + body_size//4 - 6,
            x + body_size//2 + 18, y + body_size//4 + 6,
            fill=color, outline="#993333", width=2, tags="pokemon_sprite"
        )
        
        # Bauchmuskeln (Sixpack-Andeutung)
        for i in range(3):
            for j in range(2):
                muscle_x = x - 8 + j * 16
                muscle_y = y - body_size//6 + i * 12
                canvas.create_oval(
                    muscle_x - 4, muscle_y - 3,
                    muscle_x + 4, muscle_y + 3,
                    fill="#DD6666", outline="", tags="pokemon_sprite"
                )
        
        # Kräftige Beine
        canvas.create_oval(
            x - body_size//3, y + body_size//2 - 5,
            x - body_size//3 + 15, y + body_size//2 + 25,
            fill=color, outline="#993333", width=2, tags="pokemon_sprite"
        )
        canvas.create_oval(
            x + body_size//3 - 15, y + body_size//2 - 5,
            x + body_size//3, y + body_size//2 + 25,
            fill=color, outline="#993333", width=2, tags="pokemon_sprite"
        )
        
        # Gürtel (Kampfsport-Andeutung)
        canvas.create_rectangle(
            x - body_size//2, y + body_size//6,
            x + body_size//2, y + body_size//6 + 8,
            fill="#FFD700", outline="#CC9900", width=1, tags="pokemon_sprite"
        )
        
        # Kraftlinien (Aura der Stärke)
        for i in range(4):
            line_angle = i * math.pi / 2
            line_start_x = x + math.cos(line_angle) * body_size//2
            line_start_y = y + math.sin(line_angle) * body_size//2
            line_end_x = x + math.cos(line_angle) * (body_size//2 + 12)
            line_end_y = y + math.sin(line_angle) * (body_size//2 + 12)
            
            canvas.create_line(
                line_start_x, line_start_y, line_end_x, line_end_y,
                fill="#FFFF00", width=2, tags="pokemon_sprite"
            )
    
    @staticmethod
    def _draw_default(canvas, x, y, size, color):
        """Standard-Pokemon Darstellung (einfacher Kreis)"""
        canvas.create_oval(
            x - size//2, y - size//2,
            x + size//2, y + size//2,
            fill=color, outline="black", width=3, tags="pokemon_sprite"
        )
        
        # Einfache Augen
        canvas.create_oval(x - 8, y - 8, x - 4, y - 4, fill="black", tags="pokemon_sprite")
        canvas.create_oval(x + 4, y - 8, x + 8, y - 4, fill="black", tags="pokemon_sprite")