# trainer_class.py
"""
Trainer Klasse für Spieler und NPCs
"""
from pokemon import Pokemon
from game_data import GAME_CONFIG

class Trainer:
    def __init__(self, name, is_player=True):
        self.name = name
        self.is_player = is_player
        self.pokemon_team = []
        self.pokeballs = GAME_CONFIG["starting_pokeballs"] if is_player else 0
        self.battles_won = 0
        self.pokemon_caught = 0
        self.money = GAME_CONFIG["starting_money"] if is_player else 0
        
        # Inventar für Items
        self.inventory = {
            "pokeball": GAME_CONFIG["starting_pokeballs"],
            "superball": 0,
            "hyperball": 0,
            "trank": 2,  # Starter-Tränke
            "supertrank": 0,
            "hypertrank": 0,
            "beleber": 0,
            "vitalkraut": 0
        }
        
    def add_pokemon(self, pokemon):
        """Fügt Pokemon zum Team hinzu"""
        if len(self.pokemon_team) < GAME_CONFIG["max_team_size"]:
            self.pokemon_team.append(pokemon)
            if self.is_player:
                self.pokemon_caught += 1
            return True
        return False
    
    def remove_pokemon(self, pokemon):
        """Entfernt Pokemon aus dem Team"""
        if pokemon in self.pokemon_team:
            self.pokemon_team.remove(pokemon)
            return True
        return False
    
    def get_alive_pokemon(self):
        """Gibt alle lebenden Pokemon zurück"""
        return [p for p in self.pokemon_team if p.is_alive()]
    
    def get_first_alive_pokemon(self):
        """Gibt das erste lebende Pokemon zurück"""
        alive = self.get_alive_pokemon()
        return alive[0] if alive else None
    
    def has_usable_pokemon(self):
        """Prüft ob Trainer kampffähige Pokemon hat"""
        return len(self.get_alive_pokemon()) > 0
    
    def heal_all_pokemon(self):
        """Heilt alle Pokemon vollständig"""
        for pokemon in self.pokemon_team:
            pokemon.heal()
    
    def add_pokeballs(self, amount):
        """Fügt Pokebälle hinzu"""
        if self.is_player:
            # Normale Pokebälle hinzufügen
            new_amount = min(GAME_CONFIG["max_pokeballs"], 
                           self.inventory.get("pokeball", 0) + amount)
            self.inventory["pokeball"] = new_amount
            self.pokeballs = self.get_total_pokeballs()  # Update für Kompatibilität
    
    def use_pokeball(self, ball_type="pokeball"):
        """Verwendet einen Pokeball eines bestimmten Typs"""
        if self.inventory.get(ball_type, 0) > 0:
            self.inventory[ball_type] -= 1
            self.pokeballs = self.get_total_pokeballs()  # Update für Kompatibilität
            return True
        return False
    
    def get_team_info(self):
        """Gibt Informationen über das gesamte Team zurück"""
        team_info = []
        for i, pokemon in enumerate(self.pokemon_team):
            info = pokemon.get_info_dict()
            info["team_position"] = i
            team_info.append(info)
        return team_info
    
    def get_strongest_pokemon(self):
        """Gibt das stärkste Pokemon zurück"""
        if not self.pokemon_team:
            return None
        return max(self.pokemon_team, key=lambda p: p.level * p.attack)
    
    def get_team_level_average(self):
        """Berechnet durchschnittliches Level des Teams"""
        if not self.pokemon_team:
            return 1
        return sum(p.level for p in self.pokemon_team) / len(self.pokemon_team)
    
    def win_battle(self, exp_reward=0, money_reward=0):
        """Verarbeitet Kampfsieg"""
        self.battles_won += 1
        if self.is_player:
            if money_reward == 0:
                money_reward = GAME_CONFIG["money_per_battle"]
            self.money += money_reward
    
    def buy_item(self, item_id, quantity=1):
        """Kauft Items im Shop - REPARIERT"""
        try:
            from game_data import SHOP_ITEMS
            
            if item_id not in SHOP_ITEMS:
                return False, "Item existiert nicht!"
                
            item = SHOP_ITEMS[item_id]
            total_cost = item["price"] * quantity
            
            # Prüfe ob genug Geld vorhanden
            if self.money < total_cost:
                return False, f"Nicht genug Geld! Benötigt: {total_cost}₽, verfügbar: {self.money}₽"
                
            # Prüfe Inventar-Limits
            current_amount = self.inventory.get(item_id, 0)
            
            if item["category"] == "balls":
                # Prüfe Pokeball-Limit
                total_balls_after = self.get_total_pokeballs() + quantity
                if total_balls_after > GAME_CONFIG["max_pokeballs"]:
                    return False, f"Pokeball-Inventar voll! Maximum: {GAME_CONFIG['max_pokeballs']}, derzeit: {self.get_total_pokeballs()}"
            elif item["category"] == "healing":
                # Prüfe Heilungs-Item Limit
                if current_amount + quantity > GAME_CONFIG["max_potions"]:
                    return False, f"Heilungs-Inventar voll! Maximum: {GAME_CONFIG['max_potions']} pro Item-Typ"
                    
            # Kauf durchführen
            self.money -= total_cost
            self.inventory[item_id] = current_amount + quantity
            
            # Update Pokebälle separat für Kompatibilität
            if item_id == "pokeball":
                self.pokeballs = self.inventory["pokeball"]
                
            return True, f"✅ {quantity}x {item['name']} gekauft für {total_cost}₽!\n💰 Verbleibendes Geld: {self.money}₽"
            
        except Exception as e:
            return False, f"Fehler beim Kauf: {str(e)}"
    
    def use_item(self, item_id, target_pokemon=None):
        """Verwendet ein Item aus dem Inventar"""
        try:
            if item_id not in self.inventory or self.inventory[item_id] <= 0:
                return False, "Item nicht verfügbar!"
                
            from game_data import SHOP_ITEMS
            
            if item_id not in SHOP_ITEMS:
                return False, "Unbekanntes Item!"
                
            item = SHOP_ITEMS[item_id]
            
            if item["category"] == "healing" and not target_pokemon:
                return False, "Ziel-Pokemon benötigt!"
                
            # Prüfe ob Item anwendbar ist
            if target_pokemon:
                if item_id == "beleber" and target_pokemon.is_alive():
                    return False, f"{target_pokemon.name} ist nicht besiegt!"
                elif item_id in ["trank", "supertrank", "hypertrank"] and target_pokemon.current_hp >= target_pokemon.max_hp:
                    return False, f"{target_pokemon.name} hat bereits volle HP!"
                elif item_id == "vitalkraut" and target_pokemon.status == "Normal":
                    return False, f"{target_pokemon.name} hat keine Statusprobleme!"
            
            # Item verwenden
            self.inventory[item_id] -= 1
            
            if item_id == "trank":
                old_hp = target_pokemon.current_hp
                target_pokemon.current_hp = min(target_pokemon.max_hp, target_pokemon.current_hp + 20)
                healed = target_pokemon.current_hp - old_hp
                return True, f"✨ {target_pokemon.name} wurde um {healed} HP geheilt!"
                
            elif item_id == "supertrank":
                old_hp = target_pokemon.current_hp
                target_pokemon.current_hp = min(target_pokemon.max_hp, target_pokemon.current_hp + 50)
                healed = target_pokemon.current_hp - old_hp
                return True, f"✨ {target_pokemon.name} wurde um {healed} HP geheilt!"
                
            elif item_id == "hypertrank":
                old_hp = target_pokemon.current_hp
                target_pokemon.current_hp = min(target_pokemon.max_hp, target_pokemon.current_hp + 200)
                healed = target_pokemon.current_hp - old_hp
                return True, f"✨ {target_pokemon.name} wurde um {healed} HP geheilt!"
                
            elif item_id == "beleber":
                target_pokemon.current_hp = target_pokemon.max_hp // 2
                return True, f"💫 {target_pokemon.name} wurde wiederbelebt mit {target_pokemon.current_hp} HP!"
                
            elif item_id == "vitalkraut":
                old_status = target_pokemon.status
                target_pokemon.status = "Normal"
                return True, f"🌿 {target_pokemon.name} wurde von Statuseffekt '{old_status}' geheilt!"
                
            return False, "Item konnte nicht verwendet werden!"
            
        except Exception as e:
            return False, f"Fehler bei Item-Verwendung: {str(e)}"
    
    def get_total_pokeballs(self):
        """Gibt Gesamtanzahl aller Pokebälle zurück"""
        return (self.inventory.get("pokeball", 0) + 
                self.inventory.get("superball", 0) + 
                self.inventory.get("hyperball", 0))
    
    def get_stats(self):
        """Gibt Spielerstatistiken zurück"""
        return {
            "name": self.name,
            "battles_won": self.battles_won,
            "pokemon_caught": self.pokemon_caught,
            "team_size": len(self.pokemon_team),
            "pokeballs": self.get_total_pokeballs(),
            "money": self.money,
            "strongest_pokemon": self.get_strongest_pokemon().name if self.get_strongest_pokemon() else "Keins",
            "team_average_level": round(self.get_team_level_average(), 1)
        }
    
    def get_inventory_summary(self):
        """Gibt eine Übersicht des Inventars zurück"""
        summary = {}
        from game_data import SHOP_ITEMS
        
        for item_id, amount in self.inventory.items():
            if amount > 0 and item_id in SHOP_ITEMS:
                item_info = SHOP_ITEMS[item_id]
                summary[item_id] = {
                    "name": item_info["name"],
                    "amount": amount,
                    "icon": item_info["icon"],
                    "category": item_info["category"]
                }
        
        return summary
    
    def can_afford(self, item_id, quantity=1):
        """Prüft ob der Trainer sich ein Item leisten kann"""
        try:
            from game_data import SHOP_ITEMS
            if item_id not in SHOP_ITEMS:
                return False
            
            total_cost = SHOP_ITEMS[item_id]["price"] * quantity
            return self.money >= total_cost
        except:
            return False
    
    def get_item_count(self, item_id):
        """Gibt die Anzahl eines bestimmten Items zurück"""
        return self.inventory.get(item_id, 0)
    
    def has_item(self, item_id):
        """Prüft ob der Trainer ein bestimmtes Item besitzt"""
        return self.get_item_count(item_id) > 0
    
    def __str__(self):
        alive_count = len(self.get_alive_pokemon())
        return f"Trainer {self.name} ({alive_count}/{len(self.pokemon_team)} Pokemon kampfbereit, {self.money}₽)"
    
    def __repr__(self):
        return f"Trainer(name='{self.name}', pokemon={len(self.pokemon_team)}, money={self.money})"