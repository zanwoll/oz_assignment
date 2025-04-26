class Eagle:

    def __init__(self, name, wingspan, age):

        Args:
            name (str): 독수리의 이름
            wingspan (float): 날개 길이(미터)
            age (int): 독수리의 나이
        self.name = name
        self.wingspan = wingspan
        self.age = age

    def fly(self):
        return "높이 날아오릅니다!"

    def info(self):
        return f"이름: {self.name}, 날개 길이: {self.wingspan}m, 나이: {self.age}세"