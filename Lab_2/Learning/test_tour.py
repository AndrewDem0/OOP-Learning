class Tour:
    
    all_tours = []  # Збереження всіх створених турів
     
    def __init__(self, name, duration, price):
        self.name = name
        self.duration = duration
        self.price = price
        Tour.all_tours.append(self)  # Додаємо новий тур у загальний список

    def get_info(self):
        return f"{self.name}: {self.duration} days, ${self.price}"
    
    @classmethod
    def get_all_tours(cls):
        """Виводить інформацію про всі створені тури."""
        if not cls.all_tours:
            print("No tours have been created yet.")
        else:
            print("\nAll Available Tours:")
            for tour in cls.all_tours:
                print(f"  - {tour.get_info()}")

class AdventureTour(Tour):
    def __init__(self, name, duration, price, equipment):
        super().__init__(name, duration, price)
        self.equipment = equipment

    def get_info(self):
        return super().get_info() + f" | Equipment needed: {self.equipment}"


class RelaxationTour(Tour):
    def __init__(self, name, duration, price, spa_included):
        super().__init__(name, duration, price)
        self.spa_included = spa_included

    def get_info(self):
        return super().get_info() + f" | Spa included: {'Yes' if self.spa_included else 'No'}"


class CulturalTour(Tour):
    def __init__(self, name, duration, price, museums):
        super().__init__(name, duration, price)
        self.museums = museums

    def get_info(self):
        return super().get_info() + f" | Museums visited: {', '.join(self.museums)}"


class TourAgent:
    MAX_TOURS = 3

    def __init__(self, name):
        self.name = name
        self.tours = []

    def add_tour(self, tour):
        if len(self.tours) < self.MAX_TOURS:
            self.tours.append(tour)
            print(f"Tour '{tour.name}' added to agent {self.name}.")
        else:
            print(f"Agent {self.name} cannot handle more than {self.MAX_TOURS} tours.")

    def get_tours(self):
        return [tour.get_info() for tour in self.tours]

tour1 = AdventureTour("Jungle Safari", 5, 750, "Binoculars")
tour2 = RelaxationTour("Maldives Retreat", 7, 2000, True)
tour3 = CulturalTour("Rome Heritage Tour", 4, 900, ["Colosseum", "Vatican Museums"])
tour4 = AdventureTour("Everest Base Camp", 12, 3000, "Climbing Gear")

# === Виводимо всі створені тури ===
Tour.get_all_tours()
