# game_data.py
"""
Pokemon-Spiel Datenbank und Konfiguration
"""

# Pokemon-Datenbank mit erweiterten Informationen
POKEMON_DATA = {
    "Glumanda": {
        "typ": "Feuer",
        "hp": 25,
        "attack": 12,
        "defense": 8,
        "color": "#FF4444",
        "description": "Ein kleines Echsen-Pokemon mit einer Flamme am Schwanz.",
    },
    "Schiggy": {
        "typ": "Wasser",
        "hp": 30,
        "attack": 10,
        "defense": 12,
        "color": "#4488FF",
        "description": "Ein Schildkröten-Pokemon das Wasserstrahlen schießen kann.",
    },
    "Bisasam": {
        "typ": "Pflanze",
        "hp": 28,
        "attack": 11,
        "defense": 10,
        "color": "#44FF44",
        "description": "Ein Reptil-Pokemon mit einer Zwiebel auf dem Rücken.",
    },
    "Pikachu": {
        "typ": "Elektro",
        "hp": 22,
        "attack": 14,
        "defense": 6,
        "color": "#FFDD00",
        "description": "Ein Elektro-Maus Pokemon mit roten Wangen.",
    },
    "Rattfratz": {
        "typ": "Normal",
        "hp": 18,
        "attack": 9,
        "defense": 7,
        "color": "#AA8866",
        "description": "Ein kleines Ratten-Pokemon mit scharfen Zähnen.",
    },
    "Taubsi": {
        "typ": "Normal/Flug",
        "hp": 20,
        "attack": 8,
        "defense": 8,
        "color": "#DDAA77",
        "description": "Ein kleines Vogel-Pokemon das gerne fliegt.",
    },
    "Raupy": {
        "typ": "Käfer",
        "hp": 15,
        "attack": 6,
        "defense": 9,
        "color": "#88DD88",
        "description": "Ein Raupen-Pokemon das sich später entwickelt.",
    },
    "Hornliu": {
        "typ": "Käfer/Gift",
        "hp": 17,
        "attack": 10,
        "defense": 8,
        "color": "#AA44AA",
        "description": "Ein Käfer-Pokemon mit giftigen Stacheln.",
    },
    "Zubat": {
        "typ": "Gift/Flug",
        "hp": 19,
        "attack": 9,
        "defense": 7,
        "color": "#8844BB",
        "description": "Ein Fledermaus-Pokemon ohne Augen.",
    },
    "Digda": {
        "typ": "Boden",
        "hp": 16,
        "attack": 12,
        "defense": 5,
        "color": "#CC8844",
        "description": "Ein Maulwurf-Pokemon das unter der Erde lebt.",
    },
    "Abra": {
        "typ": "Psycho",
        "hp": 14,
        "attack": 7,
        "defense": 6,
        "color": "#FFCC44",
        "description": "Ein psychisches Pokemon das teleportieren kann.",
    },
    "Machollo": {
        "typ": "Kampf",
        "hp": 24,
        "attack": 15,
        "defense": 11,
        "color": "#CC4444",
        "description": "Ein muskulöses Pokemon das gerne kämpft.",
    },
}

# Typ-Effektivität (vereinfacht)
TYPE_EFFECTIVENESS = {
    "Feuer": {"Pflanze": 2.0, "Wasser": 0.5, "Käfer": 2.0},
    "Wasser": {"Feuer": 2.0, "Pflanze": 0.5, "Boden": 2.0},
    "Pflanze": {"Wasser": 2.0, "Feuer": 0.5, "Boden": 2.0},
    "Elektro": {"Wasser": 2.0, "Flug": 2.0, "Boden": 0.0},
    "Psycho": {"Kampf": 2.0, "Gift": 2.0},
    "Kampf": {"Normal": 2.0},
    "Gift": {"Pflanze": 2.0},
    "Flug": {"Käfer": 2.0, "Kampf": 2.0},
    "Käfer": {"Psycho": 2.0, "Pflanze": 2.0},
    "Boden": {"Elektro": 2.0, "Feuer": 2.0, "Gift": 2.0},
}

# Starter Pokemon
STARTER_POKEMON = ["Glumanda", "Schiggy", "Bisasam"]

# Spielkonfiguration
GAME_CONFIG = {
    "max_team_size": 6,
    "starting_pokeballs": 5,
    "starting_money": 1000,
    "pokeball_refill": 3,
    "max_pokeballs": 50,
    "max_potions": 20,
    "exp_multiplier": 15,
    "wild_pokemon_encounter_rate": 0.15,  # Pro Schritt im Gras
    "map_tile_size": 32,
    "map_width": 20,
    "map_height": 15,
    "money_per_battle": 50,
}

# Verbesserte GUI Farben für bessere Lesbarkeit
COLORS = {
    "bg_main": "#1a1a2e",  # Dunkelblau
    "bg_secondary": "#16213e",  # Noch dunkler
    "bg_card": "#0f3460",  # Kartenhaintergrund
    "accent": "#e94560",  # Rot-Pink Akzent
    "accent_light": "#ff6b7a",  # Hellerer Akzent
    "text_primary": "#ffffff",  # Weißer Haupttext
    "text_secondary": "#e0e6ed",  # Heller Grautext
    "text_accent": "#ffd700",  # Goldener Akzenttext
    "success": "#00d2d3",  # Türkis für Erfolg
    "warning": "#ff9f43",  # Orange für Warnung
    "danger": "#ff6b7a",  # Rot für Gefahr
    "info": "#54a0ff",  # Blau für Info
    "hp_high": "#00d2d3",  # Hohe HP
    "hp_medium": "#ff9f43",  # Mittlere HP
    "hp_low": "#ff6b7a",  # Niedrige HP
    "exp_bar": "#ffd700",  # EXP Balken
    # Map-Farben
    "grass": "#2d5016",  # Dunkles Gras
    "grass_light": "#4a7c59",  # Helleres Gras
    "path": "#8b7355",  # Weg
    "water": "#1e3a8a",  # Wasser
    "building": "#7c2d12",  # Gebäude
    "player": "#fbbf24",  # Spieler
}

# Map-Tiles Definition
MAP_TILES = {
    "G": {
        "name": "Gras",
        "color": COLORS["grass"],
        "walkable": True,
        "encounter": True,
    },
    "g": {
        "name": "Helles Gras",
        "color": COLORS["grass_light"],
        "walkable": True,
        "encounter": True,
    },
    "P": {"name": "Weg", "color": COLORS["path"], "walkable": True, "encounter": False},
    "W": {
        "name": "Wasser",
        "color": COLORS["water"],
        "walkable": False,
        "encounter": False,
    },
    "B": {
        "name": "Gebäude",
        "color": COLORS["building"],
        "walkable": False,
        "encounter": False,
    },
    "C": {
        "name": "Pokemon Center",
        "color": "#dc2626",
        "walkable": True,
        "encounter": False,
    },
    "S": {"name": "Shop", "color": "#059669", "walkable": True, "encounter": False},
    "T": {"name": "Baum", "color": "#166534", "walkable": False, "encounter": False},
}

# Beispiel-Map (20x15)
WORLD_MAP = [
    "TTTTTTTTTTTTTTTTTTTT",
    "TGGGGGGPPPPGGGGGGggT",
    "TGGGGGGPCPPGGGGGGggT",
    "TGGggggPPPPGGGggGggT",
    "TGGggggPPPPGGGggGggT",
    "TGGggggPPPPGGGggGggT",
    "TGGggggPPPPGGGggGggT",
    "TGGggggPPSPGGGggGggT",
    "TGGggggPPPPGGGggGggT",
    "TGGggggPPPPGGGggGggT",
    "TGGGGGGPPPPGGGGGGggT",
    "TGGGGGGPPPPGGGGGGggT",
    "TGGGGGGPPPPGGGGGGggT",
    "TggggggWWWWggggggggT",
    "TTTTTTTTTTTTTTTTTTTT",
]

# NPCs und spezielle Orte
SPECIAL_LOCATIONS = {
    (8, 2): {"type": "pokemon_center", "name": "Pokemon Center"},
    (8, 7): {"type": "shop", "name": "Pokemarkt"},
}

# Font-Konfiguration für bessere Lesbarkeit
FONT_CONFIG = {
    "title_size": 28,
    "header_size": 18,
    "text_size": 14,
    "small_size": 12,
    "tiny_size": 10,
    "family": "Segoe UI",  # Bessere Schriftart
}

# Shop-Items
SHOP_ITEMS = {
    "pokeball": {
        "name": "Pokeball",
        "description": "Ein Ball zum Fangen von Pokemon",
        "price": 200,
        "icon": "🥎",
        "category": "balls",
    },
    "superball": {
        "name": "Superball",
        "description": "Ein verbesserter Ball mit höherer Fangchance",
        "price": 600,
        "icon": "🟦",
        "category": "balls",
    },
    "hyperball": {
        "name": "Hyperball",
        "description": "Der beste Ball mit sehr hoher Fangchance",
        "price": 1200,
        "icon": "🟨",
        "category": "balls",
    },
    "trank": {
        "name": "Trank",
        "description": "Heilt 20 HP eines Pokemon",
        "price": 300,
        "icon": "🧪",
        "category": "healing",
    },
    "supertrank": {
        "name": "Supertrank",
        "description": "Heilt 50 HP eines Pokemon",
        "price": 700,
        "icon": "💉",
        "category": "healing",
    },
    "hypertrank": {
        "name": "Hypertrank",
        "description": "Heilt 200 HP eines Pokemon",
        "price": 1200,
        "icon": "💊",
        "category": "healing",
    },
    "beleber": {
        "name": "Beleber",
        "description": "Belebt ein besiegtes Pokemon mit halber HP wieder",
        "price": 1500,
        "icon": "💫",
        "category": "healing",
    },
    "vitalkraut": {
        "name": "Vitalkraut",
        "description": "Heilt alle Statusprobleme eines Pokemon",
        "price": 800,
        "icon": "🌿",
        "category": "healing",
    },
}
