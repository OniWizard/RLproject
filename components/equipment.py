from engine.equipment_slots import EquipmentSlots


class Equipment:
    """
    Handles aspects of entities that are equipment
    """
    def __init__(self, main_hand=None, off_hand=None, body=None, legs=None, feet=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.body = body
        self.legs = legs
        self.feet = feet

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        return bonus

    @property
    def str_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.strength_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.strength_bonus

        return bonus

    @property
    def int_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.intelligence_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.intelligence_bonus

        return bonus

    @property
    def armor_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.armor_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.armor_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        return results
