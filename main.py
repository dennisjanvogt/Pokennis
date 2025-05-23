#!/usr/bin/env python3
# main.py
"""
Pokemon Rot - Python Edition
Hauptprogramm zum Starten des Spiels

Erstellt von: Claude AI
Version: 1.0
"""

import sys
import os
import traceback
from pokemon_gui import PokemonGUI


def check_dependencies():
    """Prüft ob alle benötigten Module verfügbar sind"""
    required_modules = ["tkinter", "random"]
    missing_modules = []

    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        print("❌ Fehlende Module:")
        for module in missing_modules:
            print(f"   - {module}")
        print("\nBitte installiere die fehlenden Module:")
        print("pip install tkinter")
        return False

    return True


def main():
    """Hauptfunktion - Startet das Pokemon-Spiel"""
    print("🎮 Pokemon Rot - Python Edition")
    print("=" * 50)
    print("Starte Spiel...")

    # Prüfe Dependencies
    if not check_dependencies():
        input("Drücke Enter zum Beenden...")
        return

    try:
        # Erstelle und starte GUI
        game = PokemonGUI()
        print("✅ GUI erfolgreich geladen!")
        print("🎯 Viel Spaß beim Spielen!")
        print("=" * 50)

        # Starte das Spiel
        game.run()

    except Exception as e:
        print(f"❌ Fehler beim Starten des Spiels: {e}")
        print("\nDetaillierte Fehlermeldung:")
        traceback.print_exc()
        input("Drücke Enter zum Beenden...")


if __name__ == "__main__":
    main()
