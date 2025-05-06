from models import Author, Work, MediaCompany
from royalties import calculate_royalties

# Створення авторів
author1 = Author("Іван Петренко", True)
author2 = Author("John Smith", False)

# Твір і розподіл часток
work1 = Work("Моя казка")
work1.assign_author(author1, 0.6)
work1.assign_author(author2, 0.4)

# Компанія
company = MediaCompany("Media UA")
company.add_profit("2024-05", 10000)

# Розрахунок
report, tax_sum = calculate_royalties(company, [work1], "2024-05")

# Вивід
for r in report:
    print(r)
print("Загальний податок:", tax_sum)
