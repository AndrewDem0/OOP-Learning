class Tour():
    all_tours = [] # Збереження всіх створених турів
    
    def __init__(self, name, duration, price, headcount):
        self.name = name
        self.duration = duration
        self.price = price
        self.headcount = headcount
        Tour.all_tours.append(self)
    
    def __str__(self): 
        return f"{self.name}: {self.duration} days, {self.price} $, number of persons: {self.headcount}"
    
    def expensive_check(self):
        correlation = self.price / (self.headcount * self.duration)
        if correlation > 80:
            print(f"This tour: {self.name} is expensive | {correlation} $ one day per person")
        elif correlation <30:
            print(f"This tour: {self.name} is cheap | {correlation} $ one day per person")
        else:
            print(f"This tour: {self.name} is medium | {correlation} $ one day per person")
            
    @classmethod
    def get_all_tours(cls):
        if not cls.all_tours:
            print("No tours have been created yet.")
        else:
            print("\nAll Available Tours:")
            for tour in cls.all_tours:
                print(f"  - {(tour)}")
    
    @staticmethod
    def ensure_list(items):
        """Перевіряє, чи items є списком, і якщо ні, обгортає в список."""
        return items if isinstance(items, list) else [items]

class ExtremeTour(Tour):
    
    def __init__(self, name, duration, price, headcount, equipment):
        super().__init__(name, duration, price, headcount)
        self.equipment = Tour.ensure_list(equipment)
    
    def __str__(self):
        return super().__str__() + f" | Equipment needed: {', '.join(self.equipment)}"
    
    def add_equipment(self, new_items):
        new_items = Tour.ensure_list(new_items)
        for item in new_items:
            if item not in self.equipment:  # Перевіряємо, чи елемент вже є в списку
                self.equipment.append(item)
    
    def remove_equipment(self, elements_to_remove):
        elements_to_remove = Tour.ensure_list(elements_to_remove)
        for item in elements_to_remove:
            if item in self.equipment:
                self.equipment.remove(item)

class RelaxTour(Tour):
    
    def __init__(self, name, duration, price, headcount, spa_included):
        super().__init__(name, duration, price, headcount)
        self.spa_included = spa_included
    
    def __str__(self):
        return super().__str__() + f" | Spa included: {'Yes' if self.spa_included else 'No'}"

class CulturalTour(Tour):
    def __init__(self, name, duration, price, headcount, museums):
        super().__init__(name, duration, price, headcount,)
        self.museums = museums

    def __str__(self):
        return super().__str__() + f" | Museums visited: {', '.join(self.museums)}"