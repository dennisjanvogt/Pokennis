# battle.py
"""
Kampfsystem für Pokemon-Kämpfe
"""
import random
from pokemon import Pokemon
from game_data import POKEMON_DATA, GAME_CONFIG

class BattleResult:
    def __init__(self):
        self.winner = None
        self.loser = None
        self.exp_gained = 0
        self.pokemon_caught = None
        self.battle_log = []
        self.money_earned = 0
        
class Battle:
    def __init__(self, player_trainer, opponent_pokemon=None, opponent_trainer=None):
        self.player = player_trainer
        self.opponent_pokemon = opponent_pokemon
        self.opponent_trainer = opponent_trainer
        self.is_wild_battle = opponent_pokemon is not None
        self.battle_log = []
        self.turn_count = 0
        
    def start_battle(self):
        """Startet einen Kampf"""
        if self.is_wild_battle:
            return self._wild_battle()
        else:
            return self._trainer_battle()
    
    def _wild_battle(self):
        """Führt einen Kampf gegen ein wildes Pokemon durch"""
        result = BattleResult()
        wild_pokemon = self.opponent_pokemon
        
        self.log(f"Ein wildes {wild_pokemon.name} (Lv.{wild_pokemon.level}) erscheint!")
        
        # Spieler wählt Pokemon (wird in GUI gehandhabt)
        # Hier nehmen wir das erste verfügbare Pokemon
        player_pokemon = self.player.get_first_alive_pokemon()
        if not player_pokemon:
            result.winner = "wild"
            result.loser = "player"
            self.log("Du hast keine kampffähigen Pokemon!")
            return result
            
        self.log(f"Los, {player_pokemon.name}!")
        return result
    
    def execute_turn(self, player_action, player_pokemon=None, target_pokemon=None):
        """Führt eine Kampfrunde aus"""
        result = {"success": False, "message": "", "battle_over": False, "winner": None}
        
        if not player_pokemon:
            player_pokemon = self.player.get_first_alive_pokemon()
        
        if not target_pokemon:
            target_pokemon = self.opponent_pokemon
            
        self.turn_count += 1
        
        if player_action == "attack":
            result = self._execute_attack(player_pokemon, target_pokemon)
        elif player_action == "catch":
            result = self._execute_catch(target_pokemon)
        elif player_action == "run":
            result = self._execute_run()
        elif player_action == "switch":
            result = {"success": True, "message": "Pokemon gewechselt!", "battle_over": False}
            
        # Gegner-Zug (nur wenn Kampf nicht vorbei und wildes Pokemon)
        if not result["battle_over"] and self.is_wild_battle and target_pokemon.is_alive():
            opponent_result = self._opponent_turn(target_pokemon, player_pokemon)
            result["message"] += "\n" + opponent_result["message"]
            if opponent_result["battle_over"]:
                result["battle_over"] = True
                result["winner"] = opponent_result["winner"]
                
        return result
    
    def _execute_attack(self, attacker, defender):
        """Führt einen Angriff aus"""
        attack_result = attacker.attack_pokemon(defender)
        damage = attack_result["damage"]
        effectiveness = attack_result["effectiveness"]
        
        message = f"💥 {attacker.name} greift an und verursacht {damage} Schaden!"
        
        if effectiveness > 1.0:
            message += " ✨ Das ist sehr effektiv!"
        elif effectiveness < 1.0:
            message += " 💧 Das ist nicht sehr effektiv..."
        
        if attack_result["critical"]:
            message += " 🎯 Kritischer Treffer!"
            
        battle_over = False
        winner = None
        
        if not defender.is_alive():
            message += f"\n💀 {defender.name} ist besiegt!"
            battle_over = True
            winner = "player" if attacker == self.player.get_first_alive_pokemon() else "opponent"
            
            # EXP vergeben bei Sieg
            if winner == "player":
                exp_gain = self._calculate_exp_gain(defender)
                leveled_up = attacker.gain_exp(exp_gain)
                message += f"\n⭐ {attacker.name} erhält {exp_gain} EXP!"
                if leveled_up:
                    message += f"\n🎉 {attacker.name} ist auf Level {attacker.level} gestiegen!"
        
        return {
            "success": True,
            "message": message,
            "battle_over": battle_over,
            "winner": winner,
            "damage": damage,
            "effectiveness": effectiveness
        }
    
    def _execute_catch(self, wild_pokemon):
        """Versucht ein wildes Pokemon zu fangen - Verbessert"""
        # Bestimme welchen Pokeball-Typ verwenden
        ball_type = self._determine_best_pokeball()
        
        if not self.player.use_pokeball(ball_type):
            return {
                "success": False,
                "message": "❌ Du hast keine Pokebälle mehr!",
                "battle_over": False
            }
        
        # Fangchance berechnen (abhängig vom Ball-Typ)
        catch_rate = self._calculate_catch_rate(wild_pokemon, ball_type)
        success = random.random() < catch_rate
        
        ball_names = {
            "pokeball": "Pokeball",
            "superball": "Superball", 
            "hyperball": "Hyperball"
        }
        ball_name = ball_names.get(ball_type, "Pokeball")
        
        if success:
            wild_pokemon.heal()  # Gefangene Pokemon werden geheilt
            if self.player.add_pokemon(wild_pokemon):
                message = f"🎉 Gotcha! {wild_pokemon.name} wurde mit einem {ball_name} gefangen und dem Team hinzugefügt!"
            else:
                message = f"🎉 Gotcha! {wild_pokemon.name} wurde mit einem {ball_name} gefangen, aber das Team ist voll!\n📦 Es wurde zur Pokemon-Box gesendet."
                
            return {
                "success": True,
                "message": message,
                "battle_over": True,
                "winner": "player",
                "caught_pokemon": wild_pokemon
            }
        else:
            return {
                "success": False,
                "message": f"💔 {wild_pokemon.name} ist aus dem {ball_name} ausgebrochen!",
                "battle_over": False
            }
    
    def _determine_best_pokeball(self):
        """Bestimmt den besten verfügbaren Pokeball"""
        # Verwende den besten verfügbaren Ball
        if self.player.has_item("hyperball"):
            return "hyperball"
        elif self.player.has_item("superball"):
            return "superball"
        elif self.player.has_item("pokeball"):
            return "pokeball"
        else:
            return "pokeball"  # Fallback
    
    def _execute_run(self):
        """Versucht vor dem Kampf zu fliehen"""
        if self.is_wild_battle:
            # Erfolgschance beim Fliehen (abhängig von Level-Unterschied)
            player_pokemon = self.player.get_first_alive_pokemon()
            if player_pokemon:
                level_diff = player_pokemon.level - self.opponent_pokemon.level
                escape_chance = 0.5 + (level_diff * 0.1)  # Base 50% + Level-Bonus
                escape_chance = max(0.1, min(0.9, escape_chance))  # Zwischen 10% und 90%
                
                if random.random() < escape_chance:
                    return {
                        "success": True,
                        "message": "💨 Du bist erfolgreich geflohen!",
                        "battle_over": True,
                        "winner": "run"
                    }
                else:
                    return {
                        "success": False,
                        "message": "❌ Flucht fehlgeschlagen! Du bist zu langsam!",
                        "battle_over": False
                    }
            else:
                return {
                    "success": True,
                    "message": "💨 Du bist erfolgreich geflohen!",
                    "battle_over": True,
                    "winner": "run"
                }
        else:
            # Gegen Trainer kann man nicht fliehen
            return {
                "success": False,
                "message": "❌ Du kannst nicht vor einem Trainer-Kampf fliehen!",
                "battle_over": False
            }
    
    def _opponent_turn(self, opponent_pokemon, player_pokemon):
        """KI-Zug für wildes Pokemon oder Trainer"""
        if not opponent_pokemon.is_alive():
            return {"success": False, "message": "", "battle_over": False}
            
        # Einfache KI: Immer angreifen
        attack_result = opponent_pokemon.attack_pokemon(player_pokemon)
        damage = attack_result["damage"]
        effectiveness = attack_result["effectiveness"]
        
        message = f"💥 {opponent_pokemon.name} greift {player_pokemon.name} an und verursacht {damage} Schaden!"
        
        if effectiveness > 1.0:
            message += " ✨ Das ist sehr effektiv!"
        elif effectiveness < 1.0:
            message += " 💧 Das ist nicht sehr effektiv..."
            
        if attack_result["critical"]:
            message += " 🎯 Kritischer Treffer!"
        
        battle_over = False
        winner = None
        
        if not player_pokemon.is_alive():
            message += f"\n💀 {player_pokemon.name} ist besiegt!"
            # Prüfen ob Spieler andere Pokemon hat
            if not self.player.has_usable_pokemon():
                battle_over = True
                winner = "opponent"
                message += "\n😵 Alle deine Pokemon sind besiegt!"
            else:
                message += "\n⚠️ Wähle ein neues Pokemon!"
        
        return {
            "success": True,
            "message": message,
            "battle_over": battle_over,
            "winner": winner
        }
    
    def _calculate_catch_rate(self, wild_pokemon, ball_type="pokeball"):
        """Berechnet die Fangchance für ein wildes Pokemon - Verbessert"""
        # Ball-Multiplikatoren
        ball_multipliers = {
            "pokeball": 1.0,
            "superball": 1.5,
            "hyperball": 2.0
        }
        
        # Basis-Fangchance
        base_rate = 0.3
        
        # HP-Bonus (weniger HP = leichter zu fangen)
        hp_factor = 1 - (wild_pokemon.get_hp_percentage() / 100)
        hp_bonus = hp_factor * 0.4
        
        # Level-Malus (höhere Level sind schwerer zu fangen)
        level_penalty = (wild_pokemon.level - 1) * 0.02
        
        # Ball-Bonus
        ball_bonus = ball_multipliers.get(ball_type, 1.0) - 1.0
        
        catch_rate = (base_rate + hp_bonus + ball_bonus) - level_penalty
        return max(0.05, min(0.95, catch_rate))  # Zwischen 5% und 95%
    
    def _calculate_exp_gain(self, defeated_pokemon):
        """Berechnet EXP-Gewinn für besiegtes Pokemon"""
        base_exp = GAME_CONFIG["exp_multiplier"]
        level_bonus = defeated_pokemon.level * 2
        random_bonus = random.randint(5, 15)
        
        # Bonus für starke Pokemon
        if defeated_pokemon.level > 10:
            level_bonus *= 1.5
        
        return int(base_exp + level_bonus + random_bonus)
    
    def get_battle_summary(self):
        """Gibt eine Zusammenfassung des Kampfes zurück"""
        return {
            "turns": self.turn_count,
            "is_wild": self.is_wild_battle,
            "opponent": self.opponent_pokemon.name if self.opponent_pokemon else "Trainer",
            "log": self.battle_log.copy()
        }
    
    def log(self, message):
        """Fügt Nachricht zum Kampf-Log hinzu"""
        self.battle_log.append(message)
        
    def get_battle_log(self):
        """Gibt das komplette Kampf-Log zurück"""
        return self.battle_log.copy()

def create_wild_pokemon(min_level=1, max_level=5):
    """Erstellt ein zufälliges wildes Pokemon"""
    # Entferne Starter-Pokemon aus wilden Begegnungen für Balancing
    available_pokemon = [name for name in POKEMON_DATA.keys() 
                        if name not in ["Glumanda", "Schiggy", "Bisasam"]]
    
    # Falls keine anderen Pokemon verfügbar, verwende alle
    if not available_pokemon:
        available_pokemon = list(POKEMON_DATA.keys())
    
    pokemon_name = random.choice(available_pokemon)
    level = random.randint(min_level, max_level)
    
    # Erstelle Pokemon
    wild_pokemon = Pokemon(pokemon_name, level)
    
    # Zufällige HP-Variation für wilde Pokemon (macht sie interessanter)
    hp_variation = random.uniform(0.7, 1.0)
    wild_pokemon.current_hp = int(wild_pokemon.max_hp * hp_variation)
    
    return wild_pokemon

def create_trainer_pokemon(trainer_name, pokemon_list, base_level=5):
    """Erstellt Pokemon für einen Trainer-NPC"""
    trainer_pokemon = []
    for pokemon_name in pokemon_list:
        if pokemon_name in POKEMON_DATA:
            # Leichter Level-Variation für Trainer
            level = base_level + random.randint(-1, 2)
            level = max(1, level)  # Minimum Level 1
            
            pokemon = Pokemon(pokemon_name, level)
            trainer_pokemon.append(pokemon)
    
    return trainer_pokemon