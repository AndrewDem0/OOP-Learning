from abc import ABC, abstractmethod

class ATM(ABC):
    def __init__(self,name, pin_code, balance = 0):
        self.name = name
        self.pin_code = pin_code
        self.balance = balance
        self.status = False
        
    def deposit(self, amount):
        self.balance += amount
        print(f"[+] Deposited: {amount}. Balance: {self.balance}")
        
    def check_balance(self):
        return self.balance
    
    def get_status(self):
        return "Blocked" if self.status else "Active"
    
    def __str__(self):
        return f"{self.name} | {self.__class__.__name__} | Balance: {self.balance} | Status: {self.get_status()}"

    
    @abstractmethod
    def withdraw(self, amout, entered_pin, confirmation_code = None):
        pass
    
class RegularATM(ATM):
    def withdraw(self, amount, entered_pin, confirmation_code = None):
        if self.status:
            print("[!] ATM is blocked")
            return
        
        if entered_pin != self.pin_code:
            print("[!] Incorrect PIN")
            return
        
        if self.balance < amount:
            print("[!] Insufficient funds. ATM is now blocked")
            self.status = True
        else:
            self.balance -= amount
            print(f"[-] Withdrawn: {amount}. Balance: {self.balance}")

class SecureATM(RegularATM):
    def __init__(self,name, pin_code, sms_code, balance = 0):
        super().__init__(name, pin_code, balance)
        self.sms_code = sms_code
        self.failed_attempts = 0
        self.max_attempts = 2
        
    def withdraw(self, amount, entered_pin, confirmation_code=None):
        if self.status:
            print("[!] Secure ATM is blocked.")
            return

        if entered_pin != self.pin_code:
            print("[!] Incorrect PIN.")
            return

        if confirmation_code != self.sms_code:
            self.failed_attempts += 1
            print(f"[!] Incorrect SMS code. Attempt {self.failed_attempts}/{self.max_attempts}.")
            if self.failed_attempts >= self.max_attempts:
                self.status = True
                print("[!] Too many incorrect SMS attempts. Secure ATM is now blocked.")
            return

        if self.balance < amount:
            print("[!] Insufficient funds. Secure ATM is now blocked.")
            self.status = True
        else:
            self.balance -= amount
            print(f"[-] Secure Withdrawn: {amount}. Balance: {self.balance}")
            self.failed_attempts = 0

class Bank:
    def __init__(self):
        self.atms = {
            "ATM-1": RegularATM("ATM-1", "1111", 1000),
            "ATM-2": RegularATM("ATM-2", "2222", 1500),
            "ATM-3": SecureATM("ATM-3", "3333", "3333", 3000)
        }

    def add_atm(self, atm):
        self.atms[atm.name] = atm

    def remove_atm(self, name):
        if name in self.atms:
            del self.atms[name]
            print(f"[-] ATM '{name}' removed.")
        else:
            print(f"[!] ATM '{name}' not found.")

    def __iter__(self):
        return iter(self.atms.values())

