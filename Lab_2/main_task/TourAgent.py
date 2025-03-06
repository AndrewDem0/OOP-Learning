
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