from structure import *

bank = Bank()

bank.add_atm(RegularATM("ATM-4", "4444", 500))

bank.add_atm(RegularATM("ATM-5", "5555", 700))

print("\n📋 Список банкоматів у банку:")
for atm in bank:
    print(atm)