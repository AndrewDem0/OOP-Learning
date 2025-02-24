
class Triangle:

    # список всіх трикутників 
    list_of_items = [] 
    
    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b: # теорема про існування трикутника
            self.a = a
            self.b = b
            self.c = c
            Triangle.list_of_items.append(self)
            print(f"\n Triangle {self} append succsesfuly")
        else:
            print("\n This triangle cannot exist")
    
    # обрахунок периметру
    def perimeter(self): 
        return self.a + self.b + self.c

    # обрахунок площі
    def square(self): 
        s = self.perimeter() / 2 
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    # визначення подібності трикутників
    def similarity(self, other):
        if isinstance(other, Triangle):
            return (self.a / other.a) == (self.b / other.b) == (self.c / other.c)
        return NotImplemented
    
    # магічний метод для відображення трикутника
    def __str__(self): 
        return f"/_\\ ({self.a}; {self.b}; {self.c})"
    
    # магічний метод для порівняння трикутників(>)
    def __gt__(self, other):
        if isinstance(other, Triangle):
            return self.square() > other.square()
        return NotImplemented
    
    # магічний метод для порівняння трикутників(<)
    def __lt__(self, other):
        if isinstance(other, Triangle):
            return self.square() < other.square()
        return NotImplemented
    
    # магічний метод множення на число(*)
    def __mul__(self, x):
        if not isinstance(x, int):
            raise ValueError("The multiplier must be an integer")
        self.a *= x
        self.b *= x
        self.c *= x

    # магічний метод ділення на число(/)
    def __truediv__(self, x):
        if not isinstance(x, int):
            raise ValueError("The divider must be an integer")
        self.a /= x
        self.b /= x
        self.c /= x

    # виведення всіх трикутників
    @staticmethod
    def display_all_triangles(): 
        for t in Triangle.list_of_items:
            print(t)
 
# створення  трикутників
t1 = Triangle(10, 10, 10)
t2 = Triangle(5, 12, 13)
t3 = Triangle(6, 8, 10)


print(f"\n Triangle t1 = {t1}, perimeter = {t1.perimeter()}, square = {t1.square()} ")
print(f"\n Triangle t1 = {t2}, perimeter = {t2.perimeter()}, square = {t2.square()} ")
print(f"\n Triangle t3 = {t3}, perimeter = {t3.perimeter()}, square = {t3.square()} ")

print(f"\n Triangle t1 > t2: {t1 > t2}")
print(f"\n Triangle t1 > t2: {t1 < t3}")

print (f"\n Triangle t1 before scale: {t1} ")
t1 * 9
print (f"\n Triangle t1 after scale: {t1}")

print (f"\n Triangle t1 before division: {t1} ")
t1 / 3
print (f"\n Triangle t1 after division: {t1}")

print(f"\n t1 {t1}")

print("\n Ther is all Triangles ↓")
Triangle.display_all_triangles()
