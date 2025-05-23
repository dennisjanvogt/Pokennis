# 🎮 Pokemon Rot - Python Edition 

**Version 2.0 - Mit Amazing Graphics!**

Ein vollständiges Pokemon-Spiel mit grafischer Benutzeroberfläche und kreativen Pokemon-Grafiken! 

## 🆕 Was ist neu in Version 2.0?

### 🎨 Komplett neue Pokemon-Grafiken
- **Kreative Sprites**: Jedes Pokemon hat eine einzigartige, handgezeichnete Darstellung
- **Typ-spezifische Designs**: Feuer-Pokemon mit Flammen, Wasser-Pokemon mit Tropfen, etc.
- **Detaillierte Animationen**: Bewegende Elemente wie Blitze bei Pikachu
- **Charakteristische Merkmale**: Jedes Pokemon ist sofort erkennbar

### 🛒 Funktionierender Shop
- **Komplett repariertes Shop-System**: Alle Kauf-Bugs behoben
- **Intelligente Pokeball-Auswahl**: Automatische Verwendung der besten verfügbaren Bälle
- **Erweiterte Item-Funktionen**: Alle Heilungs-Items funktionieren korrekt
- **Bessere Fehlerbehandlung**: Klare Fehlermeldungen bei Problemen

### 🖥️ Verbesserte Benutzeroberfläche
- **Bessere Lesbarkeit**: Hellere Textfarben für alle Bildschirmelemente
- **Moderneres Design**: Aufgefrischte Farbpalette und Kontraste
- **Responsive Layout**: Bessere Fenstergrößen und Proportionen
- **Intuitive Navigation**: Klarere Button-Beschriftungen und Icons

## 📋 Features

### 🔥 Kern-Gameplay
- **Starter-Pokemon Auswahl**: Wähle zwischen Glumanda, Schiggy und Bisasam
- **12+ Wilde Pokemon**: Jedes mit einzigartigen Grafiken und Eigenschaften  
- **Rundenbasierte Kämpfe**: Klassisches Pokemon-Kampfsystem mit Typ-Effektivität
- **Level-System**: Pokemon entwickeln sich durch Kämpfe weiter
- **Team-Management**: Bis zu 6 Pokemon im Team
- **Vollständiges Shop-System**: Kaufe Pokebälle, Heiltränke und Items
- **Inventar-Management**: Verwende Items zur Heilung und Unterstützung

### ⚔️ Kampfsystem
- **Typ-Effektivität**: Feuer schlägt Pflanze, Wasser schlägt Feuer, etc.
- **Kritische Treffer**: 10% Chance auf extra Schaden  
- **Intelligente Pokeball-Verwendung**: Automatische Auswahl des besten Balls
- **Flucht-System**: Level-abhängige Fluchtchancen
- **Kampfaktionen**: Angreifen, Fangen, Pokemon wechseln, Fliehen

### 🛒 Shop & Economy
- **Pokemarkt**: Kaufe verschiedene Pokebälle und Heiltränke
- **Drei Ball-Typen**: Normal (200₽), Super (600₽), Hyper (1200₽)
- **Heilungs-Items**: Tränke (300₽), Supertränke (700₽), Hypertränke (1200₽)
- **Spezial-Items**: Beleber (1500₽), Vitalkraut (800₽)
- **Geld-System**: Verdiene 50₽ pro Kampfsieg
- **Inventar-Limits**: Realistische Beschränkungen

### 🎯 Progression
- **Skalierender Schwierigkeitsgrad**: Wilde Pokemon werden mit Fortschritt stärker
- **Pokemon-Center**: Heile deine Pokemon und erhalte neue Pokebälle
- **Statistiken**: Verfolge deine Erfolge und Fortschritte
- **Wirtschafts-Progression**: Verdiene Geld für bessere Ausrüstung

### 🎨 Grafische Pokemon-Darstellungen

#### 🔥 Feuer-Typ: Glumanda
- Körper in Orange-Rot mit hellerem Bauch
- Flammen-Schwanz mit wechselnden Farben
- Kleine Arme und charakteristische Augen

#### 💧 Wasser-Typ: Schiggy  
- Blauer Panzer mit sechseckigem Muster
- Kopf und Beine in helleren Blautönen
- Wassertropfen-Animation

#### 🌿 Pflanze-Typ: Bisasam
- Grüner Körper mit Zwiebel auf dem Rücken
- Flecken auf der Zwiebel und kleine Blätter
- Freundliche Augen mit Glanzpunkten

#### ⚡ Elektro-Typ: Pikachu  
- Gelber Körper mit spitzen Ohren
- Schwarze Ohrenspitzen und rote Wangen
- Blitz-förmiger Schwanz mit Elektro-Funken

#### 🐭 Normal-Typ: Rattfratz
- Länglicher Körper in Brauntönen
- Große Vorderzähne und spitze Ohren
- Gewellter Schwanz

#### 🐦 Normal/Flug-Typ: Taubsi
- Vogelkörper mit ausgebreiteten Flügeln
- Oranger Schnabel und Schwanzfedern
- Kleine schwarze Krallen

#### 🐛 Käfer-Typ: Raupy
- Segmentierter Körper in wechselnden Grüntönen
- Große Augen und Antennenfühler
- Kleine Beine unter jedem Segment

#### 🕸️ Käfer/Gift-Typ: Hornliu
- Lila Körper mit großem Horn
- Giftstacheln und komplexe Facettenaugen
- Sechs Beine mit kleinen Klauen

#### 🦇 Gift/Flug-Typ: Zubat
- Fledermaus mit großen Flügelmembranen
- Keine Augen, aber große Ohren
- Schallwellen für Echolot-Darstellung

#### 🕳️ Boden-Typ: Digda  
- Kopf ragt aus Erdloch heraus
- Rosa Nase und kleine Augen
- Erdklumpen um das Loch

#### 🧠 Psycho-Typ: Abra
- Humanoider gelber Körper
- Geschlossene Augen (meditiert)
- Psychische Aura und Energie-Funken

#### 💪 Kampf-Typ: Machollo
- Muskulöser roter Körper
- Aufgepumpte Bizeps und Sixpack
- Kraftlinien zeigen Stärke-Aura

## 🚀 Installation & Start

### Voraussetzungen
- **Python 3.6+** (Python 3.8+ empfohlen)
- **tkinter** (normalerweise bereits mit Python installiert)

### Schnellstart
1. **Alle Dateien herunterladen** in einen Ordner:
   ```
   pokemon-game/
   ├── main.py                    # ← HIER STARTEN!
   ├── pokemon_gui.py            # Hauptinterface
   ├── pokemon_sprites.py        # Neue Grafik-Engine
   ├── pokemon.py               # Pokemon-Logik
   ├── trainer_class.py         # Spieler/Trainer
   ├── battle.py                # Kampfsystem
   ├── game_data.py             # Daten & Konfiguration
   └── README.md                # Diese Anleitung
   ```

2. **Terminal/Kommandozeile öffnen** und zum Spielordner navigieren

3. **Spiel starten**:
   ```bash
   python main.py
   ```

## 🎮 Spielanleitung

### 🏁 Spielstart
1. **Namen eingeben** und "Abenteuer starten" klicken
2. **Starter-Pokemon wählen** - jetzt mit neuen Grafiken!
3. **Welt erkunden** mit WASD oder Pfeiltasten

### 🗺️ Overworld-Navigation
- **🌿 Gras**: Wilde Pokemon-Begegnungen
- **🏥 Pokemon Center**: Heilung + gratis Pokebälle  
- **🛒 Pokemarkt**: Items kaufen
- **🟫 Wege**: Sichere Bewegung

### ⚔️ Kampfsystem
1. **Angreifen**: Nutze Typ-Vorteile für mehr Schaden
2. **Pokemon fangen**: Schwäche sie erst, dann fangen
3. **Pokemon wechseln**: Strategisch das richtige Pokemon wählen
4. **Fliehen**: Bei übermächtigen Gegnern

### 🛒 Shop-Guide
1. **Pokemarkt besuchen**: Laufe zum 🛒 Symbol
2. **Pokebälle kaufen**:
   - **Pokeball** (200₽): Standard-Fangrate
   - **Superball** (600₽): 50% höhere Fangchance  
   - **Hyperball** (1200₽): 100% höhere Fangchance
3. **Heilungs-Items**:
   - **Trank** (300₽): +20 HP
   - **Supertrank** (700₽): +50 HP
   - **Hypertrank** (1200₽): +200 HP
   - **Beleber** (1500₽): Belebt besiegte Pokemon wieder
   - **Vitalkraut** (800₽): Heilt Statusprobleme

### 💊 Item-Verwendung
- **Inventar öffnen**: Über das Hauptmenü
- **Pokemon auswählen**: Für Heilungs-Items
- **Schnell-Heilung**: "Alle Pokemon heilen" Button
- **Automatische Ball-Auswahl**: Spiel wählt besten verfügbaren Ball

## 🎯 Tipps & Strategien

### 💰 Geld verdienen
- Kämpfe gegen wilde Pokemon (50₽ pro Sieg)
- Spare für bessere Pokebälle
- Kaufe Items strategisch

### 🎭 Typ-Matchups nutzen
- **Feuer** > Pflanze, Käfer
- **Wasser** > Feuer, Boden  
- **Pflanze** > Wasser, Boden
- **Elektro** > Wasser, Flug
- **Kampf** > Normal

### 🎣 Pokemon fangen
1. Schwäche das wilde Pokemon (niedrige HP = höhere Fangchance)
2. Verwende bessere Pokebälle für schwere Fänge
3. Spare Hyperbälle für seltene/starke Pokemon

### 📈 Team-Entwicklung
- Trainiere alle Pokemon gleichmäßig
- Nutze das Pokemon-Center regelmäßig
- Baue ein ausgewogenes Team mit verschiedenen Typen

## 🐛 Fehlerbehebung

### Häufige Probleme

**Spiel startet nicht:**
```bash
# Prüfe Python-Version
python --version

# Prüfe tkinter
python -c "import tkinter; print('tkinter funktioniert!')"
```

**Shop funktioniert nicht:**
- **Wurde behoben!** Version 2.0 hat alle Shop-Bugs repariert
- Bei Problemen: Spiel neu starten

**Grafiken werden nicht angezeigt:**
- Stelle sicher, dass `pokemon_sprites.py` im gleichen Ordner ist
- Prüfe Dateiname auf Tippfehler

**"Module not found" Fehler:**
- Alle .py Dateien müssen im gleichen Ordner sein
- Prüfe Dateinamen auf Korrektheit

**GUI erscheint nicht:**
- **Linux**: `sudo apt-get install python3-tk`
- **macOS**: `brew install tcl-tk`  
- **Windows**: tkinter sollte standardmäßig verfügbar sein

## 🔧 Anpassungen

### Pokemon-Grafiken ändern
Bearbeite `pokemon_sprites.py`:
```python
@staticmethod
def _draw_mein_pokemon(canvas, x, y, size, color):
    # Deine eigene Pokemon-Grafik hier!
    canvas.create_oval(...)
```

### Neue Pokemon hinzufügen
In `game_data.py`:
```python
POKEMON_DATA = {
    "MeinPokemon": {
        "typ": "Feuer",
        "hp": 25,
        "attack": 12, 
        "defense": 8,
        "color": "#FF4444",
        "description": "Mein eigenes Pokemon!",
        "sprite_type": "mein_sprite_typ"
    }
}
```

### Schwierigkeitsgrad anpassen
In `game_data.py` unter `GAME_CONFIG`:
```python
GAME_CONFIG = {
    "starting_money": 2000,        # Mehr Startgeld
    "money_per_battle": 100,       # Mehr Geld pro Kampf
    "wild_pokemon_encounter_rate": 0.3  # Mehr Begegnungen
}
```

### Farben ändern
In `game_data.py` unter `COLORS`:
```python
COLORS = {
    "bg_main": "#YOUR_COLOR",      # Haupthintergrund
    "text_primary": "#YOUR_COLOR", # Haupttext
    "accent": "#YOUR_COLOR",       # Akzentfarbe
}
```

## 📊 Pokemon-Übersicht

| Pokemon | Typ | HP | ATK | DEF | Grafik-Features |
|---------|-----|----|----|-----|-----------------|
| Glumanda | Feuer | 25 | 12 | 8 | Flammen-Schwanz |
| Schiggy | Wasser | 30 | 10 | 12 | Panzer-Muster |
| Bisasam | Pflanze | 28 | 11 | 10 | Zwiebel + Blätter |
| Pikachu | Elektro | 22 | 14 | 6 | Blitz-Schwanz |
| Rattfratz | Normal | 18 | 9 | 7 | Große Zähne |
| Taubsi | Normal/Flug | 20 | 8 | 8 | Ausgebreitete Flügel |
| Raupy | Käfer | 15 | 6 | 9 | Segmentierter Körper |
| Hornliu | Käfer/Gift | 17 | 10 | 8 | Giftstacheln |
| Zubat | Gift/Flug | 19 | 9 | 7 | Flügelmembranen |
| Digda | Boden | 16 | 12 | 5 | Aus Erdloch ragend |
| Abra | Psycho | 14 | 7 | 6 | Psychische Aura |
| Machollo | Kampf | 24 | 15 | 11 | Muskulöser Körper |

## 🔮 Geplante Features (Version 3.0)

- **Pokemon-Entwicklungen**: Evolution bei bestimmten Leveln
- **Mehr Pokemon**: Erweiterung auf 50+ Pokemon
- **Gym-Leader**: Kämpfe gegen spezielle Trainer
- **Speichersystem**: Spielstand speichern und laden
- **Sound-Effekte**: Audio-Feedback für alle Aktionen
- **Animierte Sprites**: Bewegliche Pokemon-Grafiken
- **Multiplayer**: Trainer-gegen-Trainer Kämpfe

## 🤝 Beitragen

Möchtest du das Spiel erweitern?

### Code-Beiträge
1. **Neue Pokemon-Sprites** in `pokemon_sprites.py`
2. **Gameplay-Features** in den entsprechenden Modulen
3. **Bug-Fixes** und Verbesserungen

### Grafik-Beiträge  
1. Erstelle neue `_draw_pokemon()` Funktionen
2. Füge `sprite_type` in `POKEMON_DATA` hinzu
3. Teste die Darstellung in verschiedenen Größen

### Balance-Änderungen
1. Bearbeite `POKEMON_DATA` für Stats
2. Ändere `TYPE_EFFECTIVENESS` für Balancing
3. Passe `SHOP_ITEMS` Preise an

## 📜 Technische Details

### Architektur
- **MVC-Pattern**: Klare Trennung von Daten, Logik und Darstellung
- **Modularer Aufbau**: Jede Datei hat eine spezifische Funktion
- **Event-driven**: GUI reagiert auf Benutzerinteraktionen

### Grafik-Engine
- **Canvas-basiert**: Verwendung von tkinter Canvas für Sprites
- **Vektorbasiert**: Alle Grafiken sind skalierbar
- **Typ-abhängig**: Automatische Sprite-Auswahl basierend auf Pokemon-Typ

### Datenstruktur
- **Pokemon-Objekte**: Vollständige Kapselung von Eigenschaften
- **Trainer-System**: Inventar, Team und Fortschritt
- **Battle-Engine**: Zustandsbasiertes Kampfsystem

## 📜 Lizenz

Dieses Projekt ist ein Fan-Projekt für Bildungszwecke. Pokemon ist ein Markenzeichen von Nintendo/Game Freak/Creatures Inc.

## 🙏 Credits

- **Entwickelt mit**: Python & tkinter
- **Inspiriert von**: Pokemon Rot/Blau (Game Boy, 1996)
- **Grafik-System**: Komplett eigene Implementierung
- **Erstellt von**: Claude AI Assistant
- **Version 2.0**: Erweiterte Grafiken und Shop-Fixes

---

**Viel Spaß beim Spielen und Programmieren! 🎮✨**

*"Gotta code 'em all!"*

---

## 🆕 Changelog

### Version 2.0 (Aktuell)
- ✅ Komplett neue Pokemon-Grafiken für alle 12 Pokemon
- ✅ Shop-System vollständig repariert
- ✅ Verbesserte Textlesbarkeit
- ✅ Intelligente Pokeball-Auswahl
- ✅ Erweiterte Fehlerbehandlung
- ✅ Moderneres UI-Design

### Version 1.0
- ✅ Grundlegendes Pokemon-Spiel
- ✅ Einfache Grafiken
- ✅ Basis-Shop (mit Bugs)
- ✅ Kampfsystem
- ✅ Team-Management