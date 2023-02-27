def sum(a, b):
    return a + b


def add_element(list):
    list.append(4)


# Gọi hàm sum() để tính tổng hai số 2 và 3
result = sum(2, 3)
print(result)  # Kết quả là 5


my_list = [1, 2, 3]
add_element(my_list)
print(my_list)  # Kết quả là [1, 2, 3, 4]


# ví dụ về class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# Tạo đối tượng của lớp Person
person1 = Person("Alice", 30)

# Truy cập thuộc tính của đối tượng
print(person1.name)
print(person1.age)

# Gọi phương thức của đối tượng
print(person1.get_name())
print(person1.get_age())
