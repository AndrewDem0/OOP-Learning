
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
            std::cout << "\n Triangle " << display_triangle() << " append successfully" << std::endl;
        } else {
            std::cout << "\n This triangle cannot exist" << std::endl;
        }
    }

    void scale(double x) {
        a *= x;
        b *= x;
        c *= x;
    }

    double perimeter() const { // const - метод не може змінювати дані класу крім mutable
        return a + b + c;
    }

    double square() const {
        double s = perimeter() / 2;
        return std::sqrt(s * (s - a) * (s - b) * (s - c));
    }

    std::string display_triangle() const {
        return "/_\\ (" + std::to_string(a) + "; " + std::to_string(b) + "; " + std::to_string(c) + ")";
    }

    static void display_all_triangles() {
        for (const auto& t : list_of_items) { // auto& дає посилання на об'єкт вектора
            std::cout << " /_\\ (" << t->a << "; " << t->b << "; " << t->c << ")" << std::endl;
        }
    }

private:
    double a, b, c;
};

std::vector<Triangle*> Triangle::list_of_items;

int main() {
    Triangle t1(3, 4, 5);
    Triangle t2(1, 2, 3);
    Triangle t3(6, 8, 10);

    std::cout << "\n Triangle t1 = " << t1.display_triangle() << ", perimeter = " << t1.perimeter() << ", square = " << t1.square() << std::endl;
    std::cout << "\n Triangle t3 = " << t3.display_triangle() << ", perimeter = " << t3.perimeter() << ", square = " << t3.square() << std::endl;

    std::cout << "\n Triangle t1 before scale: " << t1.display_triangle() << std::endl;
    t1.scale(3);
    std::cout << "\n Triangle t1 after scale: " << t1.display_triangle() << std::endl;

    std::cout << "\n There are all Triangles ↓" << std::endl;
    Triangle::display_all_triangles();

    return 0;
}