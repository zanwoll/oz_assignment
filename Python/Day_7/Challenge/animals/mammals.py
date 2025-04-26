class Dog:

    def __init__(self, name, breed, age):
        초기화 메서드

        Args:
            name (str): 개의 이름
            breed (str): 개의 품종
            age (int): 개의 나이
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return "멍멍!"

    def info(self):
        return f"이름: {self.name}, 품종: {self.breed}, 나이: {self.age}세"