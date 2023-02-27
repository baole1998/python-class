# Dưới đây là một số ví dụ về OOP để giúp bạn hiểu rõ hơn về các đặc điểm của nó:

# Ví dụ về đóng gói (Encapsulation):
# Trong ví dụ này, chúng ta có một lớp hình vuông (Square) và
# chúng ta sử dụng đóng gói để giấu chi tiết bên trong của lớp như chiều dài, chiều rộng của hình vuông.

class Square:
    def __init__(self, side):
        self.__side = side  # đóng gói chiều dài cạnh bằng cách sử dụng dấu gạch chân trước tên biến

    def area(self):
        return self.__side ** 2


square = Square(5)
print(square.area())  # Kết quả là 25

# Trong ví dụ trên, ta sử dụng đóng gói bằng cách đặt dấu gạch chân trước tên thuộc tính để giấu chi tiết bên trong của lớp,
# và người dùng chỉ cần sử dụng phương thức area() để tính diện tích của hình vuông.

# Ví dụ về kế thừa (Inheritance):
# Trong ví dụ này, chúng ta có một lớp động vật (Animal) và các lớp con của nó như chó (Dog), mèo (Cat) và vịt (Duck).

# python
# Copy code


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"
# Trong ví dụ này, các lớp con (Dog, Cat, Duck) kế thừa các thuộc tính và phương thức từ lớp cha (Animal),
# và mỗi lớp con có phương thức speak() khác nhau.
