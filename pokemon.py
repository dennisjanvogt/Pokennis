# pokemon.py
"""
Pokemon Klasse mit allen Eigenschaften und Methoden
"""
import random
from game_data import POKEMON_DATA, TYPE_EFFECTIVENESS

class Pokemon:
    def __init__(self, name, level=1):
        if name not in POKEMON_DATA:
            raise ValueError(f"Pokemon {name} nicht in der Datenbank gefunden!")
        
        self.name = name
        self.level = level
        data = POKEMON_DATA[name]
        
        # Basis-Werte basierend auf Level
        self.typ = data["typ"]
        self.color = data["color"]
        self.description = data["description"]
        
        # Stats berechnen
        self.max_hp = self._calculate_stat(data["hp"], level)
        self.current_hp = self.max_hp
        self.attack = self._calculate_stat(data["attack"], level)
        self.defense = self._calculate_stat(data["defense"], level)
        
        # Erfahrung
        self.exp = 0
        self.exp_to_next_level = self._calculate_exp_needed()
        
        # Status
        self.status = "Normal"  # Normal, Vergiftet, Paralysiert, etc.
        
    def _calculate_stat(self, base_stat, level):
        """Berechnet einen Stat basierend auf Basis-Wert und Level"""
        return int(base_stat + (level - 1) * (base_stat * 0.1))
    
    def _calculate_exp_needed(self):
        """Berechnet benötigte EXP für nächstes Level"""
        return int(self.level * 25 * (1 + self.level * 0.1))
    
    def is_alive(self):
        """Prüft ob Pokemon noch kampffähig ist"""
        return self.current_hp > 0
    
    def heal(self):
        """Heilt Pokemon vollständig"""
        self.current_hp = self.max_hp
        self.status = "Normal"
    
    def take_damage(self, damage, attacker_type=None):
        """Pokemon nimmt Schaden, berücksichtigt Typ-Effektivität"""
        # Typ-Effektivität berechnen
        effectiveness = 1.0
        if attacker_type and attacker_type in TYPE_EFFECTIVENESS:
            defender_types = self.typ.split("/")
            for defender_type in defender_types:
                if defender_type in TYPE_EFFECTIVENESS[attacker_type]:
                    effectiveness *= TYPE_EFFECTIVENESS[attacker_type][defender_type]
        
        # Schaden berechnen
        defense_reduction = max(1, self.defense // 4)
        actual_damage = max(1, int((damage - defense_reduction) * effectiveness))
        
        self.current_hp = max(0, self.current_hp - actual_damage)
        
        return actual_damage, effectiveness
    
    def attack_pokemon(self, target):
        """Greift ein anderes Pokemon an"""
        base_damage = self.attack + random.randint(-3, 3)
        damage, effectiveness = target.take_damage(base_damage, self.typ.split("/")[0])
        
        return {
            "damage": damage,
            "effectiveness": effectiveness,
            "critical": random.random() < 0.1  # 10% Kritische Treffer
        }
    
    def gain_exp(self, exp):
        """Pokemon erhält Erfahrungspunkte"""
        self.exp += exp
        leveled_up = False
        
        while self.exp >= self.exp_to_next_level:
            leveled_up = True
            self.level_up()
            
        return leveled_up
    
    def level_up(self):
        """Pokemon steigt ein Level auf"""
        self.exp -= self.exp_to_next_level
        self.level += 1
        
        # Stats neu berechnen
        old_stats = {
            "hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense
        }
        
        data = POKEMON_DATA[self.name]
        self.max_hp = self._calculate_stat(data["hp"], self.level)
        self.attack = self._calculate_stat(data["attack"], self.level)
        self.defense = self._calculate_stat(data["defense"], self.level)
        
        # HP entsprechend erhöhen
        hp_gain = self.max_hp - old_stats["hp"]
        self.current_hp += hp_gain
        
        self.exp_to_next_level = self._calculate_exp_needed()
        
        return {
            "old_stats": old_stats,
            "new_stats": {
                "hp": self.max_hp,
                "attack": self.attack,
                "defense": self.defense
            },
            "hp_gain": hp_gain
        }
    
    def get_hp_percentage(self):
        """Gibt HP-Prozentsatz zurück"""
        if self.max_hp == 0:
            return 0
        return (self.current_hp / self.max_hp) * 100
    
    def get_exp_percentage(self):
        """Gibt EXP-Prozentsatz zum nächsten Level zurück"""
        if self.exp_to_next_level == 0:
            return 100
        return (self.exp / (self.exp + self.exp_to_next_level)) * 100
    
    def get_info_dict(self):
        """Gibt alle wichtigen Infos als Dictionary zurück"""
        return {
            "name": self.name,
            "level": self.level,
            "typ": self.typ,
            "hp": self.current_hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "exp": self.exp,
            "exp_to_next": self.exp_to_next_level,
            "status": self.status,
            "color": self.color,
            "description": self.description,
            "hp_percentage": self.get_hp_percentage(),
            "exp_percentage": self.get_exp_percentage()
        }
    
    def __str__(self):
        return f"{self.name} (Lv.{self.level}) - {self.current_hp}/{self.max_hp} HP"
    
    def __repr__(self):
        return f"Pokemon(name='{self.name}', level={self.level}, hp={self.current_hp}/{self.max_hp})"