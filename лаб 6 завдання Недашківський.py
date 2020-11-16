class Box:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        if self.value == 1:
            return True
        else:
            return False

box = Box(0)
result = bool(box)
print(result)

box = Box(1)
result = bool(box)
print(result)

box = Box(2)
result = bool(box)
print(result)
