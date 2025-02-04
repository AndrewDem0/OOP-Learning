
class Triangle:

    # список всіх трикутників 
    list_of_items = [] 
    
    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b: # теорема про існування трикутника
            self.a = a
            self.b = b
            self.c = c
            Triangle.list_of_items.append(self)
            print(f"\n Triangle {self.display_triangle()} append succsesfuly")
        else:
            print("\n This triangle cannot exist")
    
    # множення на число
    def scale(self, x): 
        self.a *= x
        self.b *= x
        self.c *= x
    
    # обрахунок периметру
    def perimeter(self): 
        return self.a + self.b + self.c

    # обрахунок площі
    def square(self): 
        s = self.perimeter() / 2 
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    # відображення поточного трикутника
    def display_triangle(self): 
        return f"/_\ ({self.a}; {self.b}; {self.c})"

    # виведення всіх трикутників
    @staticmethod
    def display_all_triangles(): 
        for t in Triangle.list_of_items:
            print(f" /_\ ({t.a}; {t.b}; {t.c})")
 
# створення  трикутників
t1 = Triangle(3, 4, 5)
t2 = Triangle(1, 2, 3)
t3 = Triangle(6, 8, 10)

print(f"\n Triangle t1 = {t1.display_triangle()}, perimeter = {t1.perimeter()}, square = {t1.square()} ")
print(f"\n Triangle t3 = {t3.display_triangle()}, perimeter = {t3.perimeter()}, square = {t3.square()} ")

print (f"\n Triangle t1 before scale: {t1.display_triangle()} ")
t1.scale(3)
print (f"\n Triangle t1 after scale: {t1.display_triangle()}")

print("\n Ther is oll Triangles ↓")
Triangle.display_all_triangles()