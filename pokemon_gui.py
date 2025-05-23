# pokemon_gui.py
"""
Grafische Benutzeroberfläche für das Pokemon-Spiel
"""
import tkinter as tk
from tkinter import ttk, messagebox, font
import random
from pokemon import Pokemon
from trainer_class import Trainer
from battle import Battle, create_wild_pokemon
from pokemon_sprites import PokemonSprite
from game_data import (
    STARTER_POKEMON,
    POKEMON_DATA,
    COLORS,
    GAME_CONFIG,
    MAP_TILES,
    WORLD_MAP,
    SPECIAL_LOCATIONS,
    FONT_CONFIG,
)


class GameMap:
    def __init__(self, parent, width, height):
        self.parent = parent
        self.width = width
        self.height = height
        self.tile_size = GAME_CONFIG["map_tile_size"]

        # Spieler Position
        self.player_x = 10
        self.player_y = 7

        # Canvas für Map
        self.canvas = tk.Canvas(
            parent,
            width=width * self.tile_size,
            height=height * self.tile_size,
            bg=COLORS["bg_main"],
            highlightthickness=2,
            highlightbackground=COLORS["accent"],
        )

        # Map-Daten laden
        self.map_data = WORLD_MAP

        # Map zeichnen
        self.draw_map()
        self.draw_player()

        # Tastatur-Events
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.on_key_press)

        # Callback für Pokemon-Begegnungen
        self.encounter_callback = None
        self.special_location_callback = None

    def draw_map(self):
        """Zeichnet die komplette Map"""
        self.canvas.delete("map_tile")

        for y, row in enumerate(self.map_data):
            for x, tile_char in enumerate(row):
                if tile_char in MAP_TILES:
                    tile_info = MAP_TILES[tile_char]

                    x1 = x * self.tile_size
                    y1 = y * self.tile_size
                    x2 = x1 + self.tile_size
                    y2 = y1 + self.tile_size

                    # Tile zeichnen
                    self.canvas.create_rectangle(
                        x1,
                        y1,
                        x2,
                        y2,
                        fill=tile_info["color"],
                        outline=COLORS["text_secondary"],
                        width=1,
                        tags="map_tile",
                    )

                    # Spezielle Markierungen
                    if tile_char == "C":  # Pokemon Center
                        self.canvas.create_text(
                            x1 + self.tile_size // 2,
                            y1 + self.tile_size // 2,
                            text="🏥",
                            font=("Arial", 16),
                            fill=COLORS["text_primary"],
                            tags="map_tile",
                        )
                    elif tile_char == "S":  # Shop
                        self.canvas.create_text(
                            x1 + self.tile_size // 2,
                            y1 + self.tile_size // 2,
                            text="🛒",
                            font=("Arial", 16),
                            fill=COLORS["text_primary"],
                            tags="map_tile",
                        )
                    elif tile_char == "W":  # Wasser
                        self.canvas.create_text(
                            x1 + self.tile_size // 2,
                            y1 + self.tile_size // 2,
                            text="〜",
                            font=("Arial", 12),
                            fill=COLORS["info"],
                            tags="map_tile",
                        )

    def draw_player(self):
        """Zeichnet den Spieler"""
        self.canvas.delete("player")

        x = self.player_x * self.tile_size
        y = self.player_y * self.tile_size

        # Spieler als Kreis mit Schatten
        self.canvas.create_oval(
            x + 6,
            y + 6,
            x + self.tile_size - 6,
            y + self.tile_size - 6,
            fill=COLORS["player"],
            outline=COLORS["text_primary"],
            width=3,
            tags="player",
        )

        # Spieler-Icon
        self.canvas.create_text(
            x + self.tile_size // 2,
            y + self.tile_size // 2,
            text="🧑",
            font=("Arial", 14),
            tags="player",
        )

    def can_move_to(self, x, y):
        """Prüft ob Bewegung zu Position möglich ist"""
        if x < 0 or y < 0 or x >= len(self.map_data[0]) or y >= len(self.map_data):
            return False

        tile_char = self.map_data[y][x]
        if tile_char in MAP_TILES:
            return MAP_TILES[tile_char]["walkable"]
        return False

    def move_player(self, dx, dy):
        """Bewegt Spieler um relative Position"""
        new_x = self.player_x + dx
        new_y = self.player_y + dy

        if self.can_move_to(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y
            self.draw_player()

            # Prüfe Begegnungen und spezielle Orte
            self.check_encounters()
            self.check_special_locations()
            return True
        return False

    def check_encounters(self):
        """Prüft Pokemon-Begegnungen"""
        tile_char = self.map_data[self.player_y][self.player_x]
        if tile_char in MAP_TILES and MAP_TILES[tile_char]["encounter"]:
            if random.random() < GAME_CONFIG["wild_pokemon_encounter_rate"]:
                if self.encounter_callback:
                    self.encounter_callback()

    def check_special_locations(self):
        """Prüft spezielle Orte"""
        pos = (self.player_x, self.player_y)
        if pos in SPECIAL_LOCATIONS:
            location = SPECIAL_LOCATIONS[pos]
            if self.special_location_callback:
                self.special_location_callback(location)

    def on_key_press(self, event):
        """Behandelt Tastatureingaben"""
        key = event.keysym.lower()

        if key in ["up", "w"]:
            self.move_player(0, -1)
        elif key in ["down", "s"]:
            self.move_player(0, 1)
        elif key in ["left", "a"]:
            self.move_player(-1, 0)
        elif key in ["right", "d"]:
            self.move_player(1, 0)


class PokemonGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokemon Rot - Python Edition")
        self.root.geometry("1400x900")  # Größeres Fenster
        self.root.minsize(1200, 800)  # Mindestgröße
        self.root.configure(bg=COLORS["bg_main"])
        self.root.resizable(True, True)  # Fenster vergrößerbar machen

        # Spiel-State
        self.player = None
        self.current_battle = None
        self.current_screen = "start"
        self.game_map = None

        # Verbesserte Fonts für bessere Lesbarkeit
        self.title_font = font.Font(
            family=FONT_CONFIG["family"], size=FONT_CONFIG["title_size"], weight="bold"
        )
        self.header_font = font.Font(
            family=FONT_CONFIG["family"], size=FONT_CONFIG["header_size"], weight="bold"
        )
        self.text_font = font.Font(
            family=FONT_CONFIG["family"], size=FONT_CONFIG["text_size"]
        )
        self.small_font = font.Font(
            family=FONT_CONFIG["family"], size=FONT_CONFIG["small_size"]
        )
        self.tiny_font = font.Font(
            family=FONT_CONFIG["family"], size=FONT_CONFIG["tiny_size"]
        )

        # Main Container
        self.main_frame = tk.Frame(self.root, bg=COLORS["bg_main"])
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.show_start_screen()

    def clear_screen(self):
        """Leert den Bildschirm"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_styled_button(self, parent, text, command, bg_color=None, width=20):
        """Erstellt einen stylischen Button mit besserer Lesbarkeit"""
        if not bg_color:
            bg_color = COLORS["accent"]

        btn = tk.Button(
            parent,
            text=text,
            font=self.text_font,
            bg=bg_color,
            fg=COLORS["text_primary"],
            command=command,
            width=width,
            pady=8,
            relief="flat",
            borderwidth=0,
            activebackground=COLORS["accent_light"],
            activeforeground=COLORS["text_primary"],
        )

        # Hover-Effekt
        def on_enter(e):
            btn.config(bg=COLORS["accent_light"])

        def on_leave(e):
            btn.config(bg=bg_color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    def create_info_card(self, parent, title, content, bg_color=None):
        """Erstellt eine Info-Karte mit besserer Lesbarkeit"""
        if not bg_color:
            bg_color = COLORS["bg_card"]

        card_frame = tk.Frame(parent, bg=bg_color, relief="solid", bd=2)

        # Title mit Schatten-Effekt
        title_label = tk.Label(
            card_frame,
            text=title,
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=bg_color,
        )
        title_label.pack(pady=(10, 5))

        # Content
        content_label = tk.Label(
            card_frame,
            text=content,
            font=self.text_font,
            fg=COLORS["text_primary"],
            bg=bg_color,
            justify="left",
            wraplength=300,
        )
        content_label.pack(pady=(0, 10), padx=15)

        return card_frame

    def show_start_screen(self):
        """Zeigt den Startbildschirm"""
        self.clear_screen()
        self.current_screen = "start"

        # Title mit Schatten
        title_frame = tk.Frame(self.main_frame, bg=COLORS["bg_main"])
        title_frame.pack(pady=60)

        title_label = tk.Label(
            title_frame,
            text="🎮 POKEMON ROT",
            font=self.title_font,
            fg=COLORS["accent"],
            bg=COLORS["bg_main"],
        )
        title_label.pack()

        subtitle = tk.Label(
            title_frame,
            text="Python Edition - With Amazing Graphics!",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_main"],
        )
        subtitle.pack(pady=10)

        # Info Card
        info_text = "🗺️ Laufe durch die Welt mit WASD oder Pfeiltasten\n⚔️ Kämpfe gegen wilde Pokemon\n🏥 Besuche das Pokemon-Center\n🎯 Sammle alle Pokemon!\n🎨 Genieße die neuen Pokemon-Grafiken!"
        info_card = self.create_info_card(title_frame, "Spielfeatures:", info_text)
        info_card.pack(pady=20)

        # Trainer Name Input
        name_frame = tk.Frame(
            self.main_frame, bg=COLORS["bg_card"], relief="solid", bd=2
        )
        name_frame.pack(pady=30, padx=50)

        tk.Label(
            name_frame,
            text="Dein Trainer-Name:",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        ).pack(pady=(15, 5))

        self.name_entry = tk.Entry(
            name_frame,
            font=self.text_font,
            width=25,
            bg=COLORS["bg_secondary"],
            fg=COLORS["text_primary"],
            insertbackground=COLORS["text_primary"],
            relief="solid",
            bd=2,
        )
        self.name_entry.pack(pady=10)
        self.name_entry.insert(0, "Ash")

        # Start Button
        start_btn = self.create_styled_button(
            name_frame, "🚀 Abenteuer starten!", self.show_starter_selection, width=25
        )
        start_btn.pack(pady=(10, 20))

    def show_starter_selection(self):
        """Zeigt die Starter-Pokemon Auswahl"""
        trainer_name = self.name_entry.get().strip()
        if not trainer_name:
            messagebox.showerror("Fehler", "Bitte gib deinen Namen ein!")
            return

        self.player = Trainer(trainer_name, True)

        self.clear_screen()
        self.current_screen = "starter"

        # Header
        header_frame = tk.Frame(self.main_frame, bg=COLORS["bg_main"])
        header_frame.pack(pady=30)

        welcome_label = tk.Label(
            header_frame,
            text=f"Willkommen, {trainer_name}!",
            font=self.title_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_main"],
        )
        welcome_label.pack()

        instruction = tk.Label(
            header_frame,
            text="Wähle dein Starter-Pokemon:",
            font=self.header_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_main"],
        )
        instruction.pack(pady=15)

        # Starter Pokemon Frame
        starter_frame = tk.Frame(self.main_frame, bg=COLORS["bg_main"])
        starter_frame.pack(pady=40)

        for i, starter_name in enumerate(STARTER_POKEMON):
            pokemon_data = POKEMON_DATA[starter_name]

            # Pokemon Card mit verbessertem Design
            card_frame = tk.Frame(
                starter_frame, bg=COLORS["bg_card"], relief="solid", bd=3
            )
            card_frame.grid(row=0, column=i, padx=25, pady=15)

            # Pokemon "Sprite" mit neuer Grafik-Engine
            canvas = tk.Canvas(
                card_frame,
                width=140,
                height=140,
                bg=COLORS["bg_card"],
                highlightthickness=0,
            )
            canvas.pack(pady=15)

            # Neues Pokemon-Sprite zeichnen
            PokemonSprite.draw_pokemon(canvas, starter_name, 70, 70, 80)

            # Pokemon Name
            name_label = tk.Label(
                card_frame,
                text=starter_name,
                font=self.header_font,
                fg=COLORS["text_accent"],
                bg=COLORS["bg_card"],
            )
            name_label.pack(pady=5)

            # Type mit Hintergrund
            type_frame = tk.Frame(
                card_frame, bg=pokemon_data["color"], relief="solid", bd=1
            )
            type_frame.pack(pady=5)
            type_label = tk.Label(
                type_frame,
                text=f"Typ: {pokemon_data['typ']}",
                font=self.small_font,
                fg=COLORS["text_primary"],
                bg=pokemon_data["color"],
            )
            type_label.pack(padx=10, pady=3)

            # Stats
            stats_text = f"HP: {pokemon_data['hp']} | ATK: {pokemon_data['attack']} | DEF: {pokemon_data['defense']}"
            stats_label = tk.Label(
                card_frame,
                text=stats_text,
                font=self.small_font,
                fg=COLORS["text_secondary"],
                bg=COLORS["bg_card"],
            )
            stats_label.pack(pady=5)

            # Description
            desc = (
                pokemon_data["description"][:50] + "..."
                if len(pokemon_data["description"]) > 50
                else pokemon_data["description"]
            )
            desc_label = tk.Label(
                card_frame,
                text=desc,
                font=self.tiny_font,
                fg=COLORS["text_secondary"],
                bg=COLORS["bg_card"],
                wraplength=140,
            )
            desc_label.pack(pady=5)

            # Select Button
            select_btn = self.create_styled_button(
                card_frame,
                "✨ Wählen",
                lambda name=starter_name: self.select_starter(name),
                width=15,
            )
            select_btn.pack(pady=15)

    def select_starter(self, starter_name):
        """Wählt Starter-Pokemon und startet das Hauptspiel"""
        starter = Pokemon(starter_name, 5)  # Level 5 Starter
        self.player.add_pokemon(starter)

        messagebox.showinfo(
            "Pokemon gewählt!",
            f"🎉 Du hast {starter_name} gewählt!\n🗺️ Du kannst dich jetzt frei bewegen!\n\n"
            f"🎮 Steuerung:\n• WASD oder Pfeiltasten zum Laufen\n• Laufe durch Gras für Pokemon\n• Besuche Gebäude für Services",
        )

        self.show_overworld()

    def show_overworld(self):
        """Zeigt die Overworld-Map"""
        self.clear_screen()
        self.current_screen = "overworld"

        # Header mit Spieler-Info (kompakter)
        header_frame = tk.Frame(
            self.main_frame, bg=COLORS["bg_card"], relief="solid", bd=2
        )
        header_frame.pack(fill="x", pady=(0, 15))

        # Info in einer Zeile
        player_info_text = f"👤 {self.player.name} | 🏆 Siege: {self.player.battles_won} | 🥎 Pokebälle: {self.player.get_total_pokeballs()} | 💰 Geld: {self.player.money}₽ | 👥 Team: {len(self.player.pokemon_team)}/6"
        player_info = tk.Label(
            header_frame,
            text=player_info_text,
            font=self.text_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_card"],
        )
        player_info.pack(pady=10)

        # Hauptcontainer für Map und Menü
        content_frame = tk.Frame(self.main_frame, bg=COLORS["bg_main"])
        content_frame.pack(fill="both", expand=True)

        # Map Frame (links)
        map_frame = tk.Frame(content_frame, bg=COLORS["bg_main"])
        map_frame.pack(side="left", padx=(0, 15))

        # Map Title
        map_title = tk.Label(
            map_frame,
            text="🗺️ Kanto Region",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_main"],
        )
        map_title.pack(pady=(0, 10))

        # Game Map erstellen
        self.game_map = GameMap(
            map_frame, GAME_CONFIG["map_width"], GAME_CONFIG["map_height"]
        )
        self.game_map.canvas.pack()

        # Map-Callbacks setzen
        self.game_map.encounter_callback = self.handle_pokemon_encounter
        self.game_map.special_location_callback = self.handle_special_location

        # Controls Info
        controls_text = "🎮 Steuerung: WASD oder ↑↓←→"
        controls_label = tk.Label(
            map_frame,
            text=controls_text,
            font=self.small_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_main"],
        )
        controls_label.pack(pady=10)

        # Rechtes Menü
        menu_frame = tk.Frame(
            content_frame, bg=COLORS["bg_card"], relief="solid", bd=2, width=250
        )
        menu_frame.pack(side="right", fill="y", padx=(0, 0))
        menu_frame.pack_propagate(False)

        # Menu Title
        menu_title = tk.Label(
            menu_frame,
            text="📱 Trainer-Menü",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        )
        menu_title.pack(pady=15)

        # Menu Buttons (kompakter)
        buttons = [
            ("👥 Pokemon-Team", self.show_team),
            ("🎒 Inventar & Items", self.show_inventory_manager),
            ("📊 Statistiken", self.show_stats),
            ("💾 Spiel speichern", self.save_game),
            ("❌ Spiel beenden", self.quit_game),
        ]

        for text, command in buttons:
            btn = self.create_styled_button(
                menu_frame, text, command, COLORS["info"], width=18
            )
            btn.pack(pady=8, padx=15)

        # Legende
        legend_frame = tk.Frame(menu_frame, bg=COLORS["bg_card"])
        legend_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        tk.Label(
            legend_frame,
            text="🗺️ Legende:",
            font=self.small_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        ).pack()

        legend_text = (
            "🏥 Pokemon Center\n🛒 Pokemarkt\n🌿 Gras (Pokemon)\n🟫 Weg (sicher)"
        )
        tk.Label(
            legend_frame,
            text=legend_text,
            font=self.tiny_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
            justify="left",
        ).pack()

    def handle_pokemon_encounter(self):
        """Behandelt Pokemon-Begegnungen auf der Map"""
        if not self.player.has_usable_pokemon():
            messagebox.showwarning(
                "Warnung",
                "🏥 Du hast keine kampffähigen Pokemon!\nBesuche das Pokemon-Center!",
            )
            return

        # Level der wilden Pokemon basiert auf Fortschritt
        min_level = max(1, self.player.battles_won // 3)
        max_level = max(3, self.player.battles_won // 2 + 4)
        wild_pokemon = create_wild_pokemon(min_level, max_level)

        # Kurze Benachrichtigung
        response = messagebox.askyesno(
            "Wild Pokemon!",
            f"🐾 Ein wildes {wild_pokemon.name} (Lv.{wild_pokemon.level}) erscheint!\n\n"
            f"🗯️ Möchtest du kämpfen?",
        )
        if response:
            self.start_battle(wild_pokemon)

    def handle_special_location(self, location):
        """Behandelt spezielle Orte"""
        if location["type"] == "pokemon_center":
            response = messagebox.askyesno(
                "Pokemon Center",
                "🏥 Willkommen im Pokemon Center!\n\n"
                "💚 Möchtest du deine Pokemon heilen lassen?",
            )
            if response:
                self.visit_pokemon_center()
        elif location["type"] == "shop":
            self.show_shop()

    def show_inventory_manager(self):
        """Zeigt Inventar-Manager zum Verwenden von Items"""
        inv_window = tk.Toplevel(self.root)
        inv_window.title("🎒 Inventar & Items")
        inv_window.geometry("700x500")
        inv_window.configure(bg=COLORS["bg_main"])

        # Header
        header_frame = tk.Frame(inv_window, bg=COLORS["bg_card"], relief="solid", bd=2)
        header_frame.pack(fill="x", pady=(0, 15))

        header = tk.Label(
            header_frame,
            text="🎒 Dein Inventar",
            font=self.title_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        )
        header.pack(pady=15)

        # Schnell-Heilung Button
        quick_heal_btn = self.create_styled_button(
            header_frame,
            "🏥 Alle Pokemon heilen",
            lambda: self.quick_heal_and_refresh(inv_window),
            COLORS["success"],
            20,
        )
        quick_heal_btn.pack(pady=(0, 15))

        # Inventar-Inhalt
        content_frame = tk.Frame(inv_window, bg=COLORS["bg_main"])
        content_frame.pack(fill="both", expand=True, padx=15)

        from game_data import SHOP_ITEMS

        # Heilung Items
        healing_frame = tk.LabelFrame(
            content_frame,
            text="💊 Heilungs-Items",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
        )
        healing_frame.pack(fill="x", pady=10)

        healing_items = ["trank", "supertrank", "hypertrank", "beleber", "vitalkraut"]
        for item_id in healing_items:
            amount = self.player.inventory.get(item_id, 0)
            if amount > 0:
                item = SHOP_ITEMS[item_id]
                self.create_inventory_item(
                    healing_frame, item_id, item, amount, inv_window
                )

        # Pokebälle
        balls_frame = tk.LabelFrame(
            content_frame,
            text="🥎 Pokebälle",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
        )
        balls_frame.pack(fill="x", pady=10)

        balls_text = f"🥎 Pokeball: {self.player.inventory.get('pokeball', 0)}\n"
        balls_text += f"🟦 Superball: {self.player.inventory.get('superball', 0)}\n"
        balls_text += f"🟨 Hyperball: {self.player.inventory.get('hyperball', 0)}\n"
        balls_text += f"💫 Gesamt: {self.player.get_total_pokeballs()}"

        tk.Label(
            balls_frame,
            text=balls_text,
            font=self.text_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_card"],
            justify="left",
        ).pack(padx=15, pady=10)

    def create_inventory_item(self, parent, item_id, item, amount, window):
        """Erstellt ein Inventar-Item zum Verwenden"""
        item_frame = tk.Frame(parent, bg=COLORS["bg_secondary"], relief="solid", bd=1)
        item_frame.pack(fill="x", padx=10, pady=5)

        # Item Info
        info_frame = tk.Frame(item_frame, bg=COLORS["bg_secondary"])
        info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        tk.Label(
            info_frame,
            text=f"{item['icon']} {item['name']} (x{amount})",
            font=self.text_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_secondary"],
        ).pack(anchor="w")

        tk.Label(
            info_frame,
            text=item["description"],
            font=self.small_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_secondary"],
            wraplength=300,
        ).pack(anchor="w")

        # Verwenden Button
        if item["category"] == "healing":
            use_btn = self.create_styled_button(
                item_frame,
                "Verwenden",
                lambda: self.use_item_on_pokemon(item_id, window),
                COLORS["success"],
                10,
            )
            use_btn.pack(side="right", padx=10, pady=5)

    def use_item_on_pokemon(self, item_id, window):
        """Verwendet Item auf ausgewähltes Pokemon"""
        if not self.player.pokemon_team:
            messagebox.showwarning("Warnung", "Du hast keine Pokemon!")
            return

        # Pokemon-Auswahl Fenster
        select_window = tk.Toplevel(window)
        select_window.title("Pokemon auswählen")
        select_window.geometry("400x300")
        select_window.configure(bg=COLORS["bg_main"])

        tk.Label(
            select_window,
            text="Auf welches Pokemon verwenden?",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_main"],
        ).pack(pady=20)

        for pokemon in self.player.pokemon_team:
            # Status prüfen für Item-Eignung
            from game_data import SHOP_ITEMS

            item = SHOP_ITEMS[item_id]

            can_use = True
            status_text = ""

            if item_id == "beleber" and pokemon.is_alive():
                can_use = False
                status_text = " (nicht besiegt)"
            elif (
                item_id in ["trank", "supertrank", "hypertrank"]
                and pokemon.current_hp >= pokemon.max_hp
            ):
                can_use = False
                status_text = " (volle HP)"

            pokemon_text = f"{pokemon.name} (Lv.{pokemon.level}) - {pokemon.current_hp}/{pokemon.max_hp} HP{status_text}"

            if can_use:
                btn = self.create_styled_button(
                    select_window,
                    pokemon_text,
                    lambda p=pokemon: self.execute_item_use(
                        item_id, p, select_window, window
                    ),
                    COLORS["info"],
                    30,
                )
            else:
                btn = tk.Label(
                    select_window,
                    text=pokemon_text,
                    font=self.small_font,
                    fg=COLORS["text_secondary"],
                    bg=COLORS["bg_main"],
                )

            btn.pack(pady=3, padx=20)

    def execute_item_use(self, item_id, pokemon, select_window, main_window):
        """Führt Item-Verwendung aus"""
        success, message = self.player.use_item(item_id, pokemon)

        select_window.destroy()

        if success:
            messagebox.showinfo("✅ Item verwendet!", message)
            # Inventar-Fenster refreshen
            main_window.destroy()
            self.show_inventory_manager()
        else:
            messagebox.showerror("❌ Fehler", message)

    def quick_heal(self):
        """Schnelle Heilung"""
        self.player.heal_all_pokemon()
        messagebox.showinfo("Geheilt!", "✨ Alle Pokemon wurden geheilt!")

    def quick_heal_and_refresh(self, window):
        """Schnelle Heilung mit Fenster-Refresh"""
        self.quick_heal()
        window.destroy()
        self.show_inventory_manager()

    def save_game(self):
        """Speichert das Spiel (Placeholder)"""
        messagebox.showinfo(
            "Speichern",
            "💾 Speicherfunktion kommt bald!\n\nDein Fortschritt wird automatisch\nim Hintergrund gespeichert.",
        )

    def start_battle(self, wild_pokemon):
        """Startet einen Kampf gegen ein wildes Pokemon"""
        self.current_battle = Battle(self.player, wild_pokemon)
        self.show_battle_screen(wild_pokemon)

    def show_battle_screen(self, wild_pokemon):
        """Zeigt den kompakteren Kampfbildschirm"""
        self.clear_screen()
        self.current_screen = "battle"

        # Battle Header (kompakter)
        header_frame = tk.Frame(
            self.main_frame, bg=COLORS["bg_card"], relief="solid", bd=2
        )
        header_frame.pack(fill="x", pady=(0, 15))

        header = tk.Label(
            header_frame,
            text="⚔️ POKEMON KAMPF",
            font=self.header_font,
            fg=COLORS["accent"],
            bg=COLORS["bg_card"],
        )
        header.pack(pady=10)

        # Hauptcontainer für bessere Aufteilung
        battle_container = tk.Frame(self.main_frame, bg=COLORS["bg_main"])
        battle_container.pack(fill="both", expand=True)

        # Pokemon Display Frame (kompakter, horizontal)
        pokemon_frame = tk.Frame(battle_container, bg=COLORS["bg_main"])
        pokemon_frame.pack(pady=15)

        # Wild Pokemon (left) - kleinere Karten
        wild_frame = tk.Frame(
            pokemon_frame,
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
            width=250,
            height=300,
        )
        wild_frame.grid(row=0, column=0, padx=20)
        wild_frame.pack_propagate(False)

        self.display_battle_pokemon_card(wild_frame, wild_pokemon, "🐾 Wildes Pokemon")

        # VS Label (kompakter)
        vs_frame = tk.Frame(pokemon_frame, bg=COLORS["accent"], relief="solid", bd=2)
        vs_frame.grid(row=0, column=1, padx=15)

        vs_label = tk.Label(
            vs_frame,
            text="VS",
            font=self.header_font,
            fg=COLORS["text_primary"],
            bg=COLORS["accent"],
        )
        vs_label.pack(padx=15, pady=20)

        # Player Pokemon (right) - kleinere Karten
        player_frame = tk.Frame(
            pokemon_frame,
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
            width=250,
            height=300,
        )
        player_frame.grid(row=0, column=2, padx=20)
        player_frame.pack_propagate(False)

        current_pokemon = self.player.get_first_alive_pokemon()
        self.display_battle_pokemon_card(
            player_frame, current_pokemon, "👤 Dein Pokemon"
        )

        # Battle Actions (kompakter)
        action_frame = tk.Frame(
            battle_container, bg=COLORS["bg_card"], relief="solid", bd=2
        )
        action_frame.pack(pady=20, fill="x", padx=100)

        tk.Label(
            action_frame,
            text="🎯 Wähle deine Aktion:",
            font=self.text_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        ).pack(pady=10)

        # Action Buttons in 2x2 Grid (kompakter)
        button_frame = tk.Frame(action_frame, bg=COLORS["bg_card"])
        button_frame.pack(pady=10)

        actions = [
            (
                "⚔️ Angreifen",
                lambda: self.battle_action("attack", wild_pokemon, current_pokemon),
                COLORS["danger"],
            ),
            (
                "🥎 Pokemon fangen",
                lambda: self.battle_action("catch", wild_pokemon, current_pokemon),
                COLORS["success"],
            ),
            (
                "🔄 Pokemon wechseln",
                lambda: self.show_pokemon_switch(wild_pokemon),
                COLORS["info"],
            ),
            (
                "💨 Fliehen",
                lambda: self.battle_action("run", wild_pokemon, current_pokemon),
                COLORS["warning"],
            ),
        ]

        for i, (text, command, color) in enumerate(actions):
            btn = self.create_styled_button(button_frame, text, command, color, 15)
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=5)

        # Zurück-Button
        back_btn = self.create_styled_button(
            action_frame,
            "🏠 Zurück zur Map",
            self.show_overworld,
            COLORS["bg_secondary"],
            20,
        )
        back_btn.pack(pady=10)

    def display_battle_pokemon_card(self, parent, pokemon, title):
        """Zeigt eine Pokemon-Karte im Kampfbildschirm mit neuen Sprites"""
        # Title
        title_label = tk.Label(
            parent,
            text=title,
            font=self.small_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        )
        title_label.pack(pady=5)

        # Pokemon "Sprite" mit neuer Grafik-Engine
        canvas = tk.Canvas(
            parent, width=140, height=140, bg=COLORS["bg_card"], highlightthickness=0
        )
        canvas.pack(pady=5)

        # Neues Pokemon-Sprite zeichnen
        PokemonSprite.draw_pokemon(canvas, pokemon.name, 70, 70, 100)

        # Pokemon Info (kompakt)
        name_text = f"{pokemon.name}\n(Lv.{pokemon.level})"
        tk.Label(
            parent,
            text=name_text,
            font=self.small_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_card"],
        ).pack(pady=2)

        # Type
        tk.Label(
            parent,
            text=f"Typ: {pokemon.typ}",
            font=self.tiny_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
        ).pack()

        # HP Info
        hp_percent = pokemon.get_hp_percentage()
        hp_color = (
            COLORS["hp_high"]
            if hp_percent > 60
            else COLORS["hp_medium"] if hp_percent > 30 else COLORS["hp_low"]
        )

        hp_text = f"❤️ {pokemon.current_hp}/{pokemon.max_hp}"
        tk.Label(
            parent,
            text=hp_text,
            font=self.small_font,
            fg=hp_color,
            bg=COLORS["bg_card"],
        ).pack(pady=2)

        # HP Bar (kompakt)
        hp_bar_frame = tk.Frame(parent, bg="black", height=4, relief="sunken", bd=1)
        hp_bar_frame.pack(fill="x", padx=10, pady=2)

        hp_fill = tk.Frame(hp_bar_frame, bg=hp_color, height=2)
        hp_fill.place(relwidth=hp_percent / 100, relheight=1)

        # Stats (kompakt)
        stats_text = f"⚔️{pokemon.attack} 🛡️{pokemon.defense}"
        tk.Label(
            parent,
            text=stats_text,
            font=self.tiny_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
        ).pack(pady=2)

    def show_shop(self):
        """Zeigt den vollständigen Pokemarkt"""
        shop_window = tk.Toplevel(self.root)
        shop_window.title("🛒 Pokemarkt")
        shop_window.geometry("800x600")
        shop_window.configure(bg=COLORS["bg_main"])
        shop_window.resizable(True, True)

        # Header
        header_frame = tk.Frame(shop_window, bg=COLORS["bg_card"], relief="solid", bd=2)
        header_frame.pack(fill="x", pady=(0, 15))

        header = tk.Label(
            header_frame,
            text="🛒 Willkommen im Pokemarkt!",
            font=self.title_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        )
        header.pack(pady=15)

        # Geld-Anzeige
        money_label = tk.Label(
            header_frame,
            text=f"💰 Dein Geld: {self.player.money}₽",
            font=self.header_font,
            fg=COLORS["success"],
            bg=COLORS["bg_card"],
        )
        money_label.pack(pady=(0, 15))

        # Hauptcontainer mit Scroll
        main_container = tk.Frame(shop_window, bg=COLORS["bg_main"])
        main_container.pack(fill="both", expand=True, padx=15)

        # Canvas für Scrolling
        canvas = tk.Canvas(main_container, bg=COLORS["bg_main"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            main_container, orient="vertical", command=canvas.yview
        )
        scrollable_frame = tk.Frame(canvas, bg=COLORS["bg_main"])

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Shop-Kategorien
        from game_data import SHOP_ITEMS

        # Pokebälle Kategorie
        balls_frame = tk.LabelFrame(
            scrollable_frame,
            text="🥎 Pokebälle",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
        )
        balls_frame.pack(fill="x", padx=10, pady=10)

        balls = {k: v for k, v in SHOP_ITEMS.items() if v["category"] == "balls"}
        for item_id, item in balls.items():
            self.create_shop_item(balls_frame, item_id, item, shop_window)

        # Heilung Kategorie
        healing_frame = tk.LabelFrame(
            scrollable_frame,
            text="💊 Heilung & Items",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
        )
        healing_frame.pack(fill="x", padx=10, pady=10)

        healing = {k: v for k, v in SHOP_ITEMS.items() if v["category"] == "healing"}
        for item_id, item in healing.items():
            self.create_shop_item(healing_frame, item_id, item, shop_window)

        # Inventar-Anzeige
        inventory_frame = tk.LabelFrame(
            scrollable_frame,
            text="🎒 Dein Inventar",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
            relief="solid",
            bd=2,
        )
        inventory_frame.pack(fill="x", padx=10, pady=10)

        self.show_inventory_summary(inventory_frame)

        # Pack canvas und scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Schließen-Button
        close_frame = tk.Frame(shop_window, bg=COLORS["bg_main"])
        close_frame.pack(fill="x", pady=10)

        close_btn = self.create_styled_button(
            close_frame, "❌ Shop verlassen", shop_window.destroy, COLORS["danger"], 20
        )
        close_btn.pack()

    def create_shop_item(self, parent, item_id, item, shop_window):
        """Erstellt ein Shop-Item Widget"""
        item_frame = tk.Frame(parent, bg=COLORS["bg_secondary"], relief="solid", bd=1)
        item_frame.pack(fill="x", padx=10, pady=5)

        # Item-Info (links)
        info_frame = tk.Frame(item_frame, bg=COLORS["bg_secondary"])
        info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        # Icon und Name
        title_frame = tk.Frame(info_frame, bg=COLORS["bg_secondary"])
        title_frame.pack(fill="x")

        tk.Label(
            title_frame,
            text=f"{item['icon']} {item['name']}",
            font=self.text_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_secondary"],
        ).pack(side="left")

        tk.Label(
            title_frame,
            text=f"{item['price']}₽",
            font=self.text_font,
            fg=COLORS["success"],
            bg=COLORS["bg_secondary"],
        ).pack(side="right")

        # Beschreibung
        tk.Label(
            info_frame,
            text=item["description"],
            font=self.small_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_secondary"],
            wraplength=400,
        ).pack(anchor="w")

        # Aktueller Bestand
        current_amount = self.player.inventory.get(item_id, 0)
        tk.Label(
            info_frame,
            text=f"Im Besitz: {current_amount}",
            font=self.tiny_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_secondary"],
        ).pack(anchor="w")

        # Kauf-Buttons (rechts)
        buy_frame = tk.Frame(item_frame, bg=COLORS["bg_secondary"])
        buy_frame.pack(side="right", padx=10, pady=5)

        # Kauf 1x
        buy1_btn = self.create_styled_button(
            buy_frame,
            "Kaufe 1x",
            lambda: self.buy_item_action(item_id, 1, shop_window),
            COLORS["info"],
            8,
        )
        buy1_btn.pack(pady=2)

        # Kauf 5x (wenn genug Geld)
        if self.player.money >= item["price"] * 5:
            buy5_btn = self.create_styled_button(
                buy_frame,
                "Kaufe 5x",
                lambda: self.buy_item_action(item_id, 5, shop_window),
                COLORS["success"],
                8,
            )
            buy5_btn.pack(pady=2)

    def buy_item_action(self, item_id, quantity, shop_window):
        """Führt Kauf-Aktion aus"""
        success, message = self.player.buy_item(item_id, quantity)

        if success:
            messagebox.showinfo("✅ Kauf erfolgreich!", message)
            # Shop-Fenster neu laden
            shop_window.destroy()
            self.show_shop()
        else:
            messagebox.showerror("❌ Kauf fehlgeschlagen", message)

    def show_inventory_summary(self, parent):
        """Zeigt Inventar-Zusammenfassung"""
        summary_frame = tk.Frame(parent, bg=COLORS["bg_card"])
        summary_frame.pack(fill="x", padx=10, pady=5)

        from game_data import SHOP_ITEMS

        # Inventar in Spalten anzeigen
        row = 0
        col = 0
        for item_id, amount in self.player.inventory.items():
            if amount > 0 and item_id in SHOP_ITEMS:
                item = SHOP_ITEMS[item_id]
                item_text = f"{item['icon']} {item['name']}: {amount}"

                item_label = tk.Label(
                    summary_frame,
                    text=item_text,
                    font=self.small_font,
                    fg=COLORS["text_primary"],
                    bg=COLORS["bg_card"],
                )
                item_label.grid(row=row, column=col, sticky="w", padx=5, pady=2)

                col += 1
                if col >= 3:  # 3 Spalten
                    col = 0
                    row += 1

    def battle_action(self, action, wild_pokemon, player_pokemon):
        """Führt eine Kampfaktion aus"""
        result = self.current_battle.execute_turn(action, player_pokemon, wild_pokemon)

        # Verbessertes Ergebnis-Display
        if result["battle_over"]:
            if result["winner"] == "player":
                money_earned = GAME_CONFIG["money_per_battle"]
                self.player.win_battle(money_reward=money_earned)
                messagebox.showinfo(
                    "🎉 Sieg!",
                    f"✨ Du hast gewonnen!\n💰 +{money_earned}₽ erhalten!\n\n{result['message']}",
                )
            elif result["winner"] == "opponent":
                messagebox.showwarning(
                    "💀 Niederlage", f"😵 Du hast verloren...\n\n{result['message']}"
                )
            elif result["winner"] == "run":
                messagebox.showinfo(
                    "💨 Geflohen",
                    f"🏃 Du bist erfolgreich geflohen!\n\n{result['message']}",
                )

            self.show_overworld()
        else:
            # Battle continues - zeige Ergebnis und refresh
            messagebox.showinfo("⚡ Kampf", result["message"])
            self.show_battle_screen(wild_pokemon)

    def show_pokemon_switch(self, wild_pokemon):
        """Zeigt verbessertes Pokemon-Wechsel Interface"""
        alive_pokemon = self.player.get_alive_pokemon()
        if len(alive_pokemon) <= 1:
            messagebox.showinfo("ℹ️ Info", "Du hast nur ein kampffähiges Pokemon!")
            return

        # Pokemon selection window
        switch_window = tk.Toplevel(self.root)
        switch_window.title("Pokemon wechseln")
        switch_window.geometry("500x400")
        switch_window.configure(bg=COLORS["bg_main"])

        tk.Label(
            switch_window,
            text="🔄 Wähle ein Pokemon:",
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_main"],
        ).pack(pady=20)

        for i, pokemon in enumerate(alive_pokemon):
            btn_frame = tk.Frame(
                switch_window, bg=COLORS["bg_card"], relief="solid", bd=1
            )
            btn_frame.pack(pady=5, padx=20, fill="x")

            # HP Prozent für Farbe
            hp_percent = pokemon.get_hp_percentage()
            hp_color = (
                COLORS["hp_high"]
                if hp_percent > 60
                else COLORS["hp_medium"] if hp_percent > 30 else COLORS["hp_low"]
            )

            btn_text = f"⭐ {pokemon.name} (Lv.{pokemon.level}) - ❤️ {pokemon.current_hp}/{pokemon.max_hp} HP"
            btn = tk.Button(
                btn_frame,
                text=btn_text,
                font=self.text_font,
                bg=hp_color,
                fg=COLORS["text_primary"],
                command=lambda p=pokemon: self.switch_pokemon(
                    p, wild_pokemon, switch_window
                ),
            )
            btn.pack(pady=8, padx=10, fill="x")

    def switch_pokemon(self, new_pokemon, wild_pokemon, window):
        """Wechselt das aktuelle Pokemon"""
        window.destroy()
        messagebox.showinfo(
            "🔄 Pokemon gewechselt", f"✨ {new_pokemon.name} ist jetzt aktiv!"
        )
        self.show_battle_screen(wild_pokemon)

    def show_team(self):
        """Zeigt das verbesserte Pokemon-Team"""
        team_window = tk.Toplevel(self.root)
        team_window.title(f"{self.player.name}s Pokemon-Team")
        team_window.geometry("900x700")
        team_window.configure(bg=COLORS["bg_main"])

        # Header
        header_frame = tk.Frame(team_window, bg=COLORS["bg_card"], relief="solid", bd=2)
        header_frame.pack(fill="x", pady=(0, 20))

        header = tk.Label(
            header_frame,
            text=f"👥 {self.player.name}s Team",
            font=self.title_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        )
        header.pack(pady=15)

        # Team info
        team_info = tk.Label(
            header_frame,
            text=f"📊 Team-Größe: {len(self.player.pokemon_team)}/{GAME_CONFIG['max_team_size']} | 🥎 Pokebälle: {self.player.get_total_pokeballs()}",
            font=self.text_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_card"],
        )
        team_info.pack(pady=(0, 15))

        # Pokemon Grid
        pokemon_frame = tk.Frame(team_window, bg=COLORS["bg_main"])
        pokemon_frame.pack(pady=20, fill="both", expand=True, padx=20)

        if not self.player.pokemon_team:
            empty_label = tk.Label(
                pokemon_frame,
                text="😔 Dein Team ist leer!\n\nGehe raus und fange Pokemon!",
                font=self.header_font,
                fg=COLORS["text_secondary"],
                bg=COLORS["bg_main"],
            )
            empty_label.pack(pady=100)
        else:
            for i, pokemon in enumerate(self.player.pokemon_team):
                self.display_team_pokemon(pokemon_frame, pokemon, i)

    def display_team_pokemon(self, parent, pokemon, index):
        """Zeigt ein verbessertes Pokemon im Team an"""
        # Pokemon Frame
        poke_frame = tk.Frame(parent, bg=COLORS["bg_card"], relief="solid", bd=2)
        poke_frame.pack(fill="x", pady=8)

        # Main content frame
        content_frame = tk.Frame(poke_frame, bg=COLORS["bg_card"])
        content_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # Left side - Pokemon sprite and basic info
        left_frame = tk.Frame(content_frame, bg=COLORS["bg_card"])
        left_frame.pack(side="left")

        # Pokemon sprite mit neuer Grafik-Engine
        canvas = tk.Canvas(
            left_frame, width=80, height=80, bg=COLORS["bg_card"], highlightthickness=0
        )
        canvas.pack(side="left", padx=(0, 15))

        # Neues Pokemon-Sprite zeichnen
        PokemonSprite.draw_pokemon(canvas, pokemon.name, 40, 40, 60)

        # Right side - Pokemon details
        details_frame = tk.Frame(content_frame, bg=COLORS["bg_card"])
        details_frame.pack(side="left", fill="both", expand=True)

        # Name and status
        status_emoji = "💚" if pokemon.is_alive() else "💀"
        name_text = f"{status_emoji} {pokemon.name} (Lv.{pokemon.level})"
        tk.Label(
            details_frame,
            text=name_text,
            font=self.header_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        ).pack(anchor="w")

        # Type
        tk.Label(
            details_frame,
            text=f"🏷️ Typ: {pokemon.typ}",
            font=self.text_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_card"],
        ).pack(anchor="w")

        # HP with colored bar
        hp_frame = tk.Frame(details_frame, bg=COLORS["bg_card"])
        hp_frame.pack(anchor="w", fill="x", pady=5)

        hp_percent = pokemon.get_hp_percentage()
        ring_color = (
            COLORS["hp_high"]
            if hp_percent > 60
            else COLORS["hp_medium"] if hp_percent > 30 else COLORS["hp_low"]
        )

        tk.Label(
            hp_frame,
            text=f"❤️ HP: {pokemon.current_hp}/{pokemon.max_hp} ({hp_percent:.0f}%)",
            font=self.text_font,
            fg=COLORS["text_primary"],
            bg=COLORS["bg_card"],
        ).pack(anchor="w")

        # HP Bar
        hp_bar_frame = tk.Frame(hp_frame, bg="black", height=6, relief="sunken", bd=1)
        hp_bar_frame.pack(anchor="w", fill="x", pady=2)

        hp_fill = tk.Frame(hp_bar_frame, bg=ring_color, height=4)
        hp_fill.place(relwidth=hp_percent / 100, relheight=1)

        # Stats
        tk.Label(
            details_frame,
            text=f"⚔️ ATK: {pokemon.attack} | 🛡️ DEF: {pokemon.defense}",
            font=self.small_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
        ).pack(anchor="w")

        # EXP Bar
        exp_frame = tk.Frame(details_frame, bg=COLORS["bg_card"])
        exp_frame.pack(anchor="w", fill="x", pady=5)

        exp_percent = pokemon.get_exp_percentage()
        tk.Label(
            exp_frame,
            text=f"⭐ EXP: {pokemon.exp}/{pokemon.exp_to_next_level} ({exp_percent:.0f}%)",
            font=self.small_font,
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
        ).pack(anchor="w")

        exp_bar_frame = tk.Frame(exp_frame, bg="black", height=4, relief="sunken", bd=1)
        exp_bar_frame.pack(anchor="w", fill="x")

        exp_fill = tk.Frame(exp_bar_frame, bg=COLORS["exp_bar"], height=2)
        exp_fill.place(relwidth=exp_percent / 100, relheight=1)

    def visit_pokemon_center(self):
        """Besucht das Pokemon-Center"""
        self.player.heal_all_pokemon()
        self.player.add_pokeballs(GAME_CONFIG["pokeball_refill"])

        messagebox.showinfo(
            "🏥 Pokemon-Center",
            f"💫 Willkommen im Pokemon-Center!\n\n"
            f"✨ Alle deine Pokemon wurden vollständig geheilt!\n"
            f"🥎 Du hast {GAME_CONFIG['pokeball_refill']} Pokebälle erhalten!\n\n"
            f"🎒 Pokebälle gesamt: {self.player.get_total_pokeballs()}",
        )

    def show_stats(self):
        """Zeigt verbesserte Spielerstatistiken"""
        stats = self.player.get_stats()

        stats_window = tk.Toplevel(self.root)
        stats_window.title("Trainer-Statistiken")
        stats_window.geometry("500x450")
        stats_window.configure(bg=COLORS["bg_main"])

        # Header
        header_frame = tk.Frame(
            stats_window, bg=COLORS["bg_card"], relief="solid", bd=2
        )
        header_frame.pack(fill="x", pady=(0, 20))

        header = tk.Label(
            header_frame,
            text="📊 Deine Statistiken",
            font=self.title_font,
            fg=COLORS["text_accent"],
            bg=COLORS["bg_card"],
        )
        header.pack(pady=20)

        # Stats Cards
        stats_frame = tk.Frame(stats_window, bg=COLORS["bg_main"])
        stats_frame.pack(padx=30, pady=10, fill="both", expand=True)

        # Trainer Info Card
        trainer_card = self.create_info_card(
            stats_frame,
            f"👤 Trainer: {stats['name']}",
            f"🏆 Kämpfe gewonnen: {stats['battles_won']}\n"
            f"🎯 Pokemon gefangen: {stats['pokemon_caught']}\n"
            f"💰 Geld: {stats['money']} ₽",
        )
        trainer_card.pack(fill="x", pady=10)

        # Team Info Card
        team_card = self.create_info_card(
            stats_frame,
            f"👥 Team-Info",
            f"📊 Team-Größe: {stats['team_size']}/{GAME_CONFIG['max_team_size']}\n"
            f"🥎 Pokebälle: {stats['pokeballs']}\n"
            f"⭐ Durchschnitts-Level: {stats['team_average_level']}\n"
            f"🏆 Stärkstes Pokemon: {stats['strongest_pokemon']}",
        )
        team_card.pack(fill="x", pady=10)

    def quit_game(self):
        """Beendet das Spiel"""
        if messagebox.askyesno(
            "🚪 Spiel beenden",
            "Möchtest du das Spiel wirklich beenden?\n\n"
            "💾 Dein Fortschritt wird nicht gespeichert!",
        ):
            self.root.quit()

    def run(self):
        """Startet die GUI"""
        self.root.mainloop()


if __name__ == "__main__":
    game = PokemonGUI()
    game.run()