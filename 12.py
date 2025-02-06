class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(x=1, y=2)
v2 = Vector(x=1, y=7)

result = v1 + v2

print(result.x) # 2
print(result.y) # 9