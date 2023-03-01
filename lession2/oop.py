# Trong Python, đóng gói (Encapsulation) được thực hiện thông qua việc sử dụng các thuộc tính và phương thức có phạm vi truy cập khác nhau. Có ba loại phạm vi truy cập trong Python là: public, protected và private.

# Public: Các thuộc tính và phương thức có phạm vi truy cập public có thể được truy cập từ bên ngoài lớp.
# Protected: Các thuộc tính và phương thức có phạm vi truy cập protected được xác định bằng ký hiệu " _ " ở đầu tên, và chỉ có thể được truy cập từ lớp con hoặc các phương thức của lớp đó.
# Private: Các thuộc tính và phương thức có phạm vi truy cập private được xác định bằng ký hiệu " __ " ở đầu tên, và chỉ có thể được truy cập từ bên trong lớp đó.
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name            # thuộc tính public
        self._age = age             # thuộc tính protected
        self.__gender = 'unknown'   # thuộc tính private

    def speak(self):
        print(f"Hi, my name is {self.name}. I'm {self._age} years old.")

    def __get_gender(self):        # phương thức private
        return self.__gender

    def introduce(self):
        # truy cập phương thức private
        print(f"My gender is {self.__get_gender()}")


person1 = Person("John", 25)
person1.speak()             # Output: Hi, my name is John. I'm 25 years old.
person1.introduce()         # Output: My gender is unknown


# ===================Kế thừa=========================
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species='Dog')
        self.breed = breed

    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species='Cat')
        self.color = color

    def make_sound(self):
        print("Meow!")


dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.name)         # Output: Buddy
print(dog1.species)      # Output: Dog
print(dog1.breed)        # Output: Golden Retriever
dog1.make_sound()        # Output: Woof!

cat1 = Cat("Misty", "Gray")
print(cat1.name)         # Output: Misty
print(cat1.species)      # Output: Cat
print(cat1.color)        # Output: Gray
cat1.make_sound()        # Output: Meow!


# ================== Đa hình=====================


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Meow!"


def animal_sound(animal):
    print(animal.make_sound())


dog = Dog("Buddy")
cat = Cat("Misty")

animal_sound(dog)   # Output: Woof!
animal_sound(cat)   # Output: Meow!

# Trong Python, tính trừu tượng (Abstraction) là khả năng giấu đi những chi tiết cài đặt bên trong của một đối tượng và chỉ hiển thị các tính năng cần thiết để sử dụng. Tính trừu tượng giúp tăng tính bảo mật, tính linh hoạt và giảm thiểu sự phức tạp trong việc sử dụng đối tượng.

# Ví dụ về tính trừu tượng trong Python:


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Walks on four legs"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Meow!"

    def move(self):
        return "Walks on four legs"


def animal_sound_and_move(animal):
    print(animal.name + " makes sound: " + animal.make_sound())
    print(animal.name + " " + animal.move())


dog = Dog("Buddy")
cat = Cat("Misty")

# Output: Buddy makes sound: Woof! Buddy Walks on four legs
animal_sound_and_move(dog)
# Output: Misty makes sound: Meow! Misty Walks on four legs
animal_sound_and_move(cat)
