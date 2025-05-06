class InstanceLimitMeta(type):
    _max_instances = 3

    def __new__(cls, name, bases, dct):
        dct['_instance_count'] = 0
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        if cls._instance_count >= InstanceLimitMeta._max_instances:
            raise Exception(f"Ліміт у {InstanceLimitMeta._max_instances} екземплярів досягнуто для класу {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        cls._instance_count += 1
        return instance

class MyClass(metaclass=InstanceLimitMeta):
    def __init__(self, name):
        self.name = name
        print(f"[init] Ініціалізовано екземпляр з name = {self.name}")

try:
    a = MyClass("A")
    b = MyClass("B")
    c = MyClass("C")
    d = MyClass("D")
except Exception as e:
    print("Помилка:", e)
