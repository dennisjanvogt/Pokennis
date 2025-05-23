import random
import time


class Pokemon:
    def __init__(self, name, typ, level=1, hp=None, attack=None, defense=None):
        self.name = name
        self.typ = typ
        self.level = level
        self.max_hp = hp or (20 + level * 5)
        self.current_hp = self.max_hp
        self.attack = attack or (10 + level * 2)
        self.defense = defense or (8 + level * 2)
        self.exp = 0
        self.exp_to_next_level = level * 25

    def is_alive(self):
        return self.current_hp > 0

    def heal(self):
        self.current_hp = self.max_hp

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense // 3)
        self.current_hp = max(0, self.current_hp - actual_damage)
        return actual_damage

    def gain_exp(self, exp):
        self.exp += exp
        leveled_up = False
        while self.exp >= self.exp_to_next_level:
            self.level_up()
            leveled_up = True
        return leveled_up

    def level_up(self):
        self.exp -= self.exp_to_next_level
        self.level += 1
        old_hp = self.max_hp
        old_attack = self.attack
        old_defense = self.defense

        self.max_hp = 20 + self.level * 5
        self.attack = 10 + self.level * 2
        self.defense = 8 + self.level * 2
        self.exp_to_next_level = self.level * 25

        hp_gain = self.max_hp - old_hp
        self.current_hp += hp_gain

        print(f"\n🎉 {self.name} ist auf Level {self.level} gestiegen!")
        print(f"HP: {old_hp} → {self.max_hp} (+{hp_gain})")
        print(f"Angriff: {old_attack} → {self.attack} (+{self.attack - old_attack})")
        print(
            f"Verteidigung: {old_defense} → {self.defense} (+{self.defense - old_defense})"
        )

    def __str__(self):
        return f"{self.name} (Typ: {self.typ}, Level: {self.level}, HP: {self.current_hp}/{self.max_hp})"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_team = []
        self.pokeballs = 5

    def add_pokemon(self, pokemon):
        if len(self.pokemon_team) < 6:
            self.pokemon_team.append(pokemon)
            return True
        return False

    def get_alive_pokemon(self):
        return [p for p in self.pokemon_team if p.is_alive()]

    def heal_all_pokemon(self):
        for pokemon in self.pokemon_team:
            pokemon.heal()


# Pokemon-Datenbank
POKEMON_DATA = {
    "Glumanda": {"typ": "Feuer", "hp": 25, "attack": 12, "defense": 8},
    "Schiggy": {"typ": "Wasser", "hp": 30, "attack": 10, "defense": 12},
    "Bisasam": {"typ": "Pflanze", "hp": 28, "attack": 11, "defense": 10},
    "Pikachu": {"typ": "Elektro", "hp": 22, "attack": 14, "defense": 6},
    "Rattfratz": {"typ": "Normal", "hp": 18, "attack": 9, "defense": 7},
    "Taubsi": {"typ": "Normal/Flug", "hp": 20, "attack": 8, "defense": 8},
    "Raupy": {"typ": "Käfer", "hp": 15, "attack": 6, "defense": 9},
    "Hornliu": {"typ": "Käfer/Gift", "hp": 17, "attack": 10, "defense": 8},
    "Zubat": {"typ": "Gift/Flug", "hp": 19, "attack": 9, "defense": 7},
    "Digda": {"typ": "Boden", "hp": 16, "attack": 12, "defense": 5},
}


def create_random_pokemon(level_range=(1, 5)):
    name = random.choice(list(POKEMON_DATA.keys()))
    data = POKEMON_DATA[name]
    level = random.randint(*level_range)
    return Pokemon(
        name, data["typ"], level, data["hp"], data["attack"], data["defense"]
    )


def battle_system(player, wild_pokemon):
    print(f"\n⚔️  Ein wildes {wild_pokemon.name} erscheint!")
    print(
        f"Level {wild_pokemon.level} | HP: {wild_pokemon.current_hp}/{wild_pokemon.max_hp}"
    )

    while True:
        # Spieler wählt Pokemon
        alive_pokemon = player.get_alive_pokemon()
        if not alive_pokemon:
            print("💀 Alle deine Pokemon sind besiegt! Du rennst davon...")
            return False, False

        print(f"\nDeine Pokemon:")
        for i, pokemon in enumerate(alive_pokemon):
            print(f"{i+1}. {pokemon}")

        try:
            choice = int(input(f"\nWähle ein Pokemon (1-{len(alive_pokemon)}): ")) - 1
            if choice < 0 or choice >= len(alive_pokemon):
                raise ValueError
            current_pokemon = alive_pokemon[choice]
        except (ValueError, IndexError):
            print("Ungültige Auswahl!")
            continue

        print(f"\n{current_pokemon.name}, ich wähle dich!")

        # Kampfschleife
        while current_pokemon.is_alive() and wild_pokemon.is_alive():
            print(f"\n--- {current_pokemon.name} vs {wild_pokemon.name} ---")
            print(
                f"Dein {current_pokemon.name}: {current_pokemon.current_hp}/{current_pokemon.max_hp} HP"
            )
            print(
                f"Wildes {wild_pokemon.name}: {wild_pokemon.current_hp}/{wild_pokemon.max_hp} HP"
            )

            print("\nWas möchtest du tun?")
            print("1. Angreifen")
            print("2. Pokemon fangen")
            print("3. Pokemon wechseln")
            print("4. Fliehen")

            try:
                action = int(input("Wähle eine Aktion (1-4): "))
            except ValueError:
                print("Ungültige Eingabe!")
                continue

            if action == 1:  # Angreifen
                # Spieler greift an
                damage = max(1, current_pokemon.attack + random.randint(-3, 3))
                actual_damage = wild_pokemon.take_damage(damage)
                print(
                    f"\n{current_pokemon.name} greift an und verursacht {actual_damage} Schaden!"
                )

                if not wild_pokemon.is_alive():
                    print(f"💀 {wild_pokemon.name} ist besiegt!")
                    exp_gain = wild_pokemon.level * 15 + random.randint(5, 15)
                    print(f"{current_pokemon.name} erhält {exp_gain} Erfahrungspunkte!")
                    leveled_up = current_pokemon.gain_exp(exp_gain)
                    return True, False  # Gewonnen, nicht gefangen

                # Wildes Pokemon greift an
                time.sleep(1)
                damage = max(1, wild_pokemon.attack + random.randint(-3, 3))
                actual_damage = current_pokemon.take_damage(damage)
                print(
                    f"{wild_pokemon.name} greift {current_pokemon.name} an und verursacht {actual_damage} Schaden!"
                )

                if not current_pokemon.is_alive():
                    print(f"💀 {current_pokemon.name} ist besiegt!")
                    break  # Zurück zur Pokemon-Auswahl

            elif action == 2:  # Pokemon fangen
                if player.pokeballs <= 0:
                    print("❌ Du hast keine Pokebälle mehr!")
                    continue

                player.pokeballs -= 1
                print(
                    f"\n🥎 Du wirfst einen Pokeball... (Pokebälle übrig: {player.pokeballs})"
                )
                time.sleep(1)

                # Fangchance basiert auf HP des wilden Pokemon
                catch_chance = (
                    1 - wild_pokemon.current_hp / wild_pokemon.max_hp
                ) * 0.6 + 0.2
                if random.random() < catch_chance:
                    print(f"🎉 Du hast {wild_pokemon.name} gefangen!")
                    wild_pokemon.heal()  # Gefangene Pokemon werden geheilt
                    if player.add_pokemon(wild_pokemon):
                        print(f"{wild_pokemon.name} wurde deinem Team hinzugefügt!")
                    else:
                        print(
                            f"Dein Team ist voll! {wild_pokemon.name} wurde zu Professor Eich geschickt."
                        )
                    return True, True  # Gewonnen und gefangen
                else:
                    print(f"💔 {wild_pokemon.name} ist ausgebrochen!")
                    # Wildes Pokemon greift nach fehlgeschlagenem Fangversuch an
                    damage = max(1, wild_pokemon.attack + random.randint(-3, 3))
                    actual_damage = current_pokemon.take_damage(damage)
                    print(
                        f"{wild_pokemon.name} greift {current_pokemon.name} an und verursacht {actual_damage} Schaden!"
                    )

                    if not current_pokemon.is_alive():
                        print(f"💀 {current_pokemon.name} ist besiegt!")
                        break

            elif action == 3:  # Pokemon wechseln
                break  # Zurück zur Pokemon-Auswahl

            elif action == 4:  # Fliehen
                print("💨 Du rennst davon!")
                return False, False

            else:
                print("Ungültige Aktion!")


def main_game():
    print("🎮 Willkommen in der Welt der Pokemon!")
    print("=" * 50)

    trainer_name = input("Wie heißt du, junger Trainer? ")
    player = Trainer(trainer_name)

    print(f"\nHallo {trainer_name}! Wähle dein Starter-Pokemon:")
    starters = ["Glumanda", "Schiggy", "Bisasam"]
    for i, starter in enumerate(starters):
        data = POKEMON_DATA[starter]
        print(f"{i+1}. {starter} (Typ: {data['typ']})")

    while True:
        try:
            choice = int(input("Wähle dein Starter-Pokemon (1-3): ")) - 1
            if 0 <= choice < 3:
                starter_name = starters[choice]
                starter_data = POKEMON_DATA[starter_name]
                starter = Pokemon(
                    starter_name,
                    starter_data["typ"],
                    5,
                    starter_data["hp"],
                    starter_data["attack"],
                    starter_data["defense"],
                )
                player.add_pokemon(starter)
                print(
                    f"\n🎉 Du hast {starter_name} gewählt! Viel Glück auf deiner Reise!"
                )
                break
            else:
                print("Ungültige Auswahl!")
        except ValueError:
            print("Bitte gib eine Zahl ein!")

    # Hauptspielschleife
    battles_won = 0
    pokemon_caught = 0

    while True:
        print(
            f"\n🌍 Du wanderst durch die Wildnis... (Siege: {battles_won}, Gefangen: {pokemon_caught})"
        )
        print("\nWas möchtest du tun?")
        print("1. Nach wilden Pokemon suchen")
        print("2. Pokemon-Team anzeigen")
        print("3. Im Pokemon-Center heilen")
        print("4. Spiel beenden")

        try:
            action = int(input("Wähle eine Aktion (1-4): "))
        except ValueError:
            print("Ungültige Eingabe!")
            continue

        if action == 1:  # Pokemon suchen
            if not player.get_alive_pokemon():
                print("❌ Du hast keine kampffähigen Pokemon! Gehe zum Pokemon-Center!")
                continue

            print("\n🔍 Du suchst nach wilden Pokemon...")
            time.sleep(1)

            if random.random() < 0.8:  # 80% Chance ein Pokemon zu finden
                # Level der wilden Pokemon steigt mit gewonnenen Kämpfen
                min_level = max(1, battles_won // 3)
                max_level = max(3, battles_won // 2 + 3)
                wild_pokemon = create_random_pokemon((min_level, max_level))

                won, caught = battle_system(player, wild_pokemon)
                if won:
                    battles_won += 1
                if caught:
                    pokemon_caught += 1
            else:
                print("🍃 Du findest kein Pokemon... versuche es nochmal!")

        elif action == 2:  # Team anzeigen
            print(f"\n👥 {player.name}s Pokemon-Team:")
            print(f"🥎 Pokebälle: {player.pokeballs}")
            if player.pokemon_team:
                for i, pokemon in enumerate(player.pokemon_team):
                    status = "💚" if pokemon.is_alive() else "💀"
                    exp_progress = f"EXP: {pokemon.exp}/{pokemon.exp_to_next_level}"
                    print(f"{i+1}. {status} {pokemon} | {exp_progress}")
            else:
                print("Du hast noch keine Pokemon!")

        elif action == 3:  # Heilen
            print("\n🏥 Willkommen im Pokemon-Center!")
            print("Schwester Joy heilt deine Pokemon...")
            time.sleep(2)
            player.heal_all_pokemon()
            player.pokeballs = min(10, player.pokeballs + 3)  # Pokebälle auffüllen
            print("✨ Deine Pokemon sind vollständig geheilt!")
            print(f"🥎 Du hast {player.pokeballs} Pokebälle erhalten!")

        elif action == 4:  # Spiel beenden
            print(f"\n🎮 Spielstatistiken für {player.name}:")
            print(f"⚔️  Kämpfe gewonnen: {battles_won}")
            print(f"🎯 Pokemon gefangen: {pokemon_caught}")
            print(f"👥 Team-Größe: {len(player.pokemon_team)}")
            print("\nDanke fürs Spielen! Bis zum nächsten Mal!")
            break

        else:
            print("Ungültige Aktion!")


if __name__ == "__main__":
    main_game()
