from Tour import *
from TourAgent import *

# Створюємо тури різних типів
tour1 = Tour("Amazon", 12, 450, 2)
tour2 = RelaxTour("Turkey", 6, 300, 2, 0)
tour3 = ExtremeTour("Slovakia", 2, 1000, 1, ["Rope", "Backpac"])
tour4 = CulturalTour("Greece", 10, 1500, 4, ["Acropolis", "National Archaeological"])

# Створюємо агентів
agent1 = TourAgent("John")
agent2 = TourAgent("Alice")

Tour.get_all_tours()
TourAgent.get_all_tours()

# Додаємо тури агентам
agent1.add_tour(tour1)
agent1.add_tour(tour2)
agent2.add_tour(tour3)
agent2.add_tour(tour4)

TourAgent.get_all_tours()

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