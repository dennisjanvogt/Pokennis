# 🎮 Pokemon Rot - Python Edition

Ein vollständiges Pokemon-Spiel mit grafischer Benutzeroberfläche, inspiriert von den klassischen Pokemon-Spielen!

## 📋 Features

### 🔥 Kern-Gameplay
- **Starter-Pokemon Auswahl**: Wähle zwischen Glumanda, Schiggy und Bisasam
- **Wilde Pokemon fangen**: Über 12 verschiedene Pokemon-Arten
- **Rundenbasierte Kämpfe**: Klassisches Pokemon-Kampfsystem
- **Level-System**: Pokemon entwickeln sich durch Kämpfe weiter
- **Team-Management**: Bis zu 6 Pokemon im Team
- **Vollständiges Shop-System**: Kaufe Pokebälle, Heiltränke und Items
- **Inventar-Management**: Verwende Items zur Heilung und Unterstützung

### ⚔️ Kampfsystem
- **Typ-Effektivität**: Feuer schlägt Pflanze, Wasser schlägt Feuer, etc.
- **Kritische Treffer**: 10% Chance auf extra Schaden
- **Pokemon fangen**: Strategie bei niedrigen HP für bessere Fangchancen
- **Kampfaktionen**: Angreifen, Fangen, Pokemon wechseln, Fliehen
- **Kompakter Kampfbildschirm**: Alles auf einen Blick sichtbar

### 🛒 Shop & Economy
- **Pokemarkt**: Kaufe verschiedene Pokebälle und Heiltränke
- **Geld-System**: Verdiene Geld durch Kämpfe (50₽ pro Sieg)
- **Item-Kategorien**: Pokebälle (Normal, Super, Hyper) und Heilung (Tränke, Beleber)
- **Inventar-Limits**: Realistisches Inventar-Management
- **Preisgestaltung**: Faire Preise für strategische Entscheidungen

### 🎯 Progression
- **Erfahrungspunkte**: Pokemon werden durch Kämpfe stärker
- **Skalierender Schwierigkeitsgrad**: Wilde Pokemon werden mit Fortschritt stärker
- **Pokemon-Center**: Heile deine Pokemon und erhalte neue Pokebälle
- **Statistiken**: Verfolge deine Erfolge
- **Wirtschafts-Progression**: Verdiene Geld für bessere Ausrüstung

### 🖥️ Grafische Oberfläche
- **Vergrößerbares Fenster**: 1400x900 Pixel, vollständig skalierbar
- **Moderne GUI**: Vollständig mit tkinter implementiert
- **Pokemon-Karten**: Visuelle Darstellung mit Farben und Stats
- **HP/EXP Balken**: Übersichtliche Anzeige der Pokemon-Zustände
- **Intuitive Navigation**: Einfache Bedienung mit Buttons
- **Verbesserte Lesbarkeit**: Größere Schriften und bessere Kontraste

## 🚀 Installation & Start

### Voraussetzungen
- **Python 3.6+** (Python 3.8+ empfohlen)
- **tkinter** (normalerweise bereits mit Python installiert)

### Schnellstart
1. **Dateien herunterladen**: Alle Python-Dateien in einen Ordner
2. **Terminal/Kommandozeile öffnen** und zum Spielordner navigieren
3. **Spiel starten**:
   ```bash
   python main.py
   ```

### Dateistruktur
```
pokemon-game/
├── main.py           # Hauptprogramm (hier starten!)
├── gui.py            # Grafische Benutzeroberfläche
├── pokemon.py        # Pokemon-Klasse und Logik
├── trainer.py        # Trainer/Spieler-Klasse
├── battle.py         # Kampfsystem
├── game_data.py      # Pokemon-Daten und Konfiguration
└── README.md         # Diese Anleitung
```

## 🎮 Spielanleitung

### 🏁 Spielstart
1. **Namen eingeben** und "Abenteuer starten" klicken
2. **Starter-Pokemon wählen** aus den drei Optionen
3. **Hauptmenü** erscheint - das Abenteuer beginnt!

### 🌍 Hauptmenü-Optionen
- **🔍 Wilde Pokemon suchen**: Begib dich auf die Suche nach Pokemon
- **👥 Pokemon-Team anzeigen**: Betrachte deine gefangenen Pokemon
- **🎒 Inventar & Items**: Verwalte und verwende deine Items
- **🏥 Pokemon-Center besuchen**: Heile deine Pokemon und erhalte Pokebälle
- **📊 Statistiken anzeigen**: Sieh deine Erfolge ein
- **❌ Spiel beenden**: Verlasse das Spiel

### 🛒 Shop-System
1. **Pokemarkt besuchen**: Laufe zum Shop-Gebäude (🛒) auf der Map
2. **Items kaufen**: Wähle zwischen verschiedenen Kategorien
   - **Pokebälle**: Normal (200₽), Super (600₽), Hyper (1200₽)
   - **Heilung**: Trank (300₽), Supertrank (700₽), Hypertrank (1200₽)
   - **Spezial**: Beleber (1500₽), Vitalkraut (800₽)
3. **Inventar verwalten**: Verwende Items im Inventar-Menü
4. **Geld verdienen**: 50₽ pro gewonnenem Kampf

### 💊 Item-Verwendung
- **Tränke**: Heilen 20/50/200 HP je nach Typ
- **Beleber**: Belebt besiegte Pokemon mit halber HP wieder
- **Vitalkraut**: Heilt alle Statusprobleme
- **Bessere Pokebälle**: Höhere Fangchance bei wilden Pokemon

### ⚔️ Kampf-Strategien
1. **Type-Advantage nutzen**: Achte auf Typ-Effektivität
2. **Pokemon schwächen**: Senke HP für bessere Fangchancen
3. **Team-Rotation**: Wechsle Pokemon strategisch
4. **Pokebälle sparen**: Besuche regelmäßig das Pokemon-Center

### 🎯 Progression-Tipps
- **Kämpfe regelmäßig**: Mehr Siege = stärkere wilde Pokemon
- **Team diversifizieren**: Verschiedene Typen für alle Situationen
- **Level ausgleichen**: Trainiere alle Pokemon gleichmäßig
- **Pokebälle verwalten**: Immer genug für wichtige Fänge

## 🐛 Fehlerbehebung

### Häufige Probleme

**Spiel startet nicht:**
```bash
# Prüfe Python-Version
python --version

# Prüfe tkinter
python -c "import tkinter; print('tkinter OK')"
```

**"Module not found" Fehler:**
- Stelle sicher, dass alle .py Dateien im gleichen Ordner sind
- Prüfe Dateinamen auf Tippfehler

**GUI erscheint nicht:**
- Linux: `sudo apt-get install python3-tk`
- macOS: `brew install tcl-tk`
- Windows: tkinter sollte standardmäßig verfügbar sein

## 🎨 Anpassungen

### Pokemon-Daten ändern
Bearbeite `game_data.py` um:
- Neue Pokemon hinzuzufügen
- Stats anzupassen
- Farben zu ändern
- Typ-Effektivität zu modifizieren

### Schwierigkeitsgrad anpassen
In `game_data.py` unter `GAME_CONFIG`:
```python
GAME_CONFIG = {
    "max_team_size": 6,        # Max Pokemon im Team
    "starting_pokeballs": 5,   # Start-Pokebälle
    "pokeball_refill": 3,      # Pokebälle pro Center-Besuch
    "exp_multiplier": 15,      # EXP-Multiplikator
    "wild_pokemon_encounter_rate": 0.8  # Begegnungsrate
}
```

### GUI-Design ändern
In `game_data.py` unter `COLORS`:
```python
COLORS = {
    "bg_main": "#2C3E50",      # Haupthintergrund
    "bg_secondary": "#34495E",  # Sekundärer Hintergrund
    "accent": "#E74C3C",       # Akzentfarbe
    "text_light": "#ECF0F1",   # Heller Text
    # ...weitere Farben
}
```

## 📊 Pokemon-Übersicht

### Starter-Pokemon
| Pokemon | Typ | HP | ATK | DEF | Besonderheit |
|---------|-----|----|----|-----|--------------|
| Glumanda | Feuer | 25 | 12 | 8 | Stark gegen Pflanze |
| Schiggy | Wasser | 30 | 10 | 12 | Stark gegen Feuer |
| Bisasam | Pflanze | 28 | 11 | 10 | Stark gegen Wasser |

### Wilde Pokemon
- **Pikachu** (Elektro) - Hoher Angriff, niedrige Verteidigung
- **Rattfratz** (Normal) - Ausgewogene Stats
- **Taubsi** (Normal/Flug) - Schnell aber schwach
- **Raupy** (Käfer) - Niedrige Stats, leicht zu fangen
- **Hornliu** (Käfer/Gift) - Gift-Typ mit mittleren Stats
- **Zubat** (Gift/Flug) - Schnell, schwer zu treffen
- **Digda** (Boden) - Hoher Angriff, niedrige Verteidigung
- **Abra** (Psycho) - Schwach aber selten
- **Machollo** (Kampf) - Hoher Angriff und Verteidigung

## 🔮 Geplante Features

- **Pokemon-Entwicklungen**: Evolution bei bestimmten Leveln
- **Mehr Pokemon**: Erweiterung auf 50+ Pokemon
- **Arenen**: Kampf gegen Gym-Leader
- **Items**: Tränke, Beeren und andere Hilfsmittel
- **Speichersystem**: Spielstand speichern und laden
- **Musik & Sounds**: Audio-Feedback für Aktionen
- **Animationen**: Bewegliche Pokemon-Sprites

## 🤝 Beitragen

Möchtest du das Spiel erweitern? Hier sind einige Ideen:
1. **Neue Pokemon**: Füge Pokemon mit einzigartigen Fähigkeiten hinzu
2. **Kampf-Animationen**: CSS/JS-basierte Animationen
3. **Speichersystem**: JSON-basiertes Speichern/Laden
4. **Multiplayer**: Trainer-gegen-Trainer Kämpfe
5. **Mobile Version**: Android/iOS App

## 📜 Lizenz

Dieses Projekt ist ein Fan-Projekt und für Bildungszwecke gedacht. Pokemon ist ein Markenzeichen von Nintendo/Game Freak/Creatures Inc.

## 🙏 Credits

- **Entwickelt mit**: Python & tkinter
- **Inspiriert von**: Pokemon Rot/Blau (Game Boy, 1996)
- **Erstellt von**: Claude AI Assistant
- **Für**: Alle Pokemon-Fans und Python-Lernende

---

**Viel Spaß beim Spielen und Programmieren! 🎮✨**

*"Gotta code 'em all!"*