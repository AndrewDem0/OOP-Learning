
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

class Triangle {
public:
    static std::vector<Triangle*> list_of_items; // std::vector динам. контейнер тобто змінює розмір під час виконання + контроль пам'яті
    // за допомогою * зберігає вказівник на об'єкт а не сам об'єкт
    Triangle(double a, double b, double c) {
        if (a + b > c && b + c > a && a + c > b) { // this дозволяє компілятору розрізнити локальні змінні від глобальних
            this->a = a;
            this->b = b;
            this->c = c;
            list_of_items.push_back(this);
            std::cout << "\n Triangle " << *this << " append successfully" << std::endl;
        } else {
            std::cout << "\n This triangle cannot exist" << std::endl;
        }
    }

    double perimeter() const { // const - метод не може змінювати дані класу крім mutable
        return a + b + c;
    }

    double square() const {
        double s = perimeter() / 2;
        return std::sqrt(s * (s - a) * (s - b) * (s - c));
    }

    // Оператор виводу
    friend std::ostream& operator<<(std::ostream& os, const Triangle& t) { // friend - дозволяє функції мати доступ до приватних членів класу
        os << "/_\\ (" << t.a << "; " << t.b << "; " << t.c << ")";
        return os;
    }

    // Оператори порівняння
    bool operator > (const Triangle& other) const {
        return this->square() > other.square();
    }

    bool operator < (const Triangle& other) const {
        return this->square() < other.square();
    }

    // Оператор множення
    Triangle operator * (int x) {
        a = a * x;
        b = b * x;
        c = c * x;
    }

    // Оператор ділення
    Triangle operator / (int x) {
        a = a / x;
        b = b / x;
        c = c / x;
    }

    static void display_all_triangles() {
        for (const auto& t : list_of_items) { // auto& дає посилання на об'єкт вектора
            std::cout << *t << "\n";
        }
    }

private:
    double a, b, c;
};

// Ініціалізація статичного вектора
std::vector<Triangle*> Triangle::list_of_items;

int main() {
    Triangle t1(10, 10, 10);
    Triangle t2(5, 12, 13);
    Triangle t3(6, 8, 10);

    std::cout << "t1: " << t1 << ", Perimeter: " << t1.perimeter() << ", Square: " << t1.square() << "\n";
    std::cout << "t2: " << t2 << ", Perimeter: " << t2.perimeter() << ", Square: " << t2.square() << "\n";
    std::cout << "t3: " << t3 << ", Perimeter: " << t3.perimeter() << ", Square: " << t3.square() << "\n";

    std::cout << "t1 > t2: " << (t1 > t2 ? "True" : "False") << "\n";
    std::cout << "t1 < t3: " << (t1 < t3 ? "True" : "False") << "\n";

     t1 * 2;
    std::cout << "After scaling t1 * 2: " << t1 << "\n";

     t1 / 2;
    std::cout << "After scaling t1 / 2: " << t1<< "\n";

    std::cout << "All triangles:\n";
    Triangle::display_all_triangles();

    return 0;
}