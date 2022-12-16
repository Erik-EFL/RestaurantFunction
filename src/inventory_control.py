class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = {
            ingredient: 0
            for ingredient in self.MINIMUM_INVENTORY
            
        }

    def add_new_order(self, _customer, order, _day):
        """ adds a new order to the inventory """
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] <= 0:
                return False
            self.inventory[ingredient] += 1

    def get_quantities_to_buy(self):
        """ returns the quantities to buy """
        return {
            ingredient: self.MINIMUM_INVENTORY[ingredient] - amount
            for ingredient, amount in self.inventory.items()
        }
