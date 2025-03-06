
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

class TourAgent:
    MAX_TOURS = 3
    List_of_agents = []

    def __init__(self, name):
        self.name = name
        self.tours = []
        TourAgent.List_of_agents.append(self)
    
    def __str__(self):
        return f"Tour agent {self.name} (have {len(self.tours)} tours)"

    def add_tour(self, tour):
        # Перевіряємо, чи тур вже є в списку турів всіх агентів
        if any(tour in agent.tours for agent in TourAgent.List_of_agents):
            print(f"Tour '{tour.name}' already assigned to another agent.")
        elif len(self.tours) < self.MAX_TOURS:
            self.tours.append(tour)
            print(f"Tour '{tour.name}' added to agent {self.name}.")
        else:
            print(f"Agent {self.name} cannot handle more than {self.MAX_TOURS} tours.")
        
    def remove_tour(self,tour):
        if len(self.tours) > 0:
            self.tours.remove(tour)
            print(f"Tour '{tour.name}' remove from agent {self.name}.")
        else:
            print(f"Agent {self.name} don`t handle a tour.")
    
    @classmethod
    def get_all_tours(cls):
        if not cls.List_of_agents:
            print("No agents have been added yet.")
        else:
            print("\nAll Available agents and their tours:")
            for agent in cls.List_of_agents:
                print(f"{agent}:")
                if agent.tours:  # Перевіряємо, чи є тури в агента
                    for tour in agent.tours:
                        print(f"  - {tour}")
                else:
                    print("  No tours assigned.")

                    
# Створюємо тури різних типів
tour1 = Tour("Amazon", 12, 450, 2)
tour2 = RelaxTour("Turkey", 6, 300, 2, 0)
tour3 = ExtremeTour("Slovakia", 2, 1000, 1, ["Rope", "Backpac"])
tour4 = CulturalTour("Greece", 10, 1500, 4, ["Acropolis", "National Archaeological"])

# Створюємо агентів
agent1 = TourAgent("John")
agent2 = TourAgent("Alice")

# Додаємо тури агентам
agent1.add_tour(tour1)
agent1.add_tour(tour2)
agent2.add_tour(tour3)
agent2.add_tour(tour4)

# Виводимо список всіх агентів та їх турів
TourAgent.get_all_tours()

print("\n")
# Перевіряємо ціни турів та типи турів (дорогий, дешевий, середній)
tour1.expensive_check()
tour2.expensive_check()
tour3.expensive_check()
tour4.expensive_check()

# Додаємо нові елементи до обладнання для екстремального туру
tour3.add_equipment(["Bottle", "Gloves", "Helmet"])

# Видаляємо один елемент обладнання
tour3.remove_equipment("Helmet")

# Виводимо тур після змін в обладнанні
print("\nAfter adding and removing equipment:")
print(tour3)

# Видаляємо один з турів у агента
agent1.remove_tour(tour2)

# Перевіряємо, чи змінився список турів у агента після видалення
print("\nAfter removing a tour:")
TourAgent.get_all_tours()

# Спробуємо додати більше турів, ніж дозволено
agent1.add_tour(tour4)
agent1.add_tour(tour3)
