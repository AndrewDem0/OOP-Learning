from abc import ABC, abstractmethod

class Author:
    def __init__(self, full_name, is_resident=True):
        self.full_name = full_name
        self.is_resident = is_resident

    def __str__(self):
        return f"{self.full_name} ({'резидент' if self.is_resident else 'нерезидент'})"


class Work:
    def __init__(self, title):
        self.title = title
        self.authors_shares = {}  # {Author: float}

    def assign_author(self, author, share):
        self.authors_shares[author] = share

    def __str__(self):
        return f"'{self.title}' з {len(self.authors_shares)} авторами"


class Company(ABC):
    def __init__(self, name):
        self.name = name
        self.monthly_profits = {}  # {'2024-01': 10000, ...}

    def add_profit(self, month, amount):
        self.monthly_profits[month] = self.monthly_profits.get(month, 0) + amount

    @abstractmethod
    def royalty_percent(self):
        pass


class MediaCompany(Company):
    def royalty_percent(self):
        return 0.8


class EntertainmentCompany(Company):
    def royalty_percent(self):
        return 0.5


class OtherCompany(Company):
    def royalty_percent(self):
        return 0.2
