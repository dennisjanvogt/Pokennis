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
        "sprite_type": "lizard_fire"
    },
    "Schiggy": {
        "typ": "Wasser",
        "hp": 30,
        "attack": 10,
        "defense": 12,
        "color": "#4488FF",
        "description": "Ein Schildkröten-Pokemon das Wasserstrahlen schießen kann.",
        "sprite_type": "turtle_water"
    },
    "Bisasam": {
        "typ": "Pflanze",
        "hp": 28,
        "attack": 11,
        "defense": 10,
        "color": "#44FF44",
        "description": "Ein Reptil-Pokemon mit einer Zwiebel auf dem Rücken.",
        "sprite_type": "plant_bulb"
    },
    "Pikachu": {
        "typ": "Elektro",
        "hp": 22,
        "attack": 14,
        "defense": 6,
        "color": "#FFDD00",
        "description": "Ein Elektro-Maus Pokemon mit roten Wangen.",
        "sprite_type": "electric_mouse"
    },
    "Rattfratz": {
        "typ": "Normal",
        "hp": 18,
        "attack": 9,
        "defense": 7,
        "color": "#AA8866",
        "description": "Ein kleines Ratten-Pokemon mit scharfen Zähnen.",
        "sprite_type": "rat_normal"
    },
    "Taubsi": {
        "typ": "Normal/Flug",
        "hp": 20,
        "attack": 8,
        "defense": 8,
        "color": "#DDAA77",
        "description": "Ein kleines Vogel-Pokemon das gerne fliegt.",
        "sprite_type": "bird_flying"
    },
    "Raupy": {
        "typ": "Käfer",
        "hp": 15,
        "attack": 6,
        "defense": 9,
        "color": "#88DD88",
        "description": "Ein Raupen-Pokemon das sich später entwickelt.",
        "sprite_type": "caterpillar_bug"
    },
    "Hornliu": {
        "typ": "Käfer/Gift",
        "hp": 17,
        "attack": 10,
        "defense": 8,
        "color": "#AA44AA",
        "description": "Ein Käfer-Pokemon mit giftigen Stacheln.",
        "sprite_type": "beetle_poison"
    },
    "Zubat": {
        "typ": "Gift/Flug",
        "hp": 19,
        "attack": 9,
        "defense": 7,
        "color": "#8844BB",
        "description": "Ein Fledermaus-Pokemon ohne Augen.",
        "sprite_type": "bat_poison"
    },
    "Digda": {
        "typ": "Boden",
        "hp": 16,
        "attack": 12,
        "defense": 5,
        "color": "#CC8844",
        "description": "Ein Maulwurf-Pokemon das unter der Erde lebt.",
        "sprite_type": "mole_ground"
    },
    "Abra": {
        "typ": "Psycho",
        "hp": 14,
        "attack": 7,
        "defense": 6,
        "color": "#FFCC44",
        "description": "Ein psychisches Pokemon das teleportieren kann.",
        "sprite_type": "psychic_humanoid"
    },
    "Machollo": {
        "typ": "Kampf",
        "hp": 24,
        "attack": 15,
        "defense": 11,
        "color": "#CC4444",
        "description": "Ein muskulöses Pokemon das gerne kämpft.",
        "sprite_type": "fighter_muscle"
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
    "bg_secondary": "#2d2d4a",  # Heller als vorher für besseren Kontrast
    "bg_card": "#3a3a5c",  # Deutlich heller für bessere Lesbarkeit
    "accent": "#e94560",  # Rot-Pink Akzent
    "accent_light": "#ff6b7a",  # Hellerer Akzent
    "text_primary": "#f8f9fa",  # Sehr helles Weiß für bessere Lesbarkeit
    "text_secondary": "#dee2e6",  # Hellgrau für sekundären Text
    "text_accent": "#ffd700",  # Goldener Akzenttext
    "text_dark": "#212529",  # Dunkler Text für helle Hintergründe
    "success": "#28a745",  # Grün für Erfolg
    "warning": "#ffc107",  # Gelb für Warnung
    "danger": "#dc3545",  # Rot für Gefahr
    "info": "#17a2b8",  # Blau für Info
    "hp_high": "#28a745",  # Hohe HP - Grün
    "hp_medium": "#ffc107",  # Mittlere HP - Gelb
    "hp_low": "#dc3545",  # Niedrige HP - Rot
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
    "family": "Arial",  # Arial ist universeller verfügbar
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