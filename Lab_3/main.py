from structure import Bank, RegularATM, SecureATM

bank = Bank()

print("=== Вивід усіх банкоматів у банку ===")
for atm in bank:
    print(atm)

print("\n=== Поповнення банкомату 'ATM-1' ===")
bank.atms["ATM-1"].deposit(500)

print("\n=== Спроба зняття з банкомату 'ATM-2' з неправильним PIN ===")
bank.atms["ATM-2"].withdraw(300, "1234")  # неправильний PIN

print("\n=== Зняття з 'ATM-2' з правильним PIN ===")
bank.atms["ATM-2"].withdraw(300, "2222")  # правильний PIN

print("\n=== Спроба зняття з 'ATM-3' з неправильним SMS-кодом ===")
bank.atms["ATM-3"].withdraw(500, "3333", "0000")  # неправильний SMS-код

print("\n=== Друга неправильна спроба — заблокується ===")
bank.atms["ATM-3"].withdraw(500, "3333", "1111")  # ще один неправильний код

print("\n=== Спроба зняття з заблокованого 'ATM-3' ===")
bank.atms["ATM-3"].withdraw(100, "3333", "3333")

print("\n=== Додавання нового банкомату ===")
bank.add_atm(RegularATM("ATM-4", "4444", 2000))
print(bank.atms["ATM-4"])

print("\n=== Видалення банкомату 'ATM-2' ===")
bank.remove_atm("ATM-2")

print("\n=== Фінальний стан банкоматів ===")
for atm in bank:
    print(atm)
